# Criar arquivo Python com classes e funções para interagir com o banco de dados

python_db_code = '''
# -*- coding: utf-8 -*-
"""
SISTEMA DE MEDIDAS PROTETIVAS - RONDA MARIA DA PENHA
29ª CIPM SEABRA - BAHIA

Módulo de acesso ao banco de dados SQLite
Autor: Sistema Automatizado
Data: 2025-05-31
"""

import sqlite3
import hashlib
from datetime import datetime, date
from typing import List, Dict, Any, Optional
import json

class DatabaseManager:
    """Classe principal para gerenciamento do banco de dados"""
    
    def __init__(self, db_path: str = "medidas_protetivas.db"):
        self.db_path = db_path
    
    def get_connection(self):
        """Retorna conexão com o banco de dados"""
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row  # Permite acesso por nome da coluna
        return conn
    
    def execute_query(self, query: str, params: tuple = ()) -> List[Dict]:
        """Executa query SELECT e retorna resultados como lista de dicionários"""
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(query, params)
            columns = [description[0] for description in cursor.description]
            return [dict(zip(columns, row)) for row in cursor.fetchall()]
    
    def execute_update(self, query: str, params: tuple = ()) -> int:
        """Executa query INSERT/UPDATE/DELETE e retorna ID ou rows affected"""
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(query, params)
            conn.commit()
            return cursor.lastrowid or cursor.rowcount

class UsuarioService:
    """Serviços relacionados aos usuários do sistema"""
    
    def __init__(self, db_manager: DatabaseManager):
        self.db = db_manager
    
    def hash_senha(self, senha: str) -> str:
        """Cria hash da senha para armazenamento seguro"""
        return hashlib.sha256(senha.encode()).hexdigest()
    
    def validar_login(self, usuario: str, senha: str) -> Optional[Dict]:
        """Valida credenciais de login"""
        query = """
        SELECT id, usuario, nome_completo, perfil, ativo 
        FROM usuarios 
        WHERE usuario = ? AND senha = ? AND ativo = 1
        """
        resultados = self.db.execute_query(query, (usuario, senha))
        
        if resultados:
            # Atualizar último acesso
            self.db.execute_update(
                "UPDATE usuarios SET ultimo_acesso = CURRENT_TIMESTAMP WHERE id = ?",
                (resultados[0]['id'],)
            )
            return resultados[0]
        return None
    
    def criar_usuario(self, usuario: str, senha: str, nome_completo: str, perfil: str = 'operador') -> int:
        """Cria novo usuário no sistema"""
        senha_hash = self.hash_senha(senha)
        query = """
        INSERT INTO usuarios (usuario, senha, nome_completo, perfil)
        VALUES (?, ?, ?, ?)
        """
        return self.db.execute_update(query, (usuario, senha_hash, nome_completo, perfil))

class MedidaProtetivaService:
    """Serviços relacionados às medidas protetivas"""
    
    def __init__(self, db_manager: DatabaseManager):
        self.db = db_manager
    
    def criar_medida_completa(self, dados_medida: Dict, dados_vitima: Dict, dados_agressor: Dict, 
                             tipos_medidas: List[int], usuario_id: int) -> int:
        """Cria uma medida protetiva completa com vítima, agressor e tipos de medidas"""
        
        with self.db.get_connection() as conn:
            cursor = conn.cursor()
            
            try:
                # Inserir medida protetiva
                cursor.execute("""
                    INSERT INTO medidas_protetivas 
                    (numero_processo, data_concessao, juiz_responsavel, vara_competente, 
                     comarca, status, data_inicio_vigencia, observacoes, usuario_cadastro)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
                """, (
                    dados_medida['numero_processo'],
                    dados_medida['data_concessao'],
                    dados_medida['juiz_responsavel'],
                    dados_medida['vara_competente'],
                    dados_medida['comarca'],
                    dados_medida.get('status', 'ativa'),
                    dados_medida['data_inicio_vigencia'],
                    dados_medida.get('observacoes', ''),
                    usuario_id
                ))
                
                medida_id = cursor.lastrowid
                
                # Inserir dados da vítima
                cursor.execute("""
                    INSERT INTO vitimas 
                    (medida_protetiva_id, nome_completo, nome_social, cpf, data_nascimento,
                     telefone_principal, telefone_secundario, email, cep, logradouro, numero,
                     complemento, bairro, cidade, uf, escolaridade, profissao, renda_individual,
                     cor_raca, orientacao_sexual, estado_civil, filhos, contato_emergencia_nome,
                     contato_emergencia_telefone, contato_emergencia_parentesco)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """, (
                    medida_id, dados_vitima['nome_completo'], dados_vitima.get('nome_social'),
                    dados_vitima['cpf'], dados_vitima['data_nascimento'],
                    dados_vitima['telefone_principal'], dados_vitima.get('telefone_secundario'),
                    dados_vitima.get('email'), dados_vitima['cep'], dados_vitima['logradouro'],
                    dados_vitima['numero'], dados_vitima.get('complemento'), dados_vitima['bairro'],
                    dados_vitima['cidade'], dados_vitima['uf'], dados_vitima['escolaridade'],
                    dados_vitima['profissao'], dados_vitima.get('renda_individual'),
                    dados_vitima['cor_raca'], dados_vitima.get('orientacao_sexual'),
                    dados_vitima['estado_civil'], dados_vitima.get('filhos', 0),
                    dados_vitima.get('contato_emergencia_nome'),
                    dados_vitima.get('contato_emergencia_telefone'),
                    dados_vitima.get('contato_emergencia_parentesco')
                ))
                
                # Inserir dados do agressor
                cursor.execute("""
                    INSERT INTO agressores 
                    (medida_protetiva_id, nome_completo, cpf, data_nascimento, telefone,
                     email, cep, logradouro, numero, complemento, bairro, cidade, uf,
                     profissao, local_trabalho, tipo_relacionamento, tempo_relacionamento,
                     relacionamento_ativo, uso_alcool_drogas, porte_arma, antecedentes_criminais)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """, (
                    medida_id, dados_agressor['nome_completo'], dados_agressor.get('cpf'),
                    dados_agressor.get('data_nascimento'), dados_agressor.get('telefone'),
                    dados_agressor.get('email'), dados_agressor.get('cep'),
                    dados_agressor.get('logradouro'), dados_agressor.get('numero'),
                    dados_agressor.get('complemento'), dados_agressor.get('bairro'),
                    dados_agressor.get('cidade'), dados_agressor.get('uf'),
                    dados_agressor.get('profissao'), dados_agressor.get('local_trabalho'),
                    dados_agressor['tipo_relacionamento'], dados_agressor.get('tempo_relacionamento'),
                    dados_agressor.get('relacionamento_ativo', 0),
                    dados_agressor.get('uso_alcool_drogas', 0),
                    dados_agressor.get('porte_arma', 0),
                    dados_agressor.get('antecedentes_criminais', 0)
                ))
                
                # Inserir tipos de medidas aplicadas
                for tipo_id in tipos_medidas:
                    cursor.execute("""
                        INSERT INTO medidas_aplicadas (medida_protetiva_id, tipo_medida_id, data_aplicacao)
                        VALUES (?, ?, ?)
                    """, (medida_id, tipo_id, dados_medida['data_concessao']))
                
                conn.commit()
                return medida_id
                
            except Exception as e:
                conn.rollback()
                raise e
    
    def listar_medidas(self, status: str = None, limit: int = 50) -> List[Dict]:
        """Lista medidas protetivas com filtros opcionais"""
        query = """
        SELECT m.*, v.nome_completo as vitima_nome, a.nome_completo as agressor_nome
        FROM medidas_protetivas m
        JOIN vitimas v ON m.id = v.medida_protetiva_id
        JOIN agressores a ON m.id = a.medida_protetiva_id
        """
        params = []
        
        if status:
            query += " WHERE m.status = ?"
            params.append(status)
        
        query += " ORDER BY m.data_concessao DESC LIMIT ?"
        params.append(limit)
        
        return self.db.execute_query(query, tuple(params))
    
    def buscar_medida_por_processo(self, numero_processo: str) -> Optional[Dict]:
        """Busca medida protetiva pelo número do processo"""
        query = """
        SELECT m.*, v.nome_completo as vitima_nome, v.telefone_principal as vitima_telefone,
               a.nome_completo as agressor_nome, a.telefone as agressor_telefone
        FROM medidas_protetivas m
        JOIN vitimas v ON m.id = v.medida_protetiva_id
        JOIN agressores a ON m.id = a.medida_protetiva_id
        WHERE m.numero_processo = ?
        """
        resultados = self.db.execute_query(query, (numero_processo,))
        return resultados[0] if resultados else None
    
    def atualizar_status_medida(self, medida_id: int, novo_status: str, observacoes: str = "") -> bool:
        """Atualiza status de uma medida protetiva"""
        query = """
        UPDATE medidas_protetivas 
        SET status = ?, observacoes = ?, data_atualizacao = CURRENT_TIMESTAMP
        WHERE id = ?
        """
        rows_affected = self.db.execute_update(query, (novo_status, observacoes, medida_id))
        return rows_affected > 0

class AcompanhamentoService:
    """Serviços relacionados aos acompanhamentos"""
    
    def __init__(self, db_manager: DatabaseManager):
        self.db = db_manager
    
    def registrar_visita(self, medida_id: int, dados_visita: Dict, usuario_id: int) -> int:
        """Registra uma nova visita de acompanhamento"""
        query = """
        INSERT INTO acompanhamentos 
        (medida_protetiva_id, data_visita, hora_visita, tipo_visita, local_visita,
         policial_responsavel, situacao_encontrada, cumprimento_medida, vitima_presente,
         agressor_localizado, novos_fatos, encaminhamentos, observacoes, usuario_registro)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """
        return self.db.execute_update(query, (
            medida_id, dados_visita['data_visita'], dados_visita.get('hora_visita'),
            dados_visita['tipo_visita'], dados_visita.get('local_visita'),
            dados_visita['policial_responsavel'], dados_visita['situacao_encontrada'],
            dados_visita['cumprimento_medida'], dados_visita.get('vitima_presente', 0),
            dados_visita.get('agressor_localizado', 0), dados_visita.get('novos_fatos'),
            dados_visita.get('encaminhamentos'), dados_visita.get('observacoes'), usuario_id
        ))
    
    def listar_acompanhamentos(self, medida_id: int) -> List[Dict]:
        """Lista todos os acompanhamentos de uma medida protetiva"""
        query = """
        SELECT a.*, m.numero_processo, v.nome_completo as vitima_nome
        FROM acompanhamentos a
        JOIN medidas_protetivas m ON a.medida_protetiva_id = m.id
        JOIN vitimas v ON m.id = v.medida_protetiva_id
        WHERE a.medida_protetiva_id = ?
        ORDER BY a.data_visita DESC, a.hora_visita DESC
        """
        return self.db.execute_query(query, (medida_id,))

class OcorrenciaService:
    """Serviços relacionados às ocorrências e descumprimentos"""
    
    def __init__(self, db_manager: DatabaseManager):
        self.db = db_manager
    
    def registrar_ocorrencia(self, medida_id: int, dados_ocorrencia: Dict, usuario_id: int) -> int:
        """Registra nova ocorrência de descumprimento"""
        query = """
        INSERT INTO ocorrencias 
        (medida_protetiva_id, data_ocorrencia, hora_ocorrencia, tipo_ocorrencia,
         descricao_detalhada, local_ocorrencia, boletim_ocorrencia, medidas_tomadas,
         gravidade, policial_responsavel, usuario_registro)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """
        return self.db.execute_update(query, (
            medida_id, dados_ocorrencia['data_ocorrencia'], dados_ocorrencia.get('hora_ocorrencia'),
            dados_ocorrencia['tipo_ocorrencia'], dados_ocorrencia['descricao_detalhada'],
            dados_ocorrencia.get('local_ocorrencia'), dados_ocorrencia.get('boletim_ocorrencia'),
            dados_ocorrencia.get('medidas_tomadas'), dados_ocorrencia['gravidade'],
            dados_ocorrencia['policial_responsavel'], usuario_id
        ))
    
    def listar_ocorrencias(self, medida_id: int = None, tipo: str = None) -> List[Dict]:
        """Lista ocorrências com filtros opcionais"""
        query = """
        SELECT o.*, m.numero_processo, v.nome_completo as vitima_nome
        FROM ocorrencias o
        JOIN medidas_protetivas m ON o.medida_protetiva_id = m.id
        JOIN vitimas v ON m.id = v.medida_protetiva_id
        """
        params = []
        conditions = []
        
        if medida_id:
            conditions.append("o.medida_protetiva_id = ?")
            params.append(medida_id)
        
        if tipo:
            conditions.append("o.tipo_ocorrencia = ?")
            params.append(tipo)
        
        if conditions:
            query += " WHERE " + " AND ".join(conditions)
        
        query += " ORDER BY o.data_ocorrencia DESC, o.hora_ocorrencia DESC"
        
        return self.db.execute_query(query, tuple(params))

class RelatorioService:
    """Serviços para geração de relatórios estatísticos"""
    
    def __init__(self, db_manager: DatabaseManager):
        self.db = db_manager
    
    def estatisticas_gerais(self) -> Dict:
        """Retorna estatísticas gerais do sistema"""
        stats = {}
        
        # Total de medidas por status
        query = "SELECT status, COUNT(*) as total FROM medidas_protetivas GROUP BY status"
        stats['por_status'] = self.db.execute_query(query)
        
        # Total de acompanhamentos no mês atual
        query = """
        SELECT COUNT(*) as total FROM acompanhamentos 
        WHERE strftime('%Y-%m', data_visita) = strftime('%Y-%m', 'now')
        """
        stats['acompanhamentos_mes'] = self.db.execute_query(query)[0]['total']
        
        # Total de ocorrências por tipo
        query = "SELECT tipo_ocorrencia, COUNT(*) as total FROM ocorrencias GROUP BY tipo_ocorrencia"
        stats['ocorrencias_por_tipo'] = self.db.execute_query(query)
        
        # Medidas com maior risco
        query = """
        SELECT m.numero_processo, v.nome_completo, r.nivel_risco
        FROM medidas_protetivas m
        JOIN vitimas v ON m.id = v.medida_protetiva_id
        JOIN avaliacoes_risco r ON m.id = r.medida_protetiva_id
        WHERE r.nivel_risco IN ('alto', 'extremo')
        ORDER BY r.data_avaliacao DESC
        """
        stats['medidas_alto_risco'] = self.db.execute_query(query)
        
        return stats
    
    def relatorio_periodo(self, data_inicio: str, data_fim: str) -> Dict:
        """Gera relatório de atividades por período"""
        relatorio = {}
        
        # Medidas concedidas no período
        query = """
        SELECT COUNT(*) as total FROM medidas_protetivas 
        WHERE data_concessao BETWEEN ? AND ?
        """
        relatorio['medidas_periodo'] = self.db.execute_query(query, (data_inicio, data_fim))[0]['total']
        
        # Acompanhamentos realizados
        query = """
        SELECT COUNT(*) as total FROM acompanhamentos 
        WHERE data_visita BETWEEN ? AND ?
        """
        relatorio['visitas_periodo'] = self.db.execute_query(query, (data_inicio, data_fim))[0]['total']
        
        # Ocorrências registradas
        query = """
        SELECT COUNT(*) as total FROM ocorrencias 
        WHERE data_ocorrencia BETWEEN ? AND ?
        """
        relatorio['ocorrencias_periodo'] = self.db.execute_query(query, (data_inicio, data_fim))[0]['total']
        
        return relatorio

# Exemplo de uso do sistema
def exemplo_uso():
    """Demonstra como usar as classes do sistema"""
    
    # Inicializar serviços
    db = DatabaseManager()
    usuario_service = UsuarioService(db)
    medida_service = MedidaProtetivaService(db)
    acompanhamento_service = AcompanhamentoService(db)
    ocorrencia_service = OcorrenciaService(db)
    relatorio_service = RelatorioService(db)
    
    # Validar login
    usuario = usuario_service.validar_login("30375237", "198022Pm")
    if usuario:
        print(f"Login realizado: {usuario['nome_completo']} - {usuario['perfil']}")
    
    # Listar medidas ativas
    medidas_ativas = medida_service.listar_medidas(status='ativa')
    print(f"\\nMedidas ativas: {len(medidas_ativas)}")
    
    # Buscar medida específica
    medida = medida_service.buscar_medida_por_processo("0001234-12.2024.8.05.0123")
    if medida:
        print(f"Medida encontrada: {medida['vitima_nome']} vs {medida['agressor_nome']}")
    
    # Estatísticas gerais
    stats = relatorio_service.estatisticas_gerais()
    print(f"\\nEstatísticas do sistema:")
    print(f"Acompanhamentos este mês: {stats['acompanhamentos_mes']}")
    
    return "Sistema funcionando corretamente!"

if __name__ == "__main__":
    exemplo_uso()
'''

# Salvar o arquivo Python
with open("database_manager.py", "w", encoding="utf-8") as file:
    file.write(python_db_code)

print("✓ Arquivo 'database_manager.py' criado com sucesso!")
print("\nClasses implementadas:")
print("- DatabaseManager: Gerenciamento geral do banco")
print("- UsuarioService: Autenticação e usuários")
print("- MedidaProtetivaService: CRUD de medidas protetivas")
print("- AcompanhamentoService: Visitas e monitoramento")
print("- OcorrenciaService: Descumprimentos e ocorrências")
print("- RelatorioService: Estatísticas e relatórios")

# Executar exemplo de uso
exec(python_db_code)
resultado = exemplo_uso()
print(f"\n{resultado}")