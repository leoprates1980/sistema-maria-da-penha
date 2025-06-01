// Sistema de Cadastro e Acompanhamento de Medidas Protetivas
// Ronda Maria da Penha - 29ª CIPM Seabra
// Cores Oficiais PMBA

class SistemaMediasProtetivas {
    constructor() {
        this.currentUser = null;
        this.currentSection = 'dashboard';
        this.medidas = this.loadMedidas();
        this.visitas = this.loadVisitas();
        this.ocorrencias = this.loadOcorrencias();
        
        // Cores oficiais PMBA para gráficos
        this.coresPMBA = {
            azulFerrete: '#003d6b',
            vermelhoCarmesin: '#c8102e', 
            amarelo: '#ffdc00',
            azulClaro: '#00aedb',
            branco: '#ffffff',
            cinza: '#8c8c8c'
        };
        
        this.init();
    }

    init() {
        // Ensure modal is hidden initially
        const modal = document.getElementById('editModal');
        if (modal) {
            modal.classList.add('hidden');
        }
        
        this.setupEventListeners();
        this.loadDadosExemplo();
        this.updateStats();
        this.setupMasks();
        this.populateSelects();
    }

    // Sistema de Login
    setupEventListeners() {
        // Login
        const loginForm = document.getElementById('loginForm');
        if (loginForm) {
            loginForm.addEventListener('submit', (e) => {
                e.preventDefault();
                this.handleLogin();
            });
        }

        // Logout
        const logoutBtn = document.getElementById('logoutBtn');
        if (logoutBtn) {
            logoutBtn.addEventListener('click', () => {
                this.logout();
            });
        }

        // Modal close
        const closeModalBtn = document.querySelector('.close-modal');
        if (closeModalBtn) {
            closeModalBtn.addEventListener('click', (e) => {
                e.preventDefault();
                this.fecharModal();
            });
        }

        // Navegação
        document.querySelectorAll('.nav-link').forEach(link => {
            link.addEventListener('click', (e) => {
                e.preventDefault();
                const section = e.target.dataset.section;
                this.showSection(section);
            });
        });

        // Tabs
        document.querySelectorAll('.tab-btn').forEach(btn => {
            btn.addEventListener('click', (e) => {
                this.showTab(e.target.dataset.tab);
            });
        });

        // Forms
        const cadastroForm = document.getElementById('cadastroForm');
        if (cadastroForm) {
            cadastroForm.addEventListener('submit', (e) => {
                e.preventDefault();
                this.salvarMedida();
            });
        }

        const acompanhamentoForm = document.getElementById('acompanhamentoForm');
        if (acompanhamentoForm) {
            acompanhamentoForm.addEventListener('submit', (e) => {
                e.preventDefault();
                this.salvarVisita();
            });
        }

        const ocorrenciaForm = document.getElementById('ocorrenciaForm');
        if (ocorrenciaForm) {
            ocorrenciaForm.addEventListener('submit', (e) => {
                e.preventDefault();
                this.salvarOcorrencia();
            });
        }

        // Filters
        const filtrarBtn = document.getElementById('filtrarBtn');
        if (filtrarBtn) {
            filtrarBtn.addEventListener('click', () => {
                this.filtrarMedidas();
            });
        }

        // Selects para acompanhamento
        const medidaAcompanhamento = document.getElementById('medidaAcompanhamento');
        if (medidaAcompanhamento) {
            medidaAcompanhamento.addEventListener('change', (e) => {
                this.showAcompanhamentoForm(e.target.value);
            });
        }

        const medidaOcorrencia = document.getElementById('medidaOcorrencia');
        if (medidaOcorrencia) {
            medidaOcorrencia.addEventListener('change', (e) => {
                this.showOcorrenciaForm(e.target.value);
            });
        }

        // Cancelar cadastro
        const cancelarCadastro = document.getElementById('cancelarCadastro');
        if (cancelarCadastro) {
            cancelarCadastro.addEventListener('click', () => {
                this.limparFormulario();
            });
        }
    }

