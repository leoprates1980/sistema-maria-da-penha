# Novo arquivo de estilo CSS para o aplicativo da Ronda Maria da Penha - 29ª CIPM Seabra

Este arquivo CSS foi reformulado seguindo as cores oficiais da Polícia Militar da Bahia conforme definido no Manual de Identidade Visual e Imagem Corporativa da PMBA.

## Cores Oficiais Utilizadas

- **Azul Ferrete (Pantone 281)**: `#003d6b` - Cor principal da PMBA
- **Vermelho Carmesim (Pantone 200)**: `#c8102e` - Cor de alerta/erro
- **Amarelo (Pantone 116)**: `#ffdc00` - Cor de aviso
- **Azul Claro (Pantone 306)**: `#00aedb` - Cor de sucesso/destaque
- **Branco**: `#ffffff` - Cor de fundo/texto
- **Cinza (45% Preto)**: `#8c8c8c` - Cor secundária/texto

## Instruções de Implementação

Para implementar as cores oficiais da PMBA no aplicativo, substitua o conteúdo atual do arquivo `style.css` pelo código abaixo, mantendo o restante do CSS original após estas definições.

```css
:root {
  /* Cores oficiais da PMBA conforme Manual de Identidade Visual */
  --color-background: #ffffff;
  --color-surface: #ffffff;
  --color-text: #00264a;
  --color-text-secondary: #8c8c8c;
  --color-primary: #003d6b;
  --color-primary-hover: #00264a;
  --color-primary-active: #00264a;
  --color-secondary: rgba(0, 61, 107, 0.12);
  --color-secondary-hover: rgba(0, 61, 107, 0.2);
  --color-secondary-active: rgba(0, 61, 107, 0.25);
  --color-border: rgba(0, 61, 107, 0.2);
  --color-btn-primary-text: #ffffff;
  --color-card-border: rgba(0, 61, 107, 0.12);
  --color-card-border-inner: rgba(0, 61, 107, 0.12);
  --color-error: #c8102e;
  --color-success: #00aedb;
  --color-warning: #ffdc00;
  --color-info: #8c8c8c;
  --color-focus-ring: rgba(0, 61, 107, 0.4);
  --color-select-caret: rgba(0, 61, 107, 0.8);

  /* Common style patterns */
  --focus-ring: 0 0 0 3px var(--color-focus-ring);
  --focus-outline: 2px solid var(--color-primary);
  --status-bg-opacity: 0.15;
  --status-border-opacity: 0.25;
  --select-caret-light: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='16' height='16' viewBox='0 0 24 24' fill='none' stroke='%23003d6b' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpolyline points='6 9 12 15 18 9'%3E%3C/polyline%3E%3C/svg%3E");
  --select-caret-dark: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='16' height='16' viewBox='0 0 24 24' fill='none' stroke='%23ffffff' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpolyline points='6 9 12 15 18 9'%3E%3C/polyline%3E%3C/svg%3E");

  /* RGB versions for opacity control */
  --color-success-rgb: 0, 174, 219;
  --color-error-rgb: 200, 16, 46;
  --color-warning-rgb: 255, 220, 0;
  --color-info-rgb: 140, 140, 140;

  /* Typography */
  --font-family-base: "FKGroteskNeue", "Geist", "Inter", -apple-system,
    BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
  --font-family-mono: "Berkeley Mono", ui-monospace, SFMono-Regular, Menlo,
    Monaco, Consolas, monospace;
  --font-size-xs: 11px;
  --font-size-sm: 12px;
  --font-size-base: 14px;
  --font-size-md: 14px;
  --font-size-lg: 16px;
  --font-size-xl: 18px;
  --font-size-2xl: 20px;
  --font-size-3xl: 24px;
  --font-size-4xl: 30px;
  --font-weight-normal: 400;
  --font-weight-medium: 500;
  --font-weight-semibold: 550;
  --font-weight-bold: 600;
  --line-height-tight: 1.2;
  --line-height-normal: 1.5;
  --letter-spacing-tight: -0.01em;

  /* Spacing */
  --space-0: 0;
  --space-1: 1px;
  --space-2: 2px;
  --space-4: 4px;
  --space-6: 6px;
  --space-8: 8px;
  --space-10: 10px;
  --space-12: 12px;
  --space-16: 16px;
  --space-20: 20px;
  --space-24: 24px;
  --space-32: 32px;

  /* Border Radius */
  --radius-sm: 6px;
  --radius-base: 8px;
  --radius-md: 10px;
  --radius-lg: 12px;
  --radius-full: 9999px;

  /* Shadows */
  --shadow-xs: 0 1px 2px rgba(0, 0, 0, 0.02);
  --shadow-sm: 0 1px 3px rgba(0, 0, 0, 0.04), 0 1px 2px rgba(0, 0, 0, 0.02);
  --shadow-md: 0 4px 6px -1px rgba(0, 0, 0, 0.04),
    0 2px 4px -1px rgba(0, 0, 0, 0.02);
  --shadow-lg: 0 10px 15px -3px rgba(0, 0, 0, 0.04),
    0 4px 6px -2px rgba(0, 0, 0, 0.02);
  --shadow-inset-sm: inset 0 1px 0 rgba(255, 255, 255, 0.15),
    inset 0 -1px 0 rgba(0, 0, 0, 0.03);

  /* Animation */
  --duration-fast: 150ms;
  --duration-normal: 250ms;
  --ease-standard: cubic-bezier(0.16, 1, 0.3, 1);

  /* Layout */
  --container-sm: 640px;
  --container-md: 768px;
  --container-lg: 1024px;
  --container-xl: 1280px;
}

/* Dark mode colors */
@media (prefers-color-scheme: dark) {
  :root {
    --color-background: #00264a;
    --color-surface: #003d6b;
    --color-text: #ffffff;
    --color-text-secondary: rgba(255, 255, 255, 0.7);
    --color-primary: #00aedb;
    --color-primary-hover: #0099c2;
    --color-primary-active: #0099c2;
    --color-secondary: rgba(0, 174, 219, 0.15);
    --color-secondary-hover: rgba(0, 174, 219, 0.25);
    --color-secondary-active: rgba(0, 174, 219, 0.3);
    --color-border: rgba(255, 255, 255, 0.3);
    --color-error: #e63e54;
    --color-success: #00aedb;
    --color-warning: #ffdc00;
    --color-info: rgba(255, 255, 255, 0.7);
    --color-focus-ring: rgba(0, 174, 219, 0.4);
    --color-btn-primary-text: #00264a;
    --color-card-border: rgba(255, 255, 255, 0.2);
    --color-card-border-inner: rgba(255, 255, 255, 0.15);
    --shadow-inset-sm: inset 0 1px 0 rgba(255, 255, 255, 0.1),
      inset 0 -1px 0 rgba(0, 0, 0, 0.15);
    --button-border-secondary: rgba(255, 255, 255, 0.2);
    --color-border-secondary: rgba(255, 255, 255, 0.2);
    --color-select-caret: rgba(255, 255, 255, 0.8);

    /* RGB versions for dark mode */
    --color-success-rgb: 0, 174, 219;
    --color-error-rgb: 230, 62, 84;
    --color-warning-rgb: 255, 220, 0;
    --color-info-rgb: 255, 255, 255;
  }
}

/* Data attribute for manual theme switching */
[data-color-scheme="dark"] {
  --color-background: #00264a;
  --color-surface: #003d6b;
  --color-text: #ffffff;
  --color-text-secondary: rgba(255, 255, 255, 0.7);
  --color-primary: #00aedb;
  --color-primary-hover: #0099c2;
  --color-primary-active: #0099c2;
  --color-secondary: rgba(0, 174, 219, 0.15);
  --color-secondary-hover: rgba(0, 174, 219, 0.25);
  --color-secondary-active: rgba(0, 174, 219, 0.3);
  --color-border: rgba(255, 255, 255, 0.3);
  --color-error: #e63e54;
  --color-success: #00aedb;
  --color-warning: #ffdc00;
  --color-info: rgba(255, 255, 255, 0.7);
  --color-focus-ring: rgba(0, 174, 219, 0.4);
  --color-btn-primary-text: #00264a;
  --color-card-border: rgba(255, 255, 255, 0.2);
  --color-card-border-inner: rgba(255, 255, 255, 0.15);
  --shadow-inset-sm: inset 0 1px 0 rgba(255, 255, 255, 0.1),
    inset 0 -1px 0 rgba(0, 0, 0, 0.15);
  --button-border-secondary: rgba(255, 255, 255, 0.2);
  --color-border-secondary: rgba(255, 255, 255, 0.2);
  --color-select-caret: rgba(255, 255, 255, 0.8);

  /* RGB versions for dark mode */
  --color-success-rgb: 0, 174, 219;
  --color-error-rgb: 230, 62, 84;
  --color-warning-rgb: 255, 220, 0;
  --color-info-rgb: 255, 255, 255;
}

[data-color-scheme="light"] {
  --color-background: #ffffff;
  --color-surface: #ffffff;
  --color-text: #00264a;
  --color-text-secondary: #8c8c8c;
  --color-primary: #003d6b;
  --color-primary-hover: #00264a;
  --color-primary-active: #00264a;
  --color-secondary: rgba(0, 61, 107, 0.12);
  --color-secondary-hover: rgba(0, 61, 107, 0.2);
  --color-secondary-active: rgba(0, 61, 107, 0.25);
  --color-border: rgba(0, 61, 107, 0.2);
  --color-btn-primary-text: #ffffff;
  --color-card-border: rgba(0, 61, 107, 0.12);
  --color-card-border-inner: rgba(0, 61, 107, 0.12);
  --color-error: #c8102e;
  --color-success: #00aedb;
  --color-warning: #ffdc00;
  --color-info: #8c8c8c;
  --color-focus-ring: rgba(0, 61, 107, 0.4);

  /* RGB versions for light mode */
  --color-success-rgb: 0, 174, 219;
  --color-error-rgb: 200, 16, 46;
  --color-warning-rgb: 255, 220, 0;
  --color-info-rgb: 140, 140, 140;
}

/* Login Screen Styles */
.login-screen {
  min-height: 100vh;
  background: linear-gradient(135deg, #003d6b 0%, #00264a 100%);
  display: flex;
  align-items: center;
  justify-content: center;
  padding: var(--space-16);
}

.login-container {
  width: 100%;
  max-width: 420px;
}

.login-header {
  text-align: center;
  margin-bottom: var(--space-32);
}

.logo-container {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: var(--space-16);
  color: white;
  margin-bottom: var(--space-24);
}

.logo-pmba {
  background: white;
  color: #003d6b;
  font-size: var(--font-size-3xl);
  font-weight: var(--font-weight-bold);
  padding: var(--space-16) var(--space-20);
  border-radius: var(--radius-lg);
  box-shadow: var(--shadow-lg);
}

.unit-info h1 {
  font-size: var(--font-size-2xl);
  margin: 0;
  color: white;
}

.unit-info h2 {
  font-size: var(--font-size-lg);
  margin: var(--space-4) 0 0 0;
  color: rgba(255, 255, 255, 0.9);
  font-weight: var(--font-weight-normal);
}

/* App Header Styles - PMBA */
.app-header {
  background: #003d6b;
  color: white;
  padding: var(--space-16) var(--space-24);
  box-shadow: var(--shadow-md);
}

.header-content {
  display: flex;
  justify-content: space-between;
  align-items: center;
  max-width: var(--container-xl);
  margin: 0 auto;
}

.header-left {
  display: flex;
  align-items: center;
  gap: var(--space-16);
}

.logo-pmba-small {
  background: white;
  color: #003d6b;
  font-size: var(--font-size-lg);
  font-weight: var(--font-weight-bold);
  padding: var(--space-8) var(--space-12);
  border-radius: var(--radius-base);
}

/* Status específicos para PMBA */
.status--ativa {
  background-color: rgba(0, 174, 219, 0.15);
  color: #00aedb;
  border: 1px solid rgba(0, 174, 219, 0.25);
}

.status--descumprida {
  background-color: rgba(200, 16, 46, 0.15);
  color: #c8102e;
  border: 1px solid rgba(200, 16, 46, 0.25);
}

.status--suspensa {
  background-color: rgba(255, 220, 0, 0.15);
  color: #806e00;
  border: 1px solid rgba(255, 220, 0, 0.25);
}

.nav-link.active {
  background: rgba(0, 61, 107, 0.12);
  border-right-color: #003d6b;
  color: #003d6b;
  font-weight: var(--font-weight-medium);
}

.chart-container canvas {
  max-height: 300px;
  height: 300px;
}

/* Mantenha estes ajustes no topo do arquivo para garantir a precedência */
:root {
  /* Ajustes de cores oficiais da PMBA */
  --color-primary: #003d6b;
  --color-error: #c8102e;
  --color-success: #00aedb;
  --color-warning: #ffdc00;
}

@media (prefers-color-scheme: dark) {
  :root {
    --color-primary: #00aedb;
    --color-error: #e63e54;
  }
}
```

## Elementos Modificados

1. **Esquema de Cores**: Todas as cores foram ajustadas para seguir o padrão visual oficial da PMBA, incluindo:
   - Azul Ferrete como cor primária
   - Azul Claro para elementos de sucesso
   - Vermelho Carmesim para alertas e erros
   - Amarelo para avisos

2. **Tela de Login**: 
   - Gradiente de fundo usando o Azul Ferrete oficial
   - Logo com cores oficiais da PMBA

3. **Cabeçalho do Aplicativo**:
   - Cor de fundo usando o Azul Ferrete oficial
   - Logo com contraste em branco

4. **Indicadores de Status**:
   - Status "Ativa" usando Azul Claro
   - Status "Descumprida" usando Vermelho Carmesim 
   - Status "Suspensa" usando Amarelo

5. **Navegação**:
   - Item ativo destacado com cores oficiais

## Modo Escuro

O tema escuro também foi adaptado para usar as cores oficiais da PMBA, mas com ajustes para garantir contraste e legibilidade:

- Fundo em tons mais escuros do Azul Ferrete
- Destaque em Azul Claro para elementos primários
- Texto em branco para melhor contraste