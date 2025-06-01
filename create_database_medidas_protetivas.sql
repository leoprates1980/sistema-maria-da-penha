
-- ===================================
-- BANCO DE DADOS PARA SISTEMA DE MEDIDAS PROTETIVAS
-- RONDA MARIA DA PENHA - 29ª CIPM SEABRA
-- ===================================

-- Tabela de usuários do sistema
CREATE TABLE usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    usuario VARCHAR(50) UNIQUE NOT NULL,
    senha VARCHAR(255) NOT NULL,
    nome_completo VARCHAR(150) NOT NULL,
    perfil VARCHAR(20) NOT NULL DEFAULT 'operador', -- administrador, coordenador, operador
    ativo BOOLEAN DEFAULT 1,
    data_criacao DATETIME DEFAULT CURRENT_TIMESTAMP,
    ultimo_acesso DATETIME
);

-- Tabela principal de medidas protetivas
CREATE TABLE medidas_protetivas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    numero_processo VARCHAR(50) UNIQUE NOT NULL,
    data_concessao DATE NOT NULL,
    juiz_responsavel VARCHAR(150),
    vara_competente VARCHAR(100),
    comarca VARCHAR(100),
    status VARCHAR(20) DEFAULT 'ativa', -- ativa, cumprida, descumprida, revogada, suspensa
    data_inicio_vigencia DATE,
    data_fim_vigencia DATE,
    observacoes TEXT,
    usuario_cadastro INTEGER,
    data_cadastro DATETIME DEFAULT CURRENT_TIMESTAMP,
    data_atualizacao DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (usuario_cadastro) REFERENCES usuarios(id)
);

-- Tabela de dados das vítimas
CREATE TABLE vitimas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    medida_protetiva_id INTEGER NOT NULL,
    nome_completo VARCHAR(150) NOT NULL,
    nome_social VARCHAR(150),
    cpf VARCHAR(14) UNIQUE,
    rg VARCHAR(20),
    data_nascimento DATE,
    telefone_principal VARCHAR(20),
    telefone_secundario VARCHAR(20),
    email VARCHAR(100),
    -- Endereço
    cep VARCHAR(10),
    logradouro VARCHAR(200),
    numero VARCHAR(10),
    complemento VARCHAR(100),
    bairro VARCHAR(100),
    cidade VARCHAR(100),
    uf VARCHAR(2),
    -- Dados socioeconômicos
    escolaridade VARCHAR(50),
    profissao VARCHAR(100),
    renda_individual DECIMAL(10,2),
    cor_raca VARCHAR(30),
    orientacao_sexual VARCHAR(30),
    estado_civil VARCHAR(30),
    filhos INTEGER DEFAULT 0,
    tem_deficiencia BOOLEAN DEFAULT 0,
    tipo_deficiencia VARCHAR(100),
    -- Contatos de emergência
    contato_emergencia_nome VARCHAR(150),
    contato_emergencia_telefone VARCHAR(20),
    contato_emergencia_parentesco VARCHAR(50),
    data_cadastro DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (medida_protetiva_id) REFERENCES medidas_protetivas(id) ON DELETE CASCADE
);

-- Tabela de dados dos agressores
CREATE TABLE agressores (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    medida_protetiva_id INTEGER NOT NULL,
    nome_completo VARCHAR(150) NOT NULL,
    cpf VARCHAR(14),
    rg VARCHAR(20),
    data_nascimento DATE,
    telefone VARCHAR(20),
    email VARCHAR(100),
    -- Endereço
    cep VARCHAR(10),
    logradouro VARCHAR(200),
    numero VARCHAR(10),
    complemento VARCHAR(100),
    bairro VARCHAR(100),
    cidade VARCHAR(100),
    uf VARCHAR(2),
    -- Dados adicionais
    profissao VARCHAR(100),
    local_trabalho VARCHAR(200),
    telefone_trabalho VARCHAR(20),
    escolaridade VARCHAR(50),
    cor_raca VARCHAR(30),
    -- Relacionamento com a vítima
    tipo_relacionamento VARCHAR(50), -- ex-companheiro, marido, namorado, etc.
    tempo_relacionamento INTEGER, -- em meses
    relacionamento_ativo BOOLEAN DEFAULT 0,
    historico_violencia TEXT,
    uso_alcool_drogas BOOLEAN DEFAULT 0,
    porte_arma BOOLEAN DEFAULT 0,
    profissao_risco BOOLEAN DEFAULT 0, -- policial, militar, segurança
    antecedentes_criminais BOOLEAN DEFAULT 0,
    data_cadastro DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (medida_protetiva_id) REFERENCES medidas_protetivas(id) ON DELETE CASCADE
);

-- Tabela de tipos de medidas protetivas
CREATE TABLE tipos_medidas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    codigo VARCHAR(10) UNIQUE NOT NULL,
    descricao VARCHAR(200) NOT NULL,
    categoria VARCHAR(50), -- obrigacao_agressor, protecao_vitima, assistencial
    ativo BOOLEAN DEFAULT 1
);

