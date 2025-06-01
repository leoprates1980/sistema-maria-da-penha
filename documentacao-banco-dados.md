# Documentação do Banco de Dados - Sistema de Medidas Protetivas

## Visão Geral

Este documento descreve a estrutura completa do banco de dados SQLite desenvolvido para o Sistema de Acompanhamento de Medidas Protetivas da Ronda Maria da Penha - 29ª CIPM Seabra.

## Estrutura das Tabelas

### 1. usuarios
Armazena informações dos usuários do sistema.

| Campo | Tipo | Descrição |
|-------|------|-----------|
| id | INTEGER PRIMARY KEY | Identificador único do usuário |
| usuario | VARCHAR(50) | Nome de usuário para login (único) |
| senha | VARCHAR(255) | Senha do usuário |
| nome_completo | VARCHAR(150) | Nome completo do usuário |
| perfil | VARCHAR(20) | Perfil de acesso (administrador, coordenador, operador) |
| ativo | BOOLEAN | Status do usuário (ativo/inativo) |
| data_criacao | DATETIME | Data de criação do usuário |
| ultimo_acesso | DATETIME | Data do último acesso |

### 2. medidas_protetivas
Tabela principal com informações das medidas protetivas.

| Campo | Tipo | Descrição |
|-------|------|-----------|
| id | INTEGER PRIMARY KEY | Identificador único da medida |
| numero_processo | VARCHAR(50) | Número do processo judicial (único) |
| data_concessao | DATE | Data de concessão da medida |
| juiz_responsavel | VARCHAR(150) | Nome do juiz responsável |
| vara_competente | VARCHAR(100) | Vara judicial competente |
| comarca | VARCHAR(100) | Comarca onde foi concedida |
| status | VARCHAR(20) | Status atual (ativa, cumprida, descumprida, revogada, suspensa) |
| data_inicio_vigencia | DATE | Data de início da vigência |
| data_fim_vigencia | DATE | Data de fim da vigência |
| observacoes | TEXT | Observações gerais |
| usuario_cadastro | INTEGER | ID do usuário que cadastrou |
| data_cadastro | DATETIME | Data do cadastro |
| data_atualizacao | DATETIME | Data da última atualização |

### 3. vitimas
Dados pessoais das vítimas protegidas.

| Campo | Tipo | Descrição |
|-------|------|-----------|
| id | INTEGER PRIMARY KEY | Identificador único da vítima |
| medida_protetiva_id | INTEGER | ID da medida protetiva (FK) |
| nome_completo | VARCHAR(150) | Nome completo da vítima |
| nome_social | VARCHAR(150) | Nome social (opcional) |
| cpf | VARCHAR(14) | CPF da vítima |
| rg | VARCHAR(20) | RG da vítima |
| data_nascimento | DATE | Data de nascimento |
| telefone_principal | VARCHAR(20) | Telefone principal |
| telefone_secundario | VARCHAR(20) | Telefone secundário |
| email | VARCHAR(100) | E-mail |
| cep | VARCHAR(10) | CEP |
| logradouro | VARCHAR(200) | Endereço |
| numero | VARCHAR(10) | Número |
| complemento | VARCHAR(100) | Complemento |
| bairro | VARCHAR(100) | Bairro |
| cidade | VARCHAR(100) | Cidade |
| uf | VARCHAR(2) | Estado |
| escolaridade | VARCHAR(50) | Nível de escolaridade |
| profissao | VARCHAR(100) | Profissão |
| renda_individual | DECIMAL(10,2) | Renda individual |
| cor_raca | VARCHAR(30) | Cor/raça |
| orientacao_sexual | VARCHAR(30) | Orientação sexual |
| estado_civil | VARCHAR(30) | Estado civil |
| filhos | INTEGER | Número de filhos |
| tem_deficiencia | BOOLEAN | Possui deficiência |
| tipo_deficiencia | VARCHAR(100) | Tipo de deficiência |
| contato_emergencia_nome | VARCHAR(150) | Nome do contato de emergência |
| contato_emergencia_telefone | VARCHAR(20) | Telefone do contato de emergência |
| contato_emergencia_parentesco | VARCHAR(50) | Parentesco do contato |

