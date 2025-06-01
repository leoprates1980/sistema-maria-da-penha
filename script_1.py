# Vou criar dados de exemplo para demonstrar o funcionamento do sistema
# e também um arquivo Python com funções para interagir com o banco

import sqlite3
from datetime import datetime, date, timedelta
import json

# Conectar ao banco criado
conn = sqlite3.connect("medidas_protetivas.db")
cursor = conn.cursor()

# Inserir dados de exemplo
dados_exemplo = """
-- ===================================
-- DADOS DE EXEMPLO PARA DEMONSTRAÇÃO
-- ===================================

-- Inserir mais usuários de exemplo
INSERT INTO usuarios (usuario, senha, nome_completo, perfil) VALUES 
('coord001', 'senha123', 'Sgt. João Silva Santos', 'coordenador'),
('oper001', 'senha123', 'Cb. Maria Costa Lima', 'operador'),
('oper002', 'senha123', 'Sd. Pedro Oliveira', 'operador');

-- Inserir medidas protetivas de exemplo
INSERT INTO medidas_protetivas (numero_processo, data_concessao, juiz_responsavel, vara_competente, comarca, status, data_inicio_vigencia, observacoes, usuario_cadastro) VALUES 
('0001234-12.2024.8.05.0123', '2024-03-15', 'Dra. Ana Paula Ferreira', '1ª Vara de Violência Doméstica', 'Seabra', 'ativa', '2024-03-15', 'Medida concedida em caráter de urgência', 1),
('0001235-45.2024.8.05.0123', '2024-04-02', 'Dr. Carlos Roberto Silva', '1ª Vara de Violência Doméstica', 'Seabra', 'ativa', '2024-04-02', 'Agressor com histórico de violência', 1),
('0001236-78.2024.8.05.0123', '2024-02-20', 'Dra. Fernanda Costa', '1ª Vara de Violência Doméstica', 'Seabra', 'descumprida', '2024-02-20', 'Descumprimento registrado em 15/04/2024', 1);

-- Inserir dados das vítimas
INSERT INTO vitimas (medida_protetiva_id, nome_completo, cpf, data_nascimento, telefone_principal, cep, logradouro, numero, bairro, cidade, uf, escolaridade, profissao, renda_individual, cor_raca, estado_civil, filhos, contato_emergencia_nome, contato_emergencia_telefone, contato_emergencia_parentesco) VALUES 
(1, 'Maria da Silva Santos', '123.456.789-01', '1985-07-20', '(75) 99999-1234', '46900-000', 'Rua das Flores', '123', 'Centro', 'Seabra', 'BA', 'Ensino Médio Completo', 'Comerciante', 1200.00, 'Parda', 'Solteira', 2, 'José Santos Silva', '(75) 99888-7654', 'Irmão'),
(2, 'Ana Costa Lima', '987.654.321-02', '1990-12-10', '(75) 98888-5678', '46900-000', 'Avenida Principal', '456', 'São José', 'Seabra', 'BA', 'Superior Completo', 'Professora', 2500.00, 'Branca', 'Divorciada', 1, 'Rosa Lima Costa', '(75) 97777-3210', 'Mãe'),
(3, 'Joana Pereira Oliveira', '456.789.123-03', '1982-05-30', '(75) 96666-9876', '46900-000', 'Rua da Esperança', '789', 'Centenário', 'Seabra', 'BA', 'Ensino Fundamental', 'Diarista', 600.00, 'Negra', 'União Estável', 3, 'Antônio Oliveira', '(75) 95555-1111', 'Pai');

-- Inserir dados dos agressores
INSERT INTO agressores (medida_protetiva_id, nome_completo, cpf, data_nascimento, telefone, profissao, tipo_relacionamento, tempo_relacionamento, relacionamento_ativo, uso_alcool_drogas, porte_arma, antecedentes_criminais) VALUES 
(1, 'Carlos Eduardo Santos', '111.222.333-44', '1980-03-10', '(75) 94444-8888', 'Mecânico', 'Ex-companheiro', 36, 0, 1, 0, 1),
(2, 'Roberto Silva Lima', '222.333.444-55', '1975-08-25', '(75) 93333-7777', 'Motorista', 'Ex-marido', 60, 0, 1, 0, 0),
(3, 'Fernando Oliveira Pereira', '333.444.555-66', '1978-11-15', '(75) 92222-6666', 'Desempregado', 'Companheiro', 24, 1, 1, 0, 1);

-- Inserir medidas aplicadas
INSERT INTO medidas_aplicadas (medida_protetiva_id, tipo_medida_id, detalhes, distancia_minima, data_aplicacao) VALUES 
(1, 1, 'Afastamento imediato do lar conjugal', NULL, '2024-03-15'),
(1, 2, 'Manter distância mínima da vítima e familiares', 300, '2024-03-15'),
(1, 3, 'Proibido qualquer contato por telefone, WhatsApp, redes sociais', NULL, '2024-03-15'),
(2, 2, 'Não aproximar-se da vítima', 500, '2024-04-02'),
(2, 3, 'Vedado contato por qualquer meio', NULL, '2024-04-02'),
(2, 7, 'Suspensão da posse de arma de fogo', NULL, '2024-04-02'),
(3, 1, 'Afastamento do lar', NULL, '2024-02-20'),
(3, 2, 'Distância mínima obrigatória', 200, '2024-02-20');

-- Inserir acompanhamentos
INSERT INTO acompanhamentos (medida_protetiva_id, data_visita, hora_visita, tipo_visita, policial_responsavel, situacao_encontrada, cumprimento_medida, vitima_presente, observacoes, usuario_registro) VALUES 
(1, '2024-03-20', '14:30', 'nao_agendada', 'Sgt. João Silva Santos', 'Vítima em casa, tranquila, não houve contato do agressor', 'cumprida', 1, 'Situação sob controle, vítima orientada', 2),
(1, '2024-04-10', '10:15', 'agendada', 'Cb. Maria Costa Lima', 'Vítima relatou tentativa de contato por WhatsApp', 'descumprida', 1, 'Orientada a salvar as mensagens como prova', 3),
(2, '2024-04-15', '16:00', 'nao_agendada', 'Sd. Pedro Oliveira', 'Agressor foi visto próximo ao local de trabalho da vítima', 'descumprida', 0, 'Testemunhas confirmaram a presença do agressor', 4),
(3, '2024-03-01', '09:00', 'agendada', 'Sgt. João Silva Santos', 'Agressor retornou ao lar conjugal', 'descumprida', 1, 'Vítima com medo, situação de risco', 2);

-- Inserir ocorrências
INSERT INTO ocorrencias (medida_protetiva_id, data_ocorrencia, hora_ocorrencia, tipo_ocorrencia, descricao_detalhada, local_ocorrencia, boletim_ocorrencia, medidas_tomadas, gravidade, status_seguimento, policial_responsavel, usuario_registro) VALUES 
(1, '2024-04-10', '22:30', 'descumprimento', 'Agressor enviou mensagens ameaçadoras via WhatsApp', 'Residência da vítima', 'BO-2024-001234', 'Orientação à vítima, registro de ocorrência', 'media', 'em_andamento', 'Cb. Maria Costa Lima', 3),
(2, '2024-04-15', '15:45', 'aproximacao', 'Agressor foi visto no local de trabalho da vítima', 'Escola Municipal José de Alencar', 'BO-2024-001235', 'Abordagem do agressor, advertência formal', 'alta', 'concluido', 'Sd. Pedro Oliveira', 4),
(3, '2024-02-25', '20:00', 'agressao', 'Agressor agrediu fisicamente a vítima após retornar ao lar', 'Residência do casal', 'BO-2024-001236', 'Prisão em flagrante do agressor', 'extrema', 'concluido', 'Sgt. João Silva Santos', 2);

-- Inserir avaliações de risco
INSERT INTO avaliacoes_risco (medida_protetiva_id, data_avaliacao, ameaca_morte, agressor_possui_arma, violencia_fisica_severa, uso_drogas_alcool, controle_economico, ciumes_extremo, separacao_recente, pontuacao_total, nivel_risco, recomendacoes, responsavel_avaliacao, usuario_registro) VALUES 
(1, '2024-03-15', 1, 0, 1, 1, 1, 1, 1, 6, 'alto', 'Monitoramento intensivo, encaminhamento para casa abrigo se necessário', 'Dra. Ana Paula Ferreira', 1),
(2, '2024-04-02', 0, 1, 0, 1, 0, 1, 1, 4, 'medio', 'Acompanhamento regular, atenção especial aos fins de semana', 'Dr. Carlos Roberto Silva', 1),
(3, '2024-02-20', 1, 0, 1, 1, 1, 1, 0, 5, 'alto', 'Risco elevado, considerar prisão preventiva do agressor', 'Dra. Fernanda Costa', 1);
"""

# Executar inserção dos dados de exemplo
cursor.executescript(dados_exemplo)
conn.commit()

print("✓ Dados de exemplo inseridos com sucesso!")

# Verificar os dados inseridos
cursor.execute("""
SELECT m.numero_processo, m.status, v.nome_completo as vitima, a.nome_completo as agressor
FROM medidas_protetivas m
JOIN vitimas v ON m.id = v.medida_protetiva_id
JOIN agressores a ON m.id = a.medida_protetiva_id
ORDER BY m.data_concessao DESC
""")

resultados = cursor.fetchall()
print(f"\nMedidas Protetivas Cadastradas ({len(resultados)}):")
print("-" * 80)
for processo, status, vitima, agressor in resultados:
    print(f"Processo: {processo}")
    print(f"Status: {status.upper()}")
    print(f"Vítima: {vitima}")
    print(f"Agressor: {agressor}")
    print("-" * 80)

conn.close()
print("\n✓ Verificação dos dados concluída!")