-- Tabela de medidas específicas aplicadas (relacionamento N:N)
CREATE TABLE medidas_aplicadas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    medida_protetiva_id INTEGER NOT NULL,
    tipo_medida_id INTEGER NOT NULL,
    detalhes TEXT,
    distancia_minima INTEGER, -- em metros, para medidas de afastamento
    data_aplicacao DATE,
    ativo BOOLEAN DEFAULT 1,
    FOREIGN KEY (medida_protetiva_id) REFERENCES medidas_protetivas(id) ON DELETE CASCADE,
    FOREIGN KEY (tipo_medida_id) REFERENCES tipos_medidas(id)
);

-- Tabela de acompanhamentos/visitas
CREATE TABLE acompanhamentos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    medida_protetiva_id INTEGER NOT NULL,
    data_visita DATE NOT NULL,
    hora_visita TIME,
    tipo_visita VARCHAR(30), -- agendada, nao_agendada, emergencial
    local_visita VARCHAR(200),
    policial_responsavel VARCHAR(150),
    situacao_encontrada TEXT,
    cumprimento_medida VARCHAR(20), -- cumprida, descumprida, parcial
    vitima_presente BOOLEAN DEFAULT 0,
    agressor_localizado BOOLEAN DEFAULT 0,
    novos_fatos TEXT,
    encaminhamentos TEXT,
    observacoes TEXT,
    proximavisita_agendada DATE,
    usuario_registro INTEGER,
    data_registro DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (medida_protetiva_id) REFERENCES medidas_protetivas(id) ON DELETE CASCADE,
    FOREIGN KEY (usuario_registro) REFERENCES usuarios(id)
);

-- Tabela de ocorrências e descumprimentos
CREATE TABLE ocorrencias (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    medida_protetiva_id INTEGER NOT NULL,
    data_ocorrencia DATE NOT NULL,
    hora_ocorrencia TIME,
    tipo_ocorrencia VARCHAR(50), -- descumprimento, ameaca, agressao, aproximacao
    descricao_detalhada TEXT NOT NULL,
    local_ocorrencia VARCHAR(200),
    testemunhas TEXT,
    boletim_ocorrencia VARCHAR(50), -- número do BO se houver
    medidas_tomadas TEXT,
    agressor_preso BOOLEAN DEFAULT 0,
    vitima_ferida BOOLEAN DEFAULT 0,
    gravidade VARCHAR(20), -- baixa, media, alta, extrema
    status_seguimento VARCHAR(30), -- pendente, em_andamento, concluido
    policial_responsavel VARCHAR(150),
    usuario_registro INTEGER,
    data_registro DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (medida_protetiva_id) REFERENCES medidas_protetivas(id) ON DELETE CASCADE,
    FOREIGN KEY (usuario_registro) REFERENCES usuarios(id)
);

-- Tabela de avaliação de risco (Formulário Nacional)
CREATE TABLE avaliacoes_risco (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    medida_protetiva_id INTEGER NOT NULL,
    data_avaliacao DATE NOT NULL,
    -- Fatores de risco conforme formulário nacional
    ameaca_morte BOOLEAN DEFAULT 0,
    agressor_possui_arma BOOLEAN DEFAULT 0,
    violencia_fisica_severa BOOLEAN DEFAULT 0,
    ameaca_arma BOOLEAN DEFAULT 0,
    tentativa_estrangulamento BOOLEAN DEFAULT 0,
    violencia_sexual BOOLEAN DEFAULT 0,
    uso_drogas_alcool BOOLEAN DEFAULT 0,
    controle_economico BOOLEAN DEFAULT 0,
    isolamento_social BOOLEAN DEFAULT 0,
    ciumes_extremo BOOLEAN DEFAULT 0,
    perseguicao_stalking BOOLEAN DEFAULT 0,
    vitima_gravida BOOLEAN DEFAULT 0,
    filhos_menores BOOLEAN DEFAULT 0,
    separacao_recente BOOLEAN DEFAULT 0,
    novo_relacionamento_vitima BOOLEAN DEFAULT 0,
    -- Pontuação e classificação
    pontuacao_total INTEGER DEFAULT 0,
    nivel_risco VARCHAR(20), -- baixo, medio, alto, extremo
    recomendacoes TEXT,
    responsavel_avaliacao VARCHAR(150),
    usuario_registro INTEGER,
    data_registro DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (medida_protetiva_id) REFERENCES medidas_protetivas(id) ON DELETE CASCADE,
    FOREIGN KEY (usuario_registro) REFERENCES usuarios(id)
);

-- Tabela de documentos anexos
CREATE TABLE documentos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    medida_protetiva_id INTEGER NOT NULL,
    tipo_documento VARCHAR(50), -- decisao_judicial, boletim_ocorrencia, relatorio_medico, etc.
    nome_arquivo VARCHAR(200),
    tamanho_arquivo INTEGER,
    tipo_mime VARCHAR(100),
    conteudo_base64 TEXT, -- para armazenar o arquivo como base64
    descricao TEXT,
    data_upload DATETIME DEFAULT CURRENT_TIMESTAMP,
    usuario_upload INTEGER,
    FOREIGN KEY (medida_protetiva_id) REFERENCES medidas_protetivas(id) ON DELETE CASCADE,
    FOREIGN KEY (usuario_upload) REFERENCES usuarios(id)
);