### 4. agressores
Dados dos agressores sujeitos às medidas.

| Campo | Tipo | Descrição |
|-------|------|-----------|
| id | INTEGER PRIMARY KEY | Identificador único do agressor |
| medida_protetiva_id | INTEGER | ID da medida protetiva (FK) |
| nome_completo | VARCHAR(150) | Nome completo do agressor |
| cpf | VARCHAR(14) | CPF do agressor |
| rg | VARCHAR(20) | RG do agressor |
| data_nascimento | DATE | Data de nascimento |
| telefone | VARCHAR(20) | Telefone |
| email | VARCHAR(100) | E-mail |
| cep | VARCHAR(10) | CEP |
| logradouro | VARCHAR(200) | Endereço |
| numero | VARCHAR(10) | Número |
| complemento | VARCHAR(100) | Complemento |
| bairro | VARCHAR(100) | Bairro |
| cidade | VARCHAR(100) | Cidade |
| uf | VARCHAR(2) | Estado |
| profissao | VARCHAR(100) | Profissão |
| local_trabalho | VARCHAR(200) | Local de trabalho |
| telefone_trabalho | VARCHAR(20) | Telefone do trabalho |
| escolaridade | VARCHAR(50) | Nível de escolaridade |
| cor_raca | VARCHAR(30) | Cor/raça |
| tipo_relacionamento | VARCHAR(50) | Tipo de relacionamento com a vítima |
| tempo_relacionamento | INTEGER | Tempo de relacionamento (meses) |
| relacionamento_ativo | BOOLEAN | Relacionamento ainda ativo |
| historico_violencia | TEXT | Histórico de violência |
| uso_alcool_drogas | BOOLEAN | Faz uso de álcool/drogas |
| porte_arma | BOOLEAN | Possui porte de arma |
| profissao_risco | BOOLEAN | Profissão de risco (policial, militar, etc.) |
| antecedentes_criminais | BOOLEAN | Possui antecedentes criminais |

### 5. tipos_medidas
Catálogo dos tipos de medidas protetivas.

| Campo | Tipo | Descrição |
|-------|------|-----------|
| id | INTEGER PRIMARY KEY | Identificador único |
| codigo | VARCHAR(10) | Código da medida (único) |
| descricao | VARCHAR(200) | Descrição da medida |
| categoria | VARCHAR(50) | Categoria (obrigacao_agressor, protecao_vitima, assistencial) |
| ativo | BOOLEAN | Status ativo/inativo |

### 6. medidas_aplicadas
Relacionamento N:N entre medidas protetivas e tipos de medidas.

| Campo | Tipo | Descrição |
|-------|------|-----------|
| id | INTEGER PRIMARY KEY | Identificador único |
| medida_protetiva_id | INTEGER | ID da medida protetiva (FK) |
| tipo_medida_id | INTEGER | ID do tipo de medida (FK) |
| detalhes | TEXT | Detalhes específicos da aplicação |
| distancia_minima | INTEGER | Distância mínima em metros |
| data_aplicacao | DATE | Data de aplicação |
| ativo | BOOLEAN | Status ativo/inativo |

### 7. acompanhamentos
Registro das visitas de monitoramento.