    handleLogin() {
        const username = document.getElementById('username').value;
        const password = document.getElementById('password').value;
        const loginError = document.getElementById('loginError');

        if (username === '30375237' && password === '198022Pm') {
            this.currentUser = username;
            document.getElementById('currentUser').textContent = username;
            document.getElementById('loginScreen').classList.add('hidden');
            document.getElementById('mainApp').classList.remove('hidden');
            this.updateStats();
            setTimeout(() => {
                this.createChart();
            }, 100);
        } else {
            loginError.classList.remove('hidden');
            setTimeout(() => {
                loginError.classList.add('hidden');
            }, 3000);
        }
    }

    logout() {
        this.currentUser = null;
        document.getElementById('loginScreen').classList.remove('hidden');
        document.getElementById('mainApp').classList.add('hidden');
        document.getElementById('username').value = '';
        document.getElementById('password').value = '';
    }

    // Modal functions
    fecharModal() {
        const modal = document.getElementById('editModal');
        if (modal) {
            modal.classList.add('hidden');
        }
    }

    // Navegação
    showSection(sectionName) {
        // Update nav
        document.querySelectorAll('.nav-link').forEach(link => {
            link.classList.remove('active');
        });
        const activeLink = document.querySelector(`[data-section="${sectionName}"]`);
        if (activeLink) {
            activeLink.classList.add('active');
        }

        // Update content
        document.querySelectorAll('.content-section').forEach(section => {
            section.classList.remove('active');
        });
        const activeSection = document.getElementById(sectionName);
        if (activeSection) {
            activeSection.classList.add('active');
        }

        this.currentSection = sectionName;

        // Load specific section data
        if (sectionName === 'consulta') {
            this.loadMedidasList();
        } else if (sectionName === 'acompanhamento') {
            this.populateAcompanhamentoSelect();
        } else if (sectionName === 'ocorrencias') {
            this.populateOcorrenciaSelect();
        }
    }

    showTab(tabName) {
        const parentForm = document.querySelector('.tabs').closest('section');
        
        // Update tab buttons
        parentForm.querySelectorAll('.tab-btn').forEach(btn => {
            btn.classList.remove('active');
        });
        const activeTab = parentForm.querySelector(`[data-tab="${tabName}"]`);
        if (activeTab) {
            activeTab.classList.add('active');
        }

        // Update tab content
        parentForm.querySelectorAll('.tab-content').forEach(content => {
            content.classList.remove('active');
        });
        const activeContent = parentForm.querySelector(`#tab-${tabName}`);
        if (activeContent) {
            activeContent.classList.add('active');
        }
    }

    // Dados de exemplo
    loadDadosExemplo() {
        if (this.medidas.length === 0) {
            const exemploMedidas = [
                {
                    id: 1,
                    numero_processo: "0001234-56.2024.8.05.0001",
                    vitima_nome: "Maria Silva Santos",
                    vitima_cpf: "123.456.789-01",
                    vitima_telefone: "(75) 99999-1234",
                    vitima_endereco: "Rua das Flores, 123 - Centro - Seabra/BA",
                    agressor_nome: "João Santos Silva",
                    agressor_cpf: "987.654.321-09",
                    relacionamento: "Ex-companheiro",
                    data_concessao: "2024-11-15",
                    medidas: ["Afastamento do lar", "Proibição de aproximação da ofendida"],
                    status: "Ativa",
                    data_cadastro: new Date().toISOString()
                },
                {
                    id: 2,
                    numero_processo: "0001235-67.2024.8.05.0001",
                    vitima_nome: "Ana Costa Lima",
                    vitima_cpf: "111.222.333-44",
                    vitima_telefone: "(75) 98888-5678",
                    vitima_endereco: "Av. Principal, 456 - Bairro Novo - Seabra/BA",
                    agressor_nome: "Pedro Lima Costa",
                    agressor_cpf: "555.666.777-88",
                    relacionamento: "Marido",
                    data_concessao: "2024-11-20",
                    medidas: ["Proibição de contato por qualquer meio", "Suspensão da posse/porte de armas"],
                    status: "Ativa",
                    data_cadastro: new Date().toISOString()
                }
            ];

            this.medidas = exemploMedidas;
            this.saveMedidas();
        }
    }