-- Tabela de logs do sistema
CREATE TABLE logs_sistema (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    usuario_id INTEGER,
    acao VARCHAR(100), -- login, cadastro, consulta, alteracao, exclusao
    tabela_afetada VARCHAR(50),
    id_registro INTEGER,
    detalhes TEXT,
    ip_origem VARCHAR(45),
    data_hora DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (usuario_id) REFERENCES usuarios(id)
);

-- ===================================
-- INSERÇÃO DE DADOS INICIAIS
-- ===================================

-- Inserir usuário padrão (credenciais conforme solicitado)
INSERT INTO usuarios (usuario, senha, nome_completo, perfil) 
VALUES ('30375237', '198022Pm', 'Administrador do Sistema', 'administrador');

-- Inserir tipos de medidas protetivas padrão
INSERT INTO tipos_medidas (codigo, descricao, categoria) VALUES 
('MP001', 'Afastamento do lar, domicílio ou local de convivência com a ofendida', 'obrigacao_agressor'),
('MP002', 'Proibição de aproximação da ofendida, familiares e testemunhas', 'obrigacao_agressor'),
('MP003', 'Proibição de contato com a ofendida, familiares e testemunhas por qualquer meio', 'obrigacao_agressor'),
('MP004', 'Proibição de frequentação de determinados lugares', 'obrigacao_agressor'),
('MP005', 'Restrição ou suspensão de visitas aos dependentes menores', 'obrigacao_agressor'),
('MP006', 'Prestação de alimentos provisionais ou definitivos', 'obrigacao_agressor'),
('MP007', 'Suspensão da posse ou restrição do porte de armas', 'obrigacao_agressor'),
('MP008', 'Recondução da ofendida e dependentes ao respectivo domicílio', 'protecao_vitima'),
('MP009', 'Afastamento da ofendida do lar, sem prejuízo dos direitos', 'protecao_vitima'),
('MP010', 'Separação de corpos', 'protecao_vitima'),
('MP011', 'Restituição de bens subtraídos pelo agressor', 'protecao_vitima'),
('MP012', 'Proibição temporária para celebração de atos e contratos', 'protecao_vitima'),
('MP013', 'Suspensão das procurações conferidas pela ofendida ao agressor', 'protecao_vitima'),
('MP014', 'Prestação de caução provisória por perdas e danos', 'protecao_vitima'),
('MP015', 'Encaminhamento da ofendida e dependentes a programa oficial de proteção', 'assistencial'),
('MP016', 'Determinação para recondução de bens da sociedade conjugal', 'assistencial');

-- ===================================
-- CRIAÇÃO DE ÍNDICES PARA PERFORMANCE
-- ===================================

-- Índices para melhorar performance das consultas
CREATE INDEX idx_medidas_numero_processo ON medidas_protetivas(numero_processo);
CREATE INDEX idx_medidas_status ON medidas_protetivas(status);
CREATE INDEX idx_medidas_data_concessao ON medidas_protetivas(data_concessao);

CREATE INDEX idx_vitimas_cpf ON vitimas(cpf);
CREATE INDEX idx_vitimas_nome ON vitimas(nome_completo);

CREATE INDEX idx_agressores_cpf ON agressores(cpf);
CREATE INDEX idx_agressores_nome ON agressores(nome_completo);

CREATE INDEX idx_acompanhamentos_data ON acompanhamentos(data_visita);
CREATE INDEX idx_acompanhamentos_medida ON acompanhamentos(medida_protetiva_id);

CREATE INDEX idx_ocorrencias_data ON ocorrencias(data_ocorrencia);
CREATE INDEX idx_ocorrencias_tipo ON ocorrencias(tipo_ocorrencia);
CREATE INDEX idx_ocorrencias_medida ON ocorrencias(medida_protetiva_id);

-- ===================================
-- TRIGGERS PARA AUDITORIA
-- ===================================

-- Trigger para atualizar data_atualizacao em medidas_protetivas
CREATE TRIGGER trigger_medidas_update 
AFTER UPDATE ON medidas_protetivas
FOR EACH ROW
BEGIN
    UPDATE medidas_protetivas 
    SET data_atualizacao = CURRENT_TIMESTAMP 
    WHERE id = NEW.id;
END;

-- Trigger para registrar logs de alterações
CREATE TRIGGER trigger_log_medidas_insert
AFTER INSERT ON medidas_protetivas
FOR EACH ROW
BEGIN
    INSERT INTO logs_sistema (acao, tabela_afetada, id_registro, detalhes)
    VALUES ('INSERT', 'medidas_protetivas', NEW.id, 'Nova medida protetiva cadastrada: ' || NEW.numero_processo);
END;

CREATE TRIGGER trigger_log_medidas_update
AFTER UPDATE ON medidas_protetivas
FOR EACH ROW
BEGIN
    INSERT INTO logs_sistema (acao, tabela_afetada, id_registro, detalhes)
    VALUES ('UPDATE', 'medidas_protetivas', NEW.id, 'Medida protetiva alterada: ' || NEW.numero_processo);
END;