| Campo | Tipo | Descrição |
|-------|------|-----------|
| id | INTEGER PRIMARY KEY | Identificador único |
| medida_protetiva_id | INTEGER | ID da medida protetiva (FK) |
| data_visita | DATE | Data da visita |
| hora_visita | TIME | Hora da visita |
| tipo_visita | VARCHAR(30) | Tipo (agendada, nao_agendada, emergencial) |
| local_visita | VARCHAR(200) | Local da visita |
| policial_responsavel | VARCHAR(150) | Policial responsável |
| situacao_encontrada | TEXT | Situação encontrada |
| cumprimento_medida | VARCHAR(20) | Status do cumprimento |
| vitima_presente | BOOLEAN | Vítima estava presente |
| agressor_localizado | BOOLEAN | Agressor foi localizado |
| novos_fatos | TEXT | Novos fatos relevantes |
| encaminhamentos | TEXT | Encaminhamentos realizados |
| observacoes | TEXT | Observações gerais |
| proximavisita_agendada | DATE | Próxima visita agendada |
| usuario_registro | INTEGER | Usuário que registrou (FK) |
| data_registro | DATETIME | Data do registro |

### 8. ocorrencias
Registro de ocorrências e descumprimentos.

| Campo | Tipo | Descrição |
|-------|------|-----------|
| id | INTEGER PRIMARY KEY | Identificador único |
| medida_protetiva_id | INTEGER | ID da medida protetiva (FK) |
| data_ocorrencia | DATE | Data da ocorrência |
| hora_ocorrencia | TIME | Hora da ocorrência |
| tipo_ocorrencia | VARCHAR(50) | Tipo (descumprimento, ameaca, agressao, aproximacao) |
| descricao_detalhada | TEXT | Descrição detalhada |
| local_ocorrencia | VARCHAR(200) | Local da ocorrência |
| testemunhas | TEXT | Testemunhas |
| boletim_ocorrencia | VARCHAR(50) | Número do boletim de ocorrência |
| medidas_tomadas | TEXT | Medidas tomadas |
| agressor_preso | BOOLEAN | Agressor foi preso |
| vitima_ferida | BOOLEAN | Vítima ficou ferida |
| gravidade | VARCHAR(20) | Gravidade (baixa, media, alta, extrema) |
| status_seguimento | VARCHAR(30) | Status do seguimento |
| policial_responsavel | VARCHAR(150) | Policial responsável |
| usuario_registro | INTEGER | Usuário que registrou (FK) |
| data_registro | DATETIME | Data do registro |

### 9. avaliacoes_risco
Avaliações de risco conforme Formulário Nacional.

| Campo | Tipo | Descrição |
|-------|------|-----------|
| id | INTEGER PRIMARY KEY | Identificador único |
| medida_protetiva_id | INTEGER | ID da medida protetiva (FK) |
| data_avaliacao | DATE | Data da avaliação |
| ameaca_morte | BOOLEAN | Houve ameaça de morte |
| agressor_possui_arma | BOOLEAN | Agressor possui arma |
| violencia_fisica_severa | BOOLEAN | Violência física severa |
| ameaca_arma | BOOLEAN | Ameaça com arma |
| tentativa_estrangulamento | BOOLEAN | Tentativa de estrangulamento |
| violencia_sexual | BOOLEAN | Violência sexual |
| uso_drogas_alcool | BOOLEAN | Agressor usa drogas/álcool |
| controle_economico | BOOLEAN | Controle econômico |
| isolamento_social | BOOLEAN | Isolamento social da vítima |
| ciumes_extremo | BOOLEAN | Ciúmes extremo |
| perseguicao_stalking | BOOLEAN | Perseguição/stalking |
| vitima_gravida | BOOLEAN | Vítima está grávida |
| filhos_menores | BOOLEAN | Há filhos menores envolvidos |
| separacao_recente | BOOLEAN | Separação recente |
| novo_relacionamento_vitima | BOOLEAN | Vítima tem novo relacionamento |
| pontuacao_total | INTEGER | Pontuação total da avaliação |
| nivel_risco | VARCHAR(20) | Nível de risco (baixo, medio, alto, extremo) |
| recomendacoes | TEXT | Recomendações |
| responsavel_avaliacao | VARCHAR(150) | Responsável pela avaliação |
| usuario_registro | INTEGER | Usuário que registrou (FK) |
| data_registro | DATETIME | Data do registro |