    // Local Storage (removido conforme instruções)
    loadMedidas() {
        return [];
    }

    saveMedidas() {
        // Simulação de salvamento sem localStorage
        console.log('Medidas salvas:', this.medidas);
    }

    loadVisitas() {
        return [];
    }

    saveVisitas() {
        console.log('Visitas salvas:', this.visitas);
    }

    loadOcorrencias() {
        return [];
    }

    saveOcorrencias() {
        console.log('Ocorrências salvas:', this.ocorrencias);
    }

    // Dashboard
    updateStats() {
        const medidasAtivas = this.medidas.filter(m => m.status === 'Ativa').length;
        const descumprimentos = this.ocorrencias.filter(o => o.tipo_ocorrencia === 'Descumprimento').length;
        const visitasTotal = this.visitas.length;
        const totalMedidas = this.medidas.length;

        const medidasAtivasEl = document.getElementById('medidasAtivas');
        const descumprimentosEl = document.getElementById('descumprimentos');
        const visitasRealizadasEl = document.getElementById('visitasRealizadas');
        const totalMedidasEl = document.getElementById('totalMedidas');

        if (medidasAtivasEl) medidasAtivasEl.textContent = medidasAtivas;
        if (descumprimentosEl) descumprimentosEl.textContent = descumprimentos;
        if (visitasRealizadasEl) visitasRealizadasEl.textContent = visitasTotal;
        if (totalMedidasEl) totalMedidasEl.textContent = totalMedidas;
    }

