# 🚨 GUIA SUPER FÁCIL: Como Juntar Tudo do Sistema da Ronda Maria da Penha

## 🎯 O que você tem agora?

Nós criamos várias "peças" do seu sistema como um quebra-cabeças. Agora vamos ensinar como juntar tudo!

### 📦 As "peças" que temos:
1. **Aplicação Web** (as páginas que aparecem na tela)
2. **Banco de Dados** (onde ficam guardadas as informações)
3. **Cores da PMBA** (para ficar bonito igual ao site oficial)

---

## 📋 PASSO 1: Criando a Pasta do Sistema

### 🔧 O que fazer:
1. No seu computador, crie uma pasta nova
2. Dê o nome: `Sistema-Maria-da-Penha`
3. Abra essa pasta

**📝 Dica:** É como criar uma gaveta nova para guardar tudo organizado!

---

## 📋 PASSO 2: Colocando os Arquivos da Aplicação Web

### 🔧 O que fazer:
1. Dentro da pasta `Sistema-Maria-da-Penha`, coloque estes 3 arquivos:
   - `index.html` (a página principal)
   - `style.css` (as cores e o visual)
   - `app.js` (o cérebro do sistema)

### 🎨 **IMPORTANTE - Cores da PMBA:**
No arquivo `style.css`, as cores já estão certinhas:
- **Azul da PMBA:** `#003d6b` (Azul Ferrete Pantone 281)
- **Vermelho da PMBA:** `#c8102e` (Vermelho Carmesim Pantone 200)
- **Amarelo da PMBA:** `#ffdc00` (Amarelo Pantone 116)

**📝 Dica:** É como pintar a casa com as cores certas da Polícia!

---

## 📋 PASSO 3: Colocando o Banco de Dados

### 🔧 O que fazer:
1. Na mesma pasta, coloque estes arquivos do banco:
   - `medidas_protetivas.db` (o banco pronto para usar)
   - `create_database_medidas_protetivas.sql` (para criar banco novo se precisar)
   - `database_manager.py` (para conversar com o banco)

### 🔑 **LOGIN JÁ CONFIGURADO:**
- **Usuário:** `30375237`
- **Senha:** `198022Pm`

**📝 Dica:** É como ter a chave da porta já cortada e pronta!

---

## 📋 PASSO 4: Testando se Funciona

### 🔧 O que fazer:
1. Clique duas vezes no arquivo `index.html`
2. Vai abrir no seu navegador (Chrome, Firefox, etc.)
3. Digite o usuário e senha
4. Se entrar, está funcionando! 🎉

### 🚨 **Se der erro:**
- Verifique se todos os arquivos estão na mesma pasta
- Tente abrir com outro navegador
- Veja se não tem erro de digitação no usuário/senha

---

## 📋 PASSO 5: Como Usar o Sistema

### 🎯 **Menu Principal:**
1. **Dashboard** - Ver estatísticas
2. **Cadastrar Medida** - Adicionar nova medida protetiva
3. **Consultar Medidas** - Buscar medidas existentes
4. **Acompanhamentos** - Registrar visitas
5. **Ocorrências** - Anotar problemas
6. **Relatórios** - Ver resumos

### 📝 **Para cadastrar uma medida nova:**
1. Clique em "Cadastrar Medida"
2. Preencha as abas: Vítima → Agressor → Processo → Medidas
3. Clique em "Salvar"

**📝 Dica:** É como preencher uma ficha médica, mas da Polícia!

---

## 🔧 OPÇÕES AVANÇADAS (se quiser mexer mais)

### 💾 **Se quiser usar com Python (mais avançado):**
1. Instale o Python no computador
2. Use o arquivo `database_manager.py`
3. Pode fazer relatórios mais complexos

### 📊 **Se quiser mais gráficos:**
- O sistema já tem gráficos básicos
- Para melhorar, pode mexer no arquivo `app.js`

---

## 🆘 PROBLEMAS COMUNS E SOLUÇÕES

### ❌ **"Página não carrega"**
✅ **Solução:** Verifique se o arquivo `index.html` está na pasta certa

### ❌ **"Login não funciona"**
✅ **Solução:** 
- Usuário: `30375237` (só números)
- Senha: `198022Pm` (com maiúscula no P)

### ❌ **"Dados não salvam"**
✅ **Solução:** 
- Os dados ficam no navegador
- Para salvar permanente, use o banco SQLite

### ❌ **"Cores estão erradas"**
✅ **Solução:** 
- Abra o arquivo `style.css`
- Procure por `--color-primary: #003d6b`
- Esse é o azul da PMBA

---

## 📁 ESTRUTURA FINAL DA PASTA

```
Sistema-Maria-da-Penha/
├── index.html              ← Página principal
├── style.css               ← Visual e cores da PMBA
├── app.js                  ← Funcionalidades
├── medidas_protetivas.db   ← Banco de dados
├── create_database_medidas_protetivas.sql
├── database_manager.py
└── documentacao-banco-dados.md
```

**📝 Dica:** É como ter uma pasta de trabalho com tudo organizado!

---

## 🎉 PRONTO! SISTEMA FUNCIONANDO!

### ✅ **O que você consegue fazer agora:**
- ✅ Fazer login no sistema
- ✅ Cadastrar medidas protetivas
- ✅ Consultar medidas existentes
- ✅ Registrar visitas de acompanhamento
- ✅ Anotar ocorrências e descumprimentos
- ✅ Gerar relatórios
- ✅ Ver estatísticas no dashboard

### 🚀 **Para começar a usar:**
1. Abra o `index.html`
2. Faça login
3. Comece cadastrando algumas medidas
4. Explore o menu
5. Veja os relatórios

---

## 📞 LEMBRETE IMPORTANTE

🔐 **Segurança:**
- Mantenha backup dos arquivos
- Não compartilhe usuário e senha
- Faça backup do banco de dados

🎨 **Visual:**
- As cores são oficiais da PMBA
- Layout responsivo (funciona no celular)
- Interface intuitiva

💾 **Dados:**
- Sistema funciona offline
- Dados ficam no computador
- Backup automático no navegador

---

**🎯 RESUMO SIMPLES:** 
Coloque todos os arquivos numa pasta, abra o `index.html`, faça login e use! É como instalar um jogo, mas para o trabalho da Polícia! 🚔