### 10. documentos
Armazenamento de documentos anexos.

| Campo | Tipo | Descrição |
|-------|------|-----------|
| id | INTEGER PRIMARY KEY | Identificador único |
| medida_protetiva_id | INTEGER | ID da medida protetiva (FK) |
| tipo_documento | VARCHAR(50) | Tipo do documento |
| nome_arquivo | VARCHAR(200) | Nome do arquivo |
| tamanho_arquivo | INTEGER | Tamanho em bytes |
| tipo_mime | VARCHAR(100) | Tipo MIME |
| conteudo_base64 | TEXT | Conteúdo em base64 |
| descricao | TEXT | Descrição do documento |
| data_upload | DATETIME | Data do upload |
| usuario_upload | INTEGER | Usuário que fez upload (FK) |

### 11. logs_sistema
Log de auditoria do sistema.

| Campo | Tipo | Descrição |
|-------|------|-----------|
| id | INTEGER PRIMARY KEY | Identificador único |
| usuario_id | INTEGER | ID do usuário (FK) |
| acao | VARCHAR(100) | Ação realizada |
| tabela_afetada | VARCHAR(50) | Tabela afetada |
| id_registro | INTEGER | ID do registro afetado |
| detalhes | TEXT | Detalhes da ação |
| ip_origem | VARCHAR(45) | IP de origem |
| data_hora | DATETIME | Data e hora da ação |

## Índices Criados

Para otimizar a performance das consultas, foram criados os seguintes índices:

- `idx_medidas_numero_processo`: Busca por número de processo
- `idx_medidas_status`: Filtro por status
- `idx_medidas_data_concessao`: Ordenação por data
- `idx_vitimas_cpf`: Busca por CPF da vítima
- `idx_vitimas_nome`: Busca por nome da vítima
- `idx_agressores_cpf`: Busca por CPF do agressor
- `idx_agressores_nome`: Busca por nome do agressor
- `idx_acompanhamentos_data`: Filtro por data de visita
- `idx_acompanhamentos_medida`: Acompanhamentos por medida
- `idx_ocorrencias_data`: Filtro por data de ocorrência
- `idx_ocorrencias_tipo`: Filtro por tipo de ocorrência
- `idx_ocorrencias_medida`: Ocorrências por medida

## Triggers de Auditoria

O sistema inclui triggers automáticos para:

1. **Atualização de timestamp**: Atualiza automaticamente `data_atualizacao` na tabela `medidas_protetivas`
2. **Log de inserções**: Registra automaticamente criação de novas medidas
3. **Log de atualizações**: Registra alterações em medidas existentes

## Dados Iniciais

O sistema é criado com dados iniciais essenciais:

- **Usuário administrador**: Credenciais conforme especificado (30375237/198022Pm)
- **Tipos de medidas**: 16 tipos padrão de medidas protetivas da Lei Maria da Penha
- **Dados de exemplo**: 3 medidas protetivas completas para demonstração

## Considerações de Segurança

1. **Senhas**: Devem ser armazenadas com hash SHA-256
2. **Logs**: Todas as operações críticas são registradas
3. **Constraints**: Campos únicos (CPF, número de processo) têm validação
4. **Foreign Keys**: Integridade referencial garantida entre tabelas

## Como Usar

Para utilizar o banco de dados:

1. Execute o script `create_database_medidas_protetivas.sql`
2. Utilize a classe `DatabaseManager` do arquivo `database_manager.py`
3. Autentique com as credenciais padrão ou crie novos usuários
4. Use os serviços específicos para cada funcionalidade

## Manutenção

Para manutenção regular do banco:

- Faça backup regular do arquivo `.db`
- Monitore o crescimento da tabela `logs_sistema`
- Execute VACUUM periodicamente para otimizar espaço
- Verifique integridade com PRAGMA integrity_check