    createChart() {
        const ctx = document.getElementById('statusChart');
        if (!ctx || !window.Chart) return;

        const statusCounts = {};
        this.medidas.forEach(medida => {
            statusCounts[medida.status] = (statusCounts[medida.status] || 0) + 1;
        });

        // Destroy existing chart if it exists
        if (this.chart) {
            this.chart.destroy();
        }

        // Cores PMBA para status específicos
        const statusColors = {
            'Ativa': this.coresPMBA.azulClaro,
            'Descumprida': this.coresPMBA.vermelhoCarmesin,
            'Suspensa': this.coresPMBA.amarelo,
            'Cumprida': this.coresPMBA.cinza,
            'Revogada': this.coresPMBA.azulFerrete
        };

        const labels = Object.keys(statusCounts);
        const colors = labels.map(label => statusColors[label] || this.coresPMBA.cinza);

        this.chart = new Chart(ctx, {
            type: 'doughnut',
            data: {
                labels: labels,
                datasets: [{
                    data: Object.values(statusCounts),
                    backgroundColor: colors,
                    borderColor: this.coresPMBA.branco,
                    borderWidth: 2
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                plugins: {
                    legend: {
                        position: 'bottom',
                        labels: {
                            color: this.coresPMBA.azulFerrete,
                            font: {
                                size: 12
                            }
                        }
                    }
                }
            }
        });
    }

    // Formulários
    populateSelects() {
        const tiposMedidas = [
            "Afastamento do lar",
            "Proibição de aproximação da ofendida",
            "Proibição de aproximação de familiares",
            "Suspensão da posse/porte de armas",
            "Proibição de contato por qualquer meio",
            "Restrição ou suspensão de visitas aos dependentes menores",
            "Prestação de alimentos provisionais"
        ];

        const container = document.getElementById('tiposMedidas');
        if (!container) return;

        container.innerHTML = '';

        tiposMedidas.forEach(tipo => {
            const div = document.createElement('div');
            div.className = 'checkbox-item';
            const safeId = tipo.replace(/\s+/g, '_').replace(/[^\w]/g, '');
            div.innerHTML = `
                <input type="checkbox" id="medida_${safeId}" name="tipos_medidas" value="${tipo}">
                <label for="medida_${safeId}">${tipo}</label>
            `;
            container.appendChild(div);
        });
    }

    salvarMedida() {
        const form = document.getElementById('cadastroForm');
        if (!form) return;

        const formData = new FormData(form);
        const data = Object.fromEntries(formData.entries());

        // Get checked medidas
        const medidasSelecionadas = Array.from(form.querySelectorAll('input[name="tipos_medidas"]:checked'))
            .map(input => input.value);

        if (medidasSelecionadas.length === 0) {
            alert('Selecione pelo menos um tipo de medida protetiva');
            return;
        }

        const novaMedida = {
            id: Date.now(),
            ...data,
            medidas: medidasSelecionadas,
            data_cadastro: new Date().toISOString()
        };

        this.medidas.push(novaMedida);
        this.saveMedidas();
        this.updateStats();
        this.limparFormulario();
        
        alert('Medida protetiva cadastrada com sucesso!');
        this.showSection('consulta');
    }

    limparFormulario() {
        const form = document.getElementById('cadastroForm');
        if (!form) return;

        form.reset();
        document.querySelectorAll('input[name="tipos_medidas"]:checked').forEach(input => {
            input.checked = false;
        });
    }

    // Consulta
    loadMedidasList() {
        const container = document.getElementById('listaMedidas');
        if (!container) return;

        container.innerHTML = '';

        if (this.medidas.length === 0) {
            container.innerHTML = '<p>Nenhuma medida protetiva cadastrada.</p>';
            return;
        }

        this.medidas.forEach(medida => {
            const div = document.createElement('div');
            div.className = 'medida-item';
            div.innerHTML = `
                <div class="medida-header">
                    <div class="medida-info">
                        <h4>${medida.vitima_nome}</h4>
                        <p><strong>Processo:</strong> ${medida.numero_processo}</p>
                        <p><strong>Data:</strong> ${this.formatDate(medida.data_concessao)}</p>
                    </div>
                    <div class="medida-status">
                        <span class="status status--${medida.status.toLowerCase()}">${medida.status}</span>
                        <div class="medida-actions">
                            <button class="btn btn--sm btn--outline" onclick="sistema.editarMedida(${medida.id})">Editar</button>
                        </div>
                    </div>
                </div>
                <div class="medida-details">
                    <div class="detail-item">
                        <span class="detail-label">Agressor:</span>
                        <span class="detail-value">${medida.agressor_nome}</span>
                    </div>
                    <div class="detail-item">
                        <span class="detail-label">Relacionamento:</span>
                        <span class="detail-value">${medida.relacionamento}</span>
                    </div>
                    <div class="detail-item">
                        <span class="detail-label">Telefone:</span>
                        <span class="detail-value">${medida.vitima_telefone || 'Não informado'}</span>
                    </div>
                    <div class="detail-item">
                        <span class="detail-label">Medidas:</span>
                        <span class="detail-value">${medida.medidas.join(', ')}</span>
                    </div>
                </div>
            `;
            container.appendChild(div);
        });
    }

    filtrarMedidas() {
        const nome = document.getElementById('filtroNome').value.toLowerCase();
        const status = document.getElementById('filtroStatus').value;

        let medidasFiltradas = this.medidas;

        if (nome) {
            medidasFiltradas = medidasFiltradas.filter(m => 
                m.vitima_nome.toLowerCase().includes(nome)
            );
        }

        if (status) {
            medidasFiltradas = medidasFiltradas.filter(m => m.status === status);
        }

        const container = document.getElementById('listaMedidas');
        if (!container) return;

        container.innerHTML = '';

        if (medidasFiltradas.length === 0) {
            container.innerHTML = '<p>Nenhuma medida encontrada com os filtros aplicados.</p>';
            return;
        }

        medidasFiltradas.forEach(medida => {
            const div = document.createElement('div');
            div.className = 'medida-item';
            div.innerHTML = `
                <div class="medida-header">
                    <div class="medida-info">
                        <h4>${medida.vitima_nome}</h4>
                        <p><strong>Processo:</strong> ${medida.numero_processo}</p>
                        <p><strong>Data:</strong> ${this.formatDate(medida.data_concessao)}</p>
                    </div>
                    <div class="medida-status">
                        <span class="status status--${medida.status.toLowerCase()}">${medida.status}</span>
                        <div class="medida-actions">
                            <button class="btn btn--sm btn--outline" onclick="sistema.editarMedida(${medida.id})">Editar</button>
                        </div>
                    </div>
                </div>
                <div class="medida-details">
                    <div class="detail-item">
                        <span class="detail-label">Agressor:</span>
                        <span class="detail-value">${medida.agressor_nome}</span>
                    </div>
                    <div class="detail-item">
                        <span class="detail-label">Relacionamento:</span>
                        <span class="detail-value">${medida.relacionamento}</span>
                    </div>
                    <div class="detail-item">
                        <span class="detail-label">Telefone:</span>
                        <span class="detail-value">${medida.vitima_telefone || 'Não informado'}</span>
                    </div>
                    <div class="detail-item">
                        <span class="detail-label">Medidas:</span>
                        <span class="detail-value">${medida.medidas.join(', ')}</span>
                    </div>
                </div>
            `;
            container.appendChild(div);
        });
    }

    // Acompanhamento
    populateAcompanhamentoSelect() {
        const select = document.getElementById('medidaAcompanhamento');
        if (!select) return;

        select.innerHTML = '<option value="">Selecione uma medida...</option>';

        this.medidas.forEach(medida => {
            const option = document.createElement('option');
            option.value = medida.id;
            option.textContent = `${medida.vitima_nome} - ${medida.numero_processo}`;
            select.appendChild(option);
        });
    }

    showAcompanhamentoForm(medidaId) {
        const form = document.getElementById('acompanhamentoForm');
        if (!form) return;

        if (medidaId) {
            form.classList.remove('hidden');
            this.loadHistoricoVisitas(medidaId);
        } else {
            form.classList.add('hidden');
            const historico = document.getElementById('historicoVisitas');
            if (historico) {
                historico.innerHTML = '';
            }
        }
    }

    salvarVisita() {
        const medidaId = document.getElementById('medidaAcompanhamento').value;
        const form = document.getElementById('acompanhamentoForm');
        if (!form || !medidaId) return;

        const formData = new FormData(form);
        const data = Object.fromEntries(formData.entries());

        const novaVisita = {
            id: Date.now(),
            medida_id: parseInt(medidaId),
            ...data,
            data_registro: new Date().toISOString()
        };

        this.visitas.push(novaVisita);
        this.saveVisitas();
        this.updateStats();
        
        form.reset();
        this.loadHistoricoVisitas(medidaId);
        
        alert('Visita registrada com sucesso!');
    }

    loadHistoricoVisitas(medidaId) {
        const visitasMedida = this.visitas.filter(v => v.medida_id == medidaId);
        const container = document.getElementById('historicoVisitas');
        if (!container) return;
        
        if (visitasMedida.length === 0) {
            container.innerHTML = '<p>Nenhuma visita registrada para esta medida.</p>';
            return;
        }

        container.innerHTML = '<h4>Histórico de Visitas</h4>';
        
        visitasMedida.forEach(visita => {
            const div = document.createElement('div');
            div.className = 'historico-item';
            div.innerHTML = `
                <div class="historico-header">
                    <span class="historico-date">${this.formatDate(visita.data_visita)}</span>
                    <span class="historico-type">${visita.tipo_visita}</span>
                </div>
                <div class="historico-content">
                    <p><strong>Situação:</strong> ${visita.situacao}</p>
                    ${visita.observacoes ? `<p><strong>Observações:</strong> ${visita.observacoes}</p>` : ''}
                </div>
            `;
            container.appendChild(div);
        });
    }

    // Ocorrências
    populateOcorrenciaSelect() {
        const select = document.getElementById('medidaOcorrencia');
        if (!select) return;

        select.innerHTML = '<option value="">Selecione uma medida...</option>';

        this.medidas.forEach(medida => {
            const option = document.createElement('option');
            option.value = medida.id;
            option.textContent = `${medida.vitima_nome} - ${medida.numero_processo}`;
            select.appendChild(option);
        });
    }

    showOcorrenciaForm(medidaId) {
        const form = document.getElementById('ocorrenciaForm');
        if (!form) return;

        if (medidaId) {
            form.classList.remove('hidden');
            this.loadHistoricoOcorrencias(medidaId);
        } else {
            form.classList.add('hidden');
            const historico = document.getElementById('historicoOcorrencias');
            if (historico) {
                historico.innerHTML = '';
            }
        }
    }

    salvarOcorrencia() {
        const medidaId = document.getElementById('medidaOcorrencia').value;
        const form = document.getElementById('ocorrenciaForm');
        if (!form || !medidaId) return;

        const formData = new FormData(form);
        const data = Object.fromEntries(formData.entries());

        const novaOcorrencia = {
            id: Date.now(),
            medida_id: parseInt(medidaId),
            ...data,
            data_registro: new Date().toISOString()
        };

        this.ocorrencias.push(novaOcorrencia);
        this.saveOcorrencias();
        this.updateStats();
        
        form.reset();
        this.loadHistoricoOcorrencias(medidaId);
        
        alert('Ocorrência registrada com sucesso!');
    }

    loadHistoricoOcorrencias(medidaId) {
        const ocorrenciasMedida = this.ocorrencias.filter(o => o.medida_id == medidaId);
        const container = document.getElementById('historicoOcorrencias');
        if (!container) return;
        
        if (ocorrenciasMedida.length === 0) {
            container.innerHTML = '<p>Nenhuma ocorrência registrada para esta medida.</p>';
            return;
        }

        container.innerHTML = '<h4>Histórico de Ocorrências</h4>';
        
        ocorrenciasMedida.forEach(ocorrencia => {
            const div = document.createElement('div');
            div.className = 'historico-item';
            div.innerHTML = `
                <div class="historico-header">
                    <span class="historico-date">${this.formatDate(ocorrencia.data_ocorrencia)}</span>
                    <span class="historico-type status status--error">${ocorrencia.tipo_ocorrencia}</span>
                </div>
                <div class="historico-content">
                    <p><strong>Descrição:</strong> ${ocorrencia.descricao}</p>
                    ${ocorrencia.acoes_tomadas ? `<p><strong>Ações Tomadas:</strong> ${ocorrencia.acoes_tomadas}</p>` : ''}
                </div>
            `;
            container.appendChild(div);
        });
    }

    // Máscaras de entrada
    setupMasks() {
        // CPF mask
        document.querySelectorAll('.cpf-mask').forEach(input => {
            input.addEventListener('input', (e) => {
                let value = e.target.value.replace(/\D/g, '');
                value = value.replace(/(\d{3})(\d)/, '$1.$2');
                value = value.replace(/(\d{3})(\d)/, '$1.$2');
                value = value.replace(/(\d{3})(\d{1,2})$/, '$1-$2');
                e.target.value = value;
            });
        });

        // Phone mask
        document.querySelectorAll('.phone-mask').forEach(input => {
            input.addEventListener('input', (e) => {
                let value = e.target.value.replace(/\D/g, '');
                value = value.replace(/(\d{2})(\d)/, '($1) $2');
                value = value.replace(/(\d{5})(\d)/, '$1-$2');
                e.target.value = value;
            });
        });
    }

    // Utilities
    formatDate(dateString) {
        if (!dateString) return 'N/A';
        try {
            const date = new Date(dateString);
            return date.toLocaleDateString('pt-BR');
        } catch (e) {
            return dateString;
        }
    }

    editarMedida(id) {
        const medida = this.medidas.find(m => m.id === id);
        if (!medida) return;

        // Simplified edit - just change status for demo
        const novoStatus = prompt('Novo status (Ativa, Cumprida, Descumprida, Revogada, Suspensa):', medida.status);
        if (novoStatus && ['Ativa', 'Cumprida', 'Descumprida', 'Revogada', 'Suspensa'].includes(novoStatus)) {
            medida.status = novoStatus;
            this.saveMedidas();
            this.updateStats();
            this.loadMedidasList();
            // Atualizar gráfico também
            if (this.currentSection === 'dashboard') {
                this.createChart();
            }
        }
    }
}

// Relatórios
function gerarRelatorioGeral() {
    if (!sistema) return;
    
    const container = document.getElementById('relatorioContent');
    if (!container) return;

    const medidas = sistema.medidas;
    const visitas = sistema.visitas;
    const ocorrencias = sistema.ocorrencias;

    const statusCounts = {};
    medidas.forEach(medida => {
        statusCounts[medida.status] = (statusCounts[medida.status] || 0) + 1;
    });

    const html = `
        <h3>Relatório Geral do Sistema</h3>
        <div class="dashboard-stats">
            <div class="stat-card">
                <h4>Total de Medidas</h4>
                <div class="stat-number">${medidas.length}</div>
            </div>
            <div class="stat-card">
                <h4>Visitas Realizadas</h4>
                <div class="stat-number">${visitas.length}</div>
            </div>
            <div class="stat-card">
                <h4>Ocorrências</h4>
                <div class="stat-number">${ocorrencias.length}</div>
            </div>
        </div>
        <h4>Distribuição por Status</h4>
        <table style="width: 100%; border-collapse: collapse; margin-top: 16px; border: 1px solid #003d6b;">
            <thead>
                <tr style="background: #003d6b; color: white;">
                    <th style="padding: 12px; border: 1px solid #003d6b;">Status</th>
                    <th style="padding: 12px; border: 1px solid #003d6b;">Quantidade</th>
                </tr>
            </thead>
            <tbody>
                ${Object.entries(statusCounts).map(([status, count]) => `
                    <tr>
                        <td style="padding: 12px; border: 1px solid #003d6b;">${status}</td>
                        <td style="padding: 12px; border: 1px solid #003d6b; text-align: center;">${count}</td>
                    </tr>
                `).join('')}
            </tbody>
        </table>
    `;

    container.innerHTML = html;
}

function gerarRelatorioPeriodo() {
    if (!sistema) return;

    const dataInicio = document.getElementById('dataInicio').value;
    const dataFim = document.getElementById('dataFim').value;
    const container = document.getElementById('relatorioContent');

    if (!container) return;

    if (!dataInicio || !dataFim) {
        alert('Selecione as datas de início e fim');
        return;
    }

    const medidasPeriodo = sistema.medidas.filter(medida => {
        const dataMedida = new Date(medida.data_concessao);
        const inicio = new Date(dataInicio);
        const fim = new Date(dataFim);
        return dataMedida >= inicio && dataMedida <= fim;
    });

    const html = `
        <h3>Relatório do Período: ${sistema.formatDate(dataInicio)} a ${sistema.formatDate(dataFim)}</h3>
        <p><strong>Total de medidas no período:</strong> ${medidasPeriodo.length}</p>
        <table style="width: 100%; border-collapse: collapse; margin-top: 16px; border: 1px solid #003d6b;">
            <thead>
                <tr style="background: #003d6b; color: white;">
                    <th style="padding: 12px; border: 1px solid #003d6b;">Data</th>
                    <th style="padding: 12px; border: 1px solid #003d6b;">Vítima</th>
                    <th style="padding: 12px; border: 1px solid #003d6b;">Processo</th>
                    <th style="padding: 12px; border: 1px solid #003d6b;">Status</th>
                </tr>
            </thead>
            <tbody>
                ${medidasPeriodo.map(medida => `
                    <tr>
                        <td style="padding: 12px; border: 1px solid #003d6b;">${sistema.formatDate(medida.data_concessao)}</td>
                        <td style="padding: 12px; border: 1px solid #003d6b;">${medida.vitima_nome}</td>
                        <td style="padding: 12px; border: 1px solid #003d6b;">${medida.numero_processo}</td>
                        <td style="padding: 12px; border: 1px solid #003d6b;">${medida.status}</td>
                    </tr>
                `).join('')}
            </tbody>
        </table>
    `;

    container.innerHTML = html;
}

// Global functions
function fecharModal() {
    if (sistema) {
        sistema.fecharModal();
    }
}

// Initialize system
let sistema;
document.addEventListener('DOMContentLoaded', () => {
    sistema = new SistemaMediasProtetivas();
});