---
name: design-guide
description: Enterprise-grade UI design system for creating exceptional modern interfaces. Comprehensive design tokens, advanced components, accessibility standards (WCAG 2.1 AA), animation system, dark mode, and professional UX patterns. Use for HTML artifacts, React components, dashboards, SaaS applications, landing pages, or any production-ready interface. Automatically ensures consistency, accessibility, and professional polish.
---

# Professional Design System

A comprehensive, production-ready design system that ensures every interface is modern, accessible, consistent, and delightful to use.

---

## Quick Start Overview

### When to Use
- **Ship fast with confidence:** Reach production-ready UI without reinventing foundations.
- **Scale design teams:** Keep designers, devs, y stakeholders alineados con un lenguaje común.
- **Renovar productos existentes:** Moderniza visuales sin sacrificar accesibilidad ni performance.

### Pillars at a Glance
- **Tokens & Semantics:** Base tokens más alias semánticos para superficies, texto e interacciones.
- **UX Patterns:** Guías opinadas para dashboards, formularios y flujos críticos.
- **Accessibility First:** Cobertura WCAG AA, soporte AT y lenguaje inclusivo.
- **Motion System:** Tiempos tokenizados, catálogo de microinteracciones y límites de rendimiento.

### Starter Checklist
| Área | Acciones clave |
|------|----------------|
| Fundamentos | Importa tokens → mapea nombres semánticos → documenta overrides |
| Componentes | Adopta variantes base → extiende vía composición → cubre estados |
| Accesibilidad | Audita contraste → valida navegación por teclado → prueba lector de pantalla |
| QA & Handoff | Sincroniza tokens (Figma ↔ código) → registra desviaciones en changelog |

---

## Table of Contents

1. [Core Philosophy](#core-philosophy)
2. [Design Tokens](#design-tokens)
3. [Typography System](#typography-system)
4. [Color System](#color-system)
5. [Spacing & Layout](#spacing--layout)
6. [Component Library](#component-library)
7. [Animation & Motion](#animation--motion)
8. [Accessibility](#accessibility)
9. [Dark Mode](#dark-mode)
10. [Responsive Design](#responsive-design)
11. [UX Patterns](#ux-patterns)
12. [Implementation Guide](#implementation-guide)

---

## Core Philosophy

### Design Principles

**1. Clarity First**
Every element communicates its purpose instantly. Remove cognitive load through clear visual hierarchy and intuitive patterns.

**2. Systematic Consistency**
Use design tokens religiously. Every spacing value, color, and size decision follows the system.

**3. Accessible by Default**
WCAG 2.1 AA compliance is non-negotiable. Design for everyone, including users with disabilities.

**4. Performance Matters**
Optimize for perceived performance. Fast interactions, meaningful loading states, and smooth animations.

**5. Content-Driven**
Design serves content, not the other way around. Let information breathe with generous white space.

**6. Progressive Enhancement**
Start with a solid foundation, then enhance for capable devices/browsers.

---

## Design Tokens

Design tokens are the single source of truth for all design decisions. Use CSS custom properties for maximum flexibility.

### Foundation Tokens

```css
:root {
  /* Spacing Scale (8px base) */
  --space-0: 0;
  --space-1: 0.25rem;    /* 4px */
  --space-2: 0.5rem;     /* 8px */
  --space-3: 0.75rem;    /* 12px */
  --space-4: 1rem;       /* 16px */
  --space-5: 1.25rem;    /* 20px */
  --space-6: 1.5rem;     /* 24px */
  --space-8: 2rem;       /* 32px */
  --space-10: 2.5rem;    /* 40px */
  --space-12: 3rem;      /* 48px */
  --space-16: 4rem;      /* 64px */
  --space-20: 5rem;      /* 80px */
  --space-24: 6rem;      /* 96px */
  --space-32: 8rem;      /* 128px */
  
  /* Font Sizes (Minor Third Scale - 1.2 ratio) */
  --text-xs: 0.75rem;    /* 12px */
  --text-sm: 0.875rem;   /* 14px */
  --text-base: 1rem;     /* 16px */
  --text-lg: 1.125rem;   /* 18px */
  --text-xl: 1.25rem;    /* 20px */
  --text-2xl: 1.5rem;    /* 24px */
  --text-3xl: 1.875rem;  /* 30px */
  --text-4xl: 2.25rem;   /* 36px */
  --text-5xl: 3rem;      /* 48px */
  --text-6xl: 3.75rem;   /* 60px */
  --text-7xl: 4.5rem;    /* 72px */
  
  /* Font Weights */
  --font-light: 300;
  --font-normal: 400;
  --font-medium: 500;
  --font-semibold: 600;
  --font-bold: 700;
  --font-extrabold: 800;
  
  /* Line Heights */
  --leading-none: 1;
  --leading-tight: 1.25;
  --leading-snug: 1.375;
  --leading-normal: 1.5;
  --leading-relaxed: 1.625;
  --leading-loose: 2;
  
  /* Letter Spacing */
  --tracking-tighter: -0.05em;
  --tracking-tight: -0.025em;
  --tracking-normal: 0;
  --tracking-wide: 0.025em;
  --tracking-wider: 0.05em;
  --tracking-widest: 0.1em;
  
  /* Border Radius */
  --radius-none: 0;
  --radius-sm: 0.25rem;   /* 4px */
  --radius-base: 0.5rem;  /* 8px */
  --radius-md: 0.75rem;   /* 12px */
  --radius-lg: 1rem;      /* 16px */
  --radius-xl: 1.5rem;    /* 24px */
  --radius-2xl: 2rem;     /* 32px */
  --radius-full: 9999px;
  
  /* Border Widths */
  --border-0: 0;
  --border-1: 1px;
  --border-2: 2px;
  --border-4: 4px;
  --border-8: 8px;
  
  /* Shadows (Light Mode) */
  --shadow-xs: 0 1px 2px 0 rgba(0, 0, 0, 0.05);
  --shadow-sm: 0 1px 3px 0 rgba(0, 0, 0, 0.1), 0 1px 2px -1px rgba(0, 0, 0, 0.1);
  --shadow-base: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -2px rgba(0, 0, 0, 0.1);
  --shadow-md: 0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -4px rgba(0, 0, 0, 0.1);
  --shadow-lg: 0 20px 25px -5px rgba(0, 0, 0, 0.1), 0 8px 10px -6px rgba(0, 0, 0, 0.1);
  --shadow-xl: 0 25px 50px -12px rgba(0, 0, 0, 0.25);
  --shadow-2xl: 0 35px 60px -15px rgba(0, 0, 0, 0.3);
  --shadow-inner: inset 0 2px 4px 0 rgba(0, 0, 0, 0.05);
  
  /* Z-Index Scale */
  --z-base: 0;
  --z-dropdown: 1000;
  --z-sticky: 1100;
  --z-fixed: 1200;
  --z-modal-backdrop: 1300;
  --z-modal: 1400;
  --z-popover: 1500;
  --z-tooltip: 1600;
  --z-notification: 1700;
  
  /* Transitions */
  --transition-fast: 150ms cubic-bezier(0.4, 0, 0.2, 1);
  --transition-base: 250ms cubic-bezier(0.4, 0, 0.2, 1);
  --transition-slow: 350ms cubic-bezier(0.4, 0, 0.2, 1);
  --transition-slower: 500ms cubic-bezier(0.4, 0, 0.2, 1);
  
  /* Easing Functions */
  --ease-in: cubic-bezier(0.4, 0, 1, 1);
  --ease-out: cubic-bezier(0, 0, 0.2, 1);
  --ease-in-out: cubic-bezier(0.4, 0, 0.2, 1);
  --ease-spring: cubic-bezier(0.68, -0.55, 0.265, 1.55);
  
  /* Container Max Widths */
  --container-sm: 640px;
  --container-md: 768px;
  --container-lg: 1024px;
  --container-xl: 1280px;
  --container-2xl: 1536px;
  
  /* Breakpoints (for reference in media queries) */
  --breakpoint-sm: 640px;
  --breakpoint-md: 768px;
  --breakpoint-lg: 1024px;
  --breakpoint-xl: 1280px;
  --breakpoint-2xl: 1536px;
}
```

---

## Typography System

### Font Stacks

```css
:root {
  /* System Font Stack (Default) */
  --font-sans: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Roboto', 
               'Oxygen', 'Ubuntu', 'Cantarell', 'Fira Sans', 'Droid Sans', 
               'Helvetica Neue', sans-serif;
  
  /* Monospace Stack */
  --font-mono: 'SF Mono', 'Monaco', 'Inconsolata', 'Fira Code', 
               'Fira Mono', 'Roboto Mono', 'Source Code Pro', monospace;
  
  /* Optional: Google Fonts (Professional Pairings) */
  
  /* Option 1: Inter (Modern, Clean) */
  --font-heading: 'Inter', var(--font-sans);
  --font-body: 'Inter', var(--font-sans);
  
  /* Option 2: Poppins + Inter (Distinct Hierarchy) */
  --font-heading: 'Poppins', var(--font-sans);
  --font-body: 'Inter', var(--font-sans);
  
  /* Option 3: Space Grotesk + Work Sans (Contemporary) */
  --font-heading: 'Space Grotesk', var(--font-sans);
  --font-body: 'Work Sans', var(--font-sans);
  
  /* Option 4: Plus Jakarta Sans (Geometric, Friendly) */
  --font-heading: 'Plus Jakarta Sans', var(--font-sans);
  --font-body: 'Plus Jakarta Sans', var(--font-sans);
}
```

### Semantic Tokens

Mapea los tokens base a nombres semánticos para facilitar escalabilidad y handoffs multi-equipo.

| Semántica | Alias sugerido | Uso principal |
|-----------|----------------|---------------|
| `--color-surface-default` | `var(--color-neutral-0)` | Fondos generales y contenedores estándar |
| `--color-surface-alt` | `var(--color-neutral-50)` | Paneles secundarios, tablas alternas |
| `--color-surface-inverse` | `var(--color-neutral-900)` | Navbars o barras inversas |
| `--color-text-primary` | `var(--color-neutral-900)` | Encabezados, copy crítico |
| `--color-text-secondary` | `var(--color-neutral-600)` | Descripciones, labels |
| `--color-text-inverse` | `var(--color-neutral-0)` | Texto sobre superficies oscuras |
| `--color-border-muted` | `var(--color-neutral-200)` | Divisores, tarjetas, inputs |
| `--color-border-strong` | `var(--color-neutral-400)` | Estados activos, componentes prominentes |
| `--color-interactive-primary` | `var(--color-primary-600)` | Botón principal, enlaces destacados |
| `--color-interactive-hover` | `var(--color-primary-700)` | Hover en CTA y chips seleccionables |
| `--space-stack-section` | `var(--space-16)` | Separación entre secciones |
| `--space-stack-block` | `var(--space-8)` | Separación entre bloques dentro de secciones |
| `--radius-component` | `var(--radius-base)` | Cards, inputs, menús |
| `--radius-pill` | `var(--radius-full)` | Badges, tags, toggles |

**Buenas prácticas**
- Documenta overrides de marca/tema en un changelog compartido.
- Expone los tokens semánticos en Figma y en el repositorio para evitar divergencias.
- Usa prefijos (`color-`, `space-`, `motion-`) para mantener orden y escalabilidad.

### Typography Styles

```css
/* Heading Styles */
.heading-1 {
  font-size: var(--text-5xl);
  font-weight: var(--font-extrabold);
  line-height: var(--leading-tight);
  letter-spacing: var(--tracking-tight);
  color: var(--text-primary);
  margin-bottom: var(--space-6);
}

.heading-2 {
  font-size: var(--text-4xl);
  font-weight: var(--font-bold);
  line-height: var(--leading-tight);
  letter-spacing: var(--tracking-tight);
  color: var(--text-primary);
  margin-bottom: var(--space-5);
}

.heading-3 {
  font-size: var(--text-3xl);
  font-weight: var(--font-semibold);
  line-height: var(--leading-snug);
  color: var(--text-primary);
  margin-bottom: var(--space-4);
}

.heading-4 {
  font-size: var(--text-2xl);
  font-weight: var(--font-semibold);
  line-height: var(--leading-snug);
  color: var(--text-primary);
  margin-bottom: var(--space-4);
}

.heading-5 {
  font-size: var(--text-xl);
  font-weight: var(--font-medium);
  line-height: var(--leading-normal);
  color: var(--text-primary);
  margin-bottom: var(--space-3);
}

.heading-6 {
  font-size: var(--text-lg);
  font-weight: var(--font-medium);
  line-height: var(--leading-normal);
  color: var(--text-secondary);
  margin-bottom: var(--space-3);
}

/* Body Text */
.text-body-lg {
  font-size: var(--text-lg);
  line-height: var(--leading-relaxed);
  color: var(--text-secondary);
}

.text-body {
  font-size: var(--text-base);
  line-height: var(--leading-normal);
  color: var(--text-secondary);
}

.text-body-sm {
  font-size: var(--text-sm);
  line-height: var(--leading-normal);
  color: var(--text-tertiary);
}

/* Display Text (Hero sections) */
.display-1 {
  font-size: var(--text-7xl);
  font-weight: var(--font-extrabold);
  line-height: var(--leading-none);
  letter-spacing: var(--tracking-tighter);
  color: var(--text-primary);
}

.display-2 {
  font-size: var(--text-6xl);
  font-weight: var(--font-bold);
  line-height: var(--leading-tight);
  letter-spacing: var(--tracking-tight);
  color: var(--text-primary);
}

/* Special Text Styles */
.text-label {
  font-size: var(--text-sm);
  font-weight: var(--font-medium);
  line-height: var(--leading-normal);
  letter-spacing: var(--tracking-wide);
  text-transform: uppercase;
  color: var(--text-tertiary);
}

.text-caption {
  font-size: var(--text-xs);
  line-height: var(--leading-normal);
  color: var(--text-tertiary);
}

.text-mono {
  font-family: var(--font-mono);
  font-size: var(--text-sm);
  line-height: var(--leading-normal);
}

/* Text Utilities */
.text-gradient {
  background: linear-gradient(135deg, var(--accent-primary), var(--accent-secondary));
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}

.text-balance {
  text-wrap: balance; /* CSS Text Level 4 */
}

.text-pretty {
  text-wrap: pretty; /* CSS Text Level 4 */
}
```

### Responsive Typography

```css
/* Fluid Typography (scales between min and max viewport) */
.heading-fluid {
  font-size: clamp(2rem, 5vw + 1rem, 4.5rem);
}

/* Mobile Adjustments */
@media (max-width: 768px) {
  .heading-1 { font-size: var(--text-4xl); }
  .heading-2 { font-size: var(--text-3xl); }
  .display-1 { font-size: var(--text-5xl); }
  .display-2 { font-size: var(--text-4xl); }
}
```

---

## Color System

### Semantic Color Palette

```css
:root {
  /* Base Colors (Light Mode) */
  --white: #ffffff;
  --black: #000000;
  
  /* Gray Scale (Neutral) */
  --gray-50: #f9fafb;
  --gray-100: #f3f4f6;
  --gray-200: #e5e7eb;
  --gray-300: #d1d5db;
  --gray-400: #9ca3af;
  --gray-500: #6b7280;
  --gray-600: #4b5563;
  --gray-700: #374151;
  --gray-800: #1f2937;
  --gray-900: #111827;
  --gray-950: #030712;
  
  /* Background Layers */
  --bg-primary: var(--white);
  --bg-secondary: var(--gray-50);
  --bg-tertiary: var(--gray-100);
  --bg-inverse: var(--gray-900);
  --bg-overlay: rgba(0, 0, 0, 0.5);
  
  /* Text Colors */
  --text-primary: var(--gray-900);
  --text-secondary: var(--gray-700);
  --text-tertiary: var(--gray-500);
  --text-quaternary: var(--gray-400);
  --text-disabled: var(--gray-300);
  --text-inverse: var(--white);
  --text-link: var(--accent-primary);
  --text-link-hover: var(--accent-primary-hover);
  
  /* Border Colors */
  --border-primary: var(--gray-200);
  --border-secondary: var(--gray-300);
  --border-tertiary: var(--gray-400);
  --border-focus: var(--accent-primary);
  --border-error: var(--error-primary);
  
  /* Accent Colors (Primary Brand) */
  --accent-primary: #2563eb;      /* Blue-600 */
  --accent-primary-hover: #1d4ed8; /* Blue-700 */
  --accent-primary-active: #1e40af; /* Blue-800 */
  --accent-primary-bg: #eff6ff;   /* Blue-50 */
  --accent-primary-border: #93c5fd; /* Blue-300 */
  
  /* Secondary Accent (Optional) */
  --accent-secondary: #7c3aed;      /* Purple-600 */
  --accent-secondary-hover: #6d28d9; /* Purple-700 */
  --accent-secondary-bg: #f5f3ff;   /* Purple-50 */
  
  /* Semantic Colors - Success */
  --success-primary: #059669;     /* Green-600 */
  --success-hover: #047857;       /* Green-700 */
  --success-bg: #ecfdf5;          /* Green-50 */
  --success-border: #6ee7b7;      /* Green-300 */
  --success-text: #065f46;        /* Green-800 */
  
  /* Semantic Colors - Warning */
  --warning-primary: #d97706;     /* Amber-600 */
  --warning-hover: #b45309;       /* Amber-700 */
  --warning-bg: #fffbeb;          /* Amber-50 */
  --warning-border: #fcd34d;      /* Amber-300 */
  --warning-text: #78350f;        /* Amber-900 */
  
  /* Semantic Colors - Error */
  --error-primary: #dc2626;       /* Red-600 */
  --error-hover: #b91c1c;         /* Red-700 */
  --error-bg: #fef2f2;            /* Red-50 */
  --error-border: #fca5a5;        /* Red-300 */
  --error-text: #991b1b;          /* Red-800 */
  
  /* Semantic Colors - Info */
  --info-primary: #0891b2;        /* Cyan-600 */
  --info-hover: #0e7490;          /* Cyan-700 */
  --info-bg: #ecfeff;             /* Cyan-50 */
  --info-border: #67e8f9;         /* Cyan-300 */
  --info-text: #164e63;           /* Cyan-900 */
}
```

### Color Utilities

```css
/* Background Utilities */
.bg-primary { background-color: var(--bg-primary); }
.bg-secondary { background-color: var(--bg-secondary); }
.bg-tertiary { background-color: var(--bg-tertiary); }

/* Text Color Utilities */
.text-primary { color: var(--text-primary); }
.text-secondary { color: var(--text-secondary); }
.text-tertiary { color: var(--text-tertiary); }

/* Border Color Utilities */
.border-primary { border-color: var(--border-primary); }
.border-secondary { border-color: var(--border-secondary); }

/* Semantic Background Utilities */
.bg-success { background-color: var(--success-bg); color: var(--success-text); }
.bg-warning { background-color: var(--warning-bg); color: var(--warning-text); }
.bg-error { background-color: var(--error-bg); color: var(--error-text); }
.bg-info { background-color: var(--info-bg); color: var(--info-text); }
```

---

## Spacing & Layout

### Container System

```css
.container {
  width: 100%;
  margin-left: auto;
  margin-right: auto;
  padding-left: var(--space-4);
  padding-right: var(--space-4);
}

@media (min-width: 640px) {
  .container { max-width: var(--container-sm); padding-left: var(--space-6); padding-right: var(--space-6); }
}

@media (min-width: 768px) {
  .container { max-width: var(--container-md); padding-left: var(--space-8); padding-right: var(--space-8); }
}

@media (min-width: 1024px) {
  .container { max-width: var(--container-lg); }
}

@media (min-width: 1280px) {
  .container { max-width: var(--container-xl); }
}

@media (min-width: 1536px) {
  .container { max-width: var(--container-2xl); }
}

/* Container Variants */
.container-narrow { max-width: var(--container-md); }
.container-wide { max-width: var(--container-2xl); }
.container-full { max-width: 100%; }
```

### Grid System

```css
/* Modern CSS Grid */
.grid {
  display: grid;
  gap: var(--space-6);
}

.grid-cols-1 { grid-template-columns: repeat(1, minmax(0, 1fr)); }
.grid-cols-2 { grid-template-columns: repeat(2, minmax(0, 1fr)); }
.grid-cols-3 { grid-template-columns: repeat(3, minmax(0, 1fr)); }
.grid-cols-4 { grid-template-columns: repeat(4, minmax(0, 1fr)); }
.grid-cols-6 { grid-template-columns: repeat(6, minmax(0, 1fr)); }
.grid-cols-12 { grid-template-columns: repeat(12, minmax(0, 1fr)); }

/* Auto-fit Grid (Responsive by nature) */
.grid-auto-fit {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(min(300px, 100%), 1fr));
  gap: var(--space-6);
}

.grid-auto-fill {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(min(300px, 100%), 1fr));
  gap: var(--space-6);
}

/* Gap Utilities */
.gap-2 { gap: var(--space-2); }
.gap-3 { gap: var(--space-3); }
.gap-4 { gap: var(--space-4); }
.gap-6 { gap: var(--space-6); }
.gap-8 { gap: var(--space-8); }

/* Responsive Grid */
@media (min-width: 768px) {
  .md\:grid-cols-2 { grid-template-columns: repeat(2, minmax(0, 1fr)); }
  .md\:grid-cols-3 { grid-template-columns: repeat(3, minmax(0, 1fr)); }
}

@media (min-width: 1024px) {
  .lg\:grid-cols-3 { grid-template-columns: repeat(3, minmax(0, 1fr)); }
  .lg\:grid-cols-4 { grid-template-columns: repeat(4, minmax(0, 1fr)); }
}
```

### Flexbox Utilities

```css
.flex { display: flex; }
.inline-flex { display: inline-flex; }

/* Direction */
.flex-row { flex-direction: row; }
.flex-col { flex-direction: column; }

/* Wrap */
.flex-wrap { flex-wrap: wrap; }
.flex-nowrap { flex-wrap: nowrap; }

/* Justify Content */
.justify-start { justify-content: flex-start; }
.justify-end { justify-content: flex-end; }
.justify-center { justify-content: center; }
.justify-between { justify-content: space-between; }
.justify-around { justify-content: space-around; }
.justify-evenly { justify-content: space-evenly; }

/* Align Items */
.items-start { align-items: flex-start; }
.items-end { align-items: flex-end; }
.items-center { align-items: center; }
.items-baseline { align-items: baseline; }
.items-stretch { align-items: stretch; }

/* Align Content */
.content-start { align-content: flex-start; }
.content-end { align-content: flex-end; }
.content-center { align-content: center; }
.content-between { align-content: space-between; }

/* Gap */
.flex-gap-2 { gap: var(--space-2); }
.flex-gap-4 { gap: var(--space-4); }
.flex-gap-6 { gap: var(--space-6); }

/* Grow & Shrink */
.flex-1 { flex: 1 1 0%; }
.flex-auto { flex: 1 1 auto; }
.flex-none { flex: none; }
```

### Stack Layout (Vertical Rhythm)

```css
.stack {
  display: flex;
  flex-direction: column;
}

.stack > * + * {
  margin-top: var(--space-4);
}

.stack-sm > * + * { margin-top: var(--space-2); }
.stack-md > * + * { margin-top: var(--space-4); }
.stack-lg > * + * { margin-top: var(--space-8); }
.stack-xl > * + * { margin-top: var(--space-12); }
```

### Section Spacing

```css
.section {
  padding-top: var(--space-16);
  padding-bottom: var(--space-16);
}

.section-sm {
  padding-top: var(--space-12);
  padding-bottom: var(--space-12);
}

.section-lg {
  padding-top: var(--space-24);
  padding-bottom: var(--space-24);
}

@media (max-width: 768px) {
  .section {
    padding-top: var(--space-12);
    padding-bottom: var(--space-12);
  }
}
```

---

## Component Library

### Buttons

```css
/* Base Button */
.btn {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: var(--space-2);
  padding: var(--space-3) var(--space-6);
  font-size: var(--text-base);
  font-weight: var(--font-medium);
  line-height: var(--leading-normal);
  border-radius: var(--radius-base);
  border: var(--border-2) solid transparent;
  cursor: pointer;
  transition: all var(--transition-fast);
  white-space: nowrap;
  user-select: none;
  position: relative;
  overflow: hidden;
}

.btn:focus-visible {
  outline: 2px solid var(--accent-primary);
  outline-offset: 2px;
}

.btn:disabled {
  opacity: 0.5;
  cursor: not-allowed;
  pointer-events: none;
}

/* Button Variants */
.btn-primary {
  background-color: var(--accent-primary);
  color: var(--white);
  box-shadow: var(--shadow-sm);
}

.btn-primary:hover {
  background-color: var(--accent-primary-hover);
  transform: translateY(-1px);
  box-shadow: var(--shadow-base);
}

.btn-primary:active {
  transform: translateY(0);
  box-shadow: var(--shadow-xs);
}

.btn-secondary {
  background-color: var(--bg-primary);
  color: var(--text-primary);
  border-color: var(--border-secondary);
}

.btn-secondary:hover {
  background-color: var(--bg-secondary);
  border-color: var(--border-tertiary);
}

.btn-ghost {
  background-color: transparent;
  color: var(--text-secondary);
}

.btn-ghost:hover {
  background-color: var(--bg-secondary);
  color: var(--text-primary);
}

.btn-danger {
  background-color: var(--error-primary);
  color: var(--white);
}

.btn-danger:hover {
  background-color: var(--error-hover);
}

.btn-success {
  background-color: var(--success-primary);
  color: var(--white);
}

.btn-success:hover {
  background-color: var(--success-hover);
}

/* Button Sizes */
.btn-sm {
  padding: var(--space-2) var(--space-4);
  font-size: var(--text-sm);
}

.btn-lg {
  padding: var(--space-4) var(--space-8);
  font-size: var(--text-lg);
}

.btn-xl {
  padding: var(--space-5) var(--space-10);
  font-size: var(--text-xl);
}

/* Button States with Icons */
.btn-loading {
  position: relative;
  color: transparent;
  pointer-events: none;
}

.btn-loading::after {
  content: '';
  position: absolute;
  width: 16px;
  height: 16px;
  top: 50%;
  left: 50%;
  margin-left: -8px;
  margin-top: -8px;
  border: 2px solid currentColor;
  border-radius: 50%;
  border-right-color: transparent;
  animation: spin 0.6s linear infinite;
}

@keyframes spin {
  to { transform: rotate(360deg); }
}

/* Icon Buttons */
.btn-icon {
  padding: var(--space-3);
  border-radius: var(--radius-full);
}

.btn-icon-sm {
  padding: var(--space-2);
}

.btn-icon-lg {
  padding: var(--space-4);
}

/* Button Group */
.btn-group {
  display: inline-flex;
  border-radius: var(--radius-base);
  box-shadow: var(--shadow-sm);
}

.btn-group .btn {
  border-radius: 0;
  margin: 0;
}

.btn-group .btn:first-child {
  border-top-left-radius: var(--radius-base);
  border-bottom-left-radius: var(--radius-base);
}

.btn-group .btn:last-child {
  border-top-right-radius: var(--radius-base);
  border-bottom-right-radius: var(--radius-base);
}

.btn-group .btn:not(:last-child) {
  border-right: 1px solid var(--border-primary);
}
```

### Cards

```css
.card {
  background-color: var(--bg-primary);
  border-radius: var(--radius-lg);
  padding: var(--space-6);
  transition: all var(--transition-base);
}

/* Card Variants */
.card-bordered {
  border: var(--border-1) solid var(--border-primary);
}

.card-elevated {
  box-shadow: var(--shadow-base);
}

.card-elevated:hover {
  box-shadow: var(--shadow-lg);
}

/* Interactive Card */
.card-interactive {
  cursor: pointer;
  transition: all var(--transition-base);
}

.card-interactive:hover {
  transform: translateY(-2px);
  box-shadow: var(--shadow-lg);
}

.card-interactive:active {
  transform: translateY(0);
}

/* Card Components */
.card-header {
  padding-bottom: var(--space-4);
  border-bottom: var(--border-1) solid var(--border-primary);
  margin-bottom: var(--space-4);
}

.card-title {
  font-size: var(--text-xl);
  font-weight: var(--font-semibold);
  color: var(--text-primary);
  margin: 0;
}

.card-description {
  font-size: var(--text-sm);
  color: var(--text-tertiary);
  margin-top: var(--space-2);
}

.card-body {
  padding: var(--space-4) 0;
}

.card-footer {
  padding-top: var(--space-4);
  border-top: var(--border-1) solid var(--border-primary);
  margin-top: var(--space-4);
  display: flex;
  align-items: center;
  justify-content: space-between;
}

/* Card Sizes */
.card-sm { padding: var(--space-4); }
.card-lg { padding: var(--space-8); }

/* Stat Card */
.card-stat {
  text-align: center;
  padding: var(--space-8);
}

.card-stat-value {
  font-size: var(--text-5xl);
  font-weight: var(--font-bold);
  color: var(--accent-primary);
  line-height: var(--leading-none);
}

.card-stat-label {
  font-size: var(--text-sm);
  color: var(--text-tertiary);
  margin-top: var(--space-2);
  text-transform: uppercase;
  letter-spacing: var(--tracking-wide);
}

.card-stat-change {
  display: inline-flex;
  align-items: center;
  gap: var(--space-1);
  margin-top: var(--space-3);
  font-size: var(--text-sm);
  font-weight: var(--font-medium);
}

.card-stat-change.positive { color: var(--success-primary); }
.card-stat-change.negative { color: var(--error-primary); }
```

### Form Controls

```css
/* Input Base */
.input {
  display: block;
  width: 100%;
  padding: var(--space-3) var(--space-4);
  font-size: var(--text-base);
  line-height: var(--leading-normal);
  color: var(--text-primary);
  background-color: var(--bg-primary);
  border: var(--border-2) solid var(--border-secondary);
  border-radius: var(--radius-base);
  transition: all var(--transition-fast);
  appearance: none;
}

.input::placeholder {
  color: var(--text-quaternary);
}

.input:hover {
  border-color: var(--border-tertiary);
}

.input:focus {
  outline: none;
  border-color: var(--accent-primary);
  box-shadow: 0 0 0 3px var(--accent-primary-bg);
}

.input:disabled {
  background-color: var(--bg-secondary);
  border-color: var(--border-primary);
  cursor: not-allowed;
  opacity: 0.6;
}

.input.error {
  border-color: var(--error-primary);
}

.input.error:focus {
  box-shadow: 0 0 0 3px var(--error-bg);
}

/* Input Sizes */
.input-sm {
  padding: var(--space-2) var(--space-3);
  font-size: var(--text-sm);
}

.input-lg {
  padding: var(--space-4) var(--space-5);
  font-size: var(--text-lg);
}

/* Textarea */
.textarea {
  resize: vertical;
  min-height: 120px;
}

/* Label */
.label {
  display: block;
  font-size: var(--text-sm);
  font-weight: var(--font-medium);
  color: var(--text-secondary);
  margin-bottom: var(--space-2);
}

.label-required::after {
  content: ' *';
  color: var(--error-primary);
}

/* Helper Text */
.helper-text {
  display: block;
  font-size: var(--text-sm);
  color: var(--text-tertiary);
  margin-top: var(--space-2);
}

.error-text {
  display: block;
  font-size: var(--text-sm);
  color: var(--error-primary);
  margin-top: var(--space-2);
}

/* Form Group */
.form-group {
  margin-bottom: var(--space-6);
}

/* Checkbox & Radio */
.checkbox,
.radio {
  display: inline-flex;
  align-items: center;
  gap: var(--space-3);
  cursor: pointer;
  user-select: none;
}

.checkbox input,
.radio input {
  width: 20px;
  height: 20px;
  margin: 0;
  cursor: pointer;
  accent-color: var(--accent-primary);
}

/* Select */
.select {
  display: block;
  width: 100%;
  padding: var(--space-3) var(--space-4);
  font-size: var(--text-base);
  color: var(--text-primary);
  background-color: var(--bg-primary);
  background-image: url("data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' fill='none' viewBox='0 0 20 20'%3e%3cpath stroke='%236b7280' stroke-linecap='round' stroke-linejoin='round' stroke-width='1.5' d='M6 8l4 4 4-4'/%3e%3c/svg%3e");
  background-position: right var(--space-3) center;
  background-repeat: no-repeat;
  background-size: 1.5em 1.5em;
  border: var(--border-2) solid var(--border-secondary);
  border-radius: var(--radius-base);
  padding-right: var(--space-10);
  cursor: pointer;
  transition: all var(--transition-fast);
}

.select:hover {
  border-color: var(--border-tertiary);
}

.select:focus {
  outline: none;
  border-color: var(--accent-primary);
  box-shadow: 0 0 0 3px var(--accent-primary-bg);
}

/* Toggle Switch */
.toggle {
  position: relative;
  display: inline-block;
  width: 44px;
  height: 24px;
}

.toggle input {
  opacity: 0;
  width: 0;
  height: 0;
}

.toggle-slider {
  position: absolute;
  cursor: pointer;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background-color: var(--gray-300);
  transition: var(--transition-base);
  border-radius: var(--radius-full);
}

.toggle-slider:before {
  position: absolute;
  content: "";
  height: 18px;
  width: 18px;
  left: 3px;
  bottom: 3px;
  background-color: white;
  transition: var(--transition-base);
  border-radius: 50%;
}

.toggle input:checked + .toggle-slider {
  background-color: var(--accent-primary);
}

.toggle input:checked + .toggle-slider:before {
  transform: translateX(20px);
}

.toggle input:focus-visible + .toggle-slider {
  box-shadow: 0 0 0 3px var(--accent-primary-bg);
}
```

### Navigation

```css
/* Navbar */
.navbar {
  position: sticky;
  top: 0;
  z-index: var(--z-sticky);
  background-color: var(--bg-primary);
  border-bottom: var(--border-1) solid var(--border-primary);
  backdrop-filter: blur(8px);
  background-color: rgba(255, 255, 255, 0.8);
}

.navbar-container {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: var(--space-4) var(--space-6);
  max-width: var(--container-2xl);
  margin: 0 auto;
}

.navbar-logo {
  font-size: var(--text-xl);
  font-weight: var(--font-bold);
  color: var(--text-primary);
  text-decoration: none;
}

.navbar-menu {
  display: flex;
  align-items: center;
  gap: var(--space-6);
  list-style: none;
  margin: 0;
  padding: 0;
}

.navbar-link {
  color: var(--text-secondary);
  text-decoration: none;
  font-size: var(--text-base);
  font-weight: var(--font-medium);
  transition: color var(--transition-fast);
  padding: var(--space-2) var(--space-3);
  border-radius: var(--radius-base);
}

.navbar-link:hover {
  color: var(--text-primary);
  background-color: var(--bg-secondary);
}

.navbar-link.active {
  color: var(--accent-primary);
}

/* Sidebar */
.sidebar {
  position: fixed;
  top: 0;
  left: 0;
  bottom: 0;
  width: 280px;
  background-color: var(--bg-primary);
  border-right: var(--border-1) solid var(--border-primary);
  padding: var(--space-6);
  overflow-y: auto;
  z-index: var(--z-fixed);
}

.sidebar-nav {
  display: flex;
  flex-direction: column;
  gap: var(--space-2);
}

.sidebar-link {
  display: flex;
  align-items: center;
  gap: var(--space-3);
  padding: var(--space-3) var(--space-4);
  color: var(--text-secondary);
  text-decoration: none;
  font-size: var(--text-base);
  font-weight: var(--font-medium);
  border-radius: var(--radius-base);
  transition: all var(--transition-fast);
}

.sidebar-link:hover {
  background-color: var(--bg-secondary);
  color: var(--text-primary);
}

.sidebar-link.active {
  background-color: var(--accent-primary-bg);
  color: var(--accent-primary);
}

.sidebar-section {
  margin-top: var(--space-6);
}

.sidebar-title {
  font-size: var(--text-xs);
  font-weight: var(--font-semibold);
  color: var(--text-tertiary);
  text-transform: uppercase;
  letter-spacing: var(--tracking-wider);
  margin-bottom: var(--space-3);
  padding: 0 var(--space-4);
}

/* Breadcrumbs */
.breadcrumbs {
  display: flex;
  align-items: center;
  gap: var(--space-2);
  font-size: var(--text-sm);
  color: var(--text-tertiary);
  padding: var(--space-4) 0;
}

.breadcrumb-item {
  display: flex;
  align-items: center;
  gap: var(--space-2);
}

.breadcrumb-link {
  color: var(--text-secondary);
  text-decoration: none;
  transition: color var(--transition-fast);
}

.breadcrumb-link:hover {
  color: var(--accent-primary);
}

.breadcrumb-separator {
  color: var(--text-quaternary);
}

.breadcrumb-current {
  color: var(--text-primary);
  font-weight: var(--font-medium);
}

/* Tabs */
.tabs {
  display: flex;
  border-bottom: var(--border-1) solid var(--border-primary);
}

.tab {
  padding: var(--space-4) var(--space-6);
  font-size: var(--text-base);
  font-weight: var(--font-medium);
  color: var(--text-tertiary);
  background: none;
  border: none;
  border-bottom: 2px solid transparent;
  cursor: pointer;
  transition: all var(--transition-fast);
  position: relative;
  bottom: -1px;
}

.tab:hover {
  color: var(--text-secondary);
  background-color: var(--bg-secondary);
}

.tab.active {
  color: var(--accent-primary);
  border-bottom-color: var(--accent-primary);
}

.tab-content {
  padding: var(--space-6) 0;
}
```

### Modals & Dialogs

```css
/* Modal Backdrop */
.modal-backdrop {
  position: fixed;
  inset: 0;
  background-color: var(--bg-overlay);
  z-index: var(--z-modal-backdrop);
  display: flex;
  align-items: center;
  justify-content: center;
  padding: var(--space-4);
  animation: fadeIn var(--transition-base);
}

@keyframes fadeIn {
  from { opacity: 0; }
  to { opacity: 1; }
}

/* Modal Container */
.modal {
  background-color: var(--bg-primary);
  border-radius: var(--radius-lg);
  box-shadow: var(--shadow-2xl);
  max-width: 500px;
  width: 100%;
  max-height: 90vh;
  overflow: hidden;
  animation: slideUp var(--transition-base);
  z-index: var(--z-modal);
}

@keyframes slideUp {
  from {
    opacity: 0;
    transform: translateY(20px) scale(0.95);
  }
  to {
    opacity: 1;
    transform: translateY(0) scale(1);
  }
}

.modal-header {
  padding: var(--space-6);
  border-bottom: var(--border-1) solid var(--border-primary);
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.modal-title {
  font-size: var(--text-2xl);
  font-weight: var(--font-semibold);
  color: var(--text-primary);
  margin: 0;
}

.modal-close {
  padding: var(--space-2);
  background: none;
  border: none;
  cursor: pointer;
  color: var(--text-tertiary);
  border-radius: var(--radius-base);
  transition: all var(--transition-fast);
}

.modal-close:hover {
  background-color: var(--bg-secondary);
  color: var(--text-primary);
}

.modal-body {
  padding: var(--space-6);
  overflow-y: auto;
  max-height: calc(90vh - 140px);
}

.modal-footer {
  padding: var(--space-6);
  border-top: var(--border-1) solid var(--border-primary);
  display: flex;
  align-items: center;
  justify-content: flex-end;
  gap: var(--space-3);
}

/* Modal Sizes */
.modal-sm { max-width: 400px; }
.modal-lg { max-width: 800px; }
.modal-xl { max-width: 1200px; }
.modal-full { max-width: calc(100% - var(--space-8)); }
```

### Toast Notifications

```css
.toast-container {
  position: fixed;
  top: var(--space-6);
  right: var(--space-6);
  z-index: var(--z-notification);
  display: flex;
  flex-direction: column;
  gap: var(--space-3);
  max-width: 420px;
  pointer-events: none;
}

.toast {
  background-color: var(--bg-primary);
  border-radius: var(--radius-lg);
  box-shadow: var(--shadow-lg);
  padding: var(--space-4);
  display: flex;
  align-items: flex-start;
  gap: var(--space-3);
  pointer-events: auto;
  animation: slideInRight var(--transition-base);
}

@keyframes slideInRight {
  from {
    opacity: 0;
    transform: translateX(100%);
  }
  to {
    opacity: 1;
    transform: translateX(0);
  }
}

.toast-icon {
  flex-shrink: 0;
  width: 20px;
  height: 20px;
  border-radius: var(--radius-full);
  display: flex;
  align-items: center;
  justify-content: center;
}

.toast-content {
  flex: 1;
}

.toast-title {
  font-size: var(--text-base);
  font-weight: var(--font-semibold);
  color: var(--text-primary);
  margin-bottom: var(--space-1);
}

.toast-message {
  font-size: var(--text-sm);
  color: var(--text-secondary);
}

.toast-close {
  flex-shrink: 0;
  padding: var(--space-1);
  background: none;
  border: none;
  cursor: pointer;
  color: var(--text-tertiary);
  border-radius: var(--radius-base);
  transition: all var(--transition-fast);
}

.toast-close:hover {
  background-color: var(--bg-secondary);
}

/* Toast Variants */
.toast-success {
  border-left: 4px solid var(--success-primary);
}

.toast-success .toast-icon {
  background-color: var(--success-bg);
  color: var(--success-primary);
}

.toast-error {
  border-left: 4px solid var(--error-primary);
}

.toast-error .toast-icon {
  background-color: var(--error-bg);
  color: var(--error-primary);
}

.toast-warning {
  border-left: 4px solid var(--warning-primary);
}

.toast-warning .toast-icon {
  background-color: var(--warning-bg);
  color: var(--warning-primary);
}

.toast-info {
  border-left: 4px solid var(--info-primary);
}

.toast-info .toast-icon {
  background-color: var(--info-bg);
  color: var(--info-primary);
}
```

### Tables

```css
.table-container {
  overflow-x: auto;
  border-radius: var(--radius-lg);
  border: var(--border-1) solid var(--border-primary);
}

.table {
  width: 100%;
  border-collapse: collapse;
  font-size: var(--text-sm);
}

.table thead {
  background-color: var(--bg-secondary);
  border-bottom: var(--border-2) solid var(--border-secondary);
}

.table th {
  padding: var(--space-4);
  text-align: left;
  font-weight: var(--font-semibold);
  color: var(--text-secondary);
  text-transform: uppercase;
  font-size: var(--text-xs);
  letter-spacing: var(--tracking-wider);
}

.table td {
  padding: var(--space-4);
  border-bottom: var(--border-1) solid var(--border-primary);
  color: var(--text-primary);
}

.table tbody tr:last-child td {
  border-bottom: none;
}

.table tbody tr:hover {
  background-color: var(--bg-secondary);
}

/* Striped Table */
.table-striped tbody tr:nth-child(even) {
  background-color: var(--bg-secondary);
}

/* Compact Table */
.table-compact th,
.table-compact td {
  padding: var(--space-2) var(--space-3);
}

/* Table with Actions */
.table-actions {
  display: flex;
  gap: var(--space-2);
}
```

### Badges & Pills

```css
.badge {
  display: inline-flex;
  align-items: center;
  gap: var(--space-1);
  padding: var(--space-1) var(--space-3);
  font-size: var(--text-xs);
  font-weight: var(--font-medium);
  line-height: var(--leading-none);
  border-radius: var(--radius-full);
  white-space: nowrap;
}

/* Badge Variants */
.badge-primary {
  background-color: var(--accent-primary-bg);
  color: var(--accent-primary);
}

.badge-success {
  background-color: var(--success-bg);
  color: var(--success-text);
}

.badge-warning {
  background-color: var(--warning-bg);
  color: var(--warning-text);
}

.badge-error {
  background-color: var(--error-bg);
  color: var(--error-text);
}

.badge-info {
  background-color: var(--info-bg);
  color: var(--info-text);
}

.badge-neutral {
  background-color: var(--bg-tertiary);
  color: var(--text-secondary);
}

/* Badge Sizes */
.badge-sm {
  padding: 0 var(--space-2);
  font-size: 0.65rem;
}

.badge-lg {
  padding: var(--space-2) var(--space-4);
  font-size: var(--text-sm);
}

/* Badge with Dot */
.badge-dot::before {
  content: '';
  width: 6px;
  height: 6px;
  border-radius: 50%;
  background-color: currentColor;
}
```

### Progress Indicators

```css
/* Progress Bar */
.progress {
  width: 100%;
  height: 8px;
  background-color: var(--bg-tertiary);
  border-radius: var(--radius-full);
  overflow: hidden;
}

.progress-bar {
  height: 100%;
  background-color: var(--accent-primary);
  border-radius: var(--radius-full);
  transition: width var(--transition-slow);
}

/* Progress Variants */
.progress-bar-success { background-color: var(--success-primary); }
.progress-bar-warning { background-color: var(--warning-primary); }
.progress-bar-error { background-color: var(--error-primary); }

/* Progress Sizes */
.progress-sm { height: 4px; }
.progress-lg { height: 12px; }

/* Animated Progress */
.progress-bar-animated {
  background-image: linear-gradient(
    45deg,
    rgba(255, 255, 255, 0.15) 25%,
    transparent 25%,
    transparent 50%,
    rgba(255, 255, 255, 0.15) 50%,
    rgba(255, 255, 255, 0.15) 75%,
    transparent 75%,
    transparent
  );
  background-size: 1rem 1rem;
  animation: progressAnimation 1s linear infinite;
}

@keyframes progressAnimation {
  0% { background-position: 1rem 0; }
  100% { background-position: 0 0; }
}

/* Spinner */
.spinner {
  width: 40px;
  height: 40px;
  border: 4px solid var(--bg-tertiary);
  border-top-color: var(--accent-primary);
  border-radius: 50%;
  animation: spin 0.8s linear infinite;
}

.spinner-sm {
  width: 20px;
  height: 20px;
  border-width: 2px;
}

.spinner-lg {
  width: 60px;
  height: 60px;
  border-width: 6px;
}

/* Skeleton Loader */
.skeleton {
  background: linear-gradient(
    90deg,
    var(--bg-tertiary) 0%,
    var(--bg-secondary) 50%,
    var(--bg-tertiary) 100%
  );
  background-size: 200% 100%;
  animation: skeleton 1.5s ease-in-out infinite;
  border-radius: var(--radius-base);
}

@keyframes skeleton {
  0% { background-position: 200% 0; }
  100% { background-position: -200% 0; }
}

.skeleton-text {
  height: 16px;
  margin-bottom: var(--space-2);
}

.skeleton-title {
  height: 24px;
  width: 60%;
  margin-bottom: var(--space-4);
}

.skeleton-avatar {
  width: 48px;
  height: 48px;
  border-radius: var(--radius-full);
}

.skeleton-card {
  height: 200px;
}
```

### Alerts

```css
.alert {
  display: flex;
  align-items: flex-start;
  gap: var(--space-3);
  padding: var(--space-4);
  border-radius: var(--radius-base);
  border-left: 4px solid;
}

.alert-icon {
  flex-shrink: 0;
  width: 20px;
  height: 20px;
}

.alert-content {
  flex: 1;
}

.alert-title {
  font-size: var(--text-base);
  font-weight: var(--font-semibold);
  margin-bottom: var(--space-1);
}

.alert-message {
  font-size: var(--text-sm);
  line-height: var(--leading-relaxed);
}

.alert-close {
  flex-shrink: 0;
  padding: var(--space-1);
  background: none;
  border: none;
  cursor: pointer;
  border-radius: var(--radius-base);
  transition: background-color var(--transition-fast);
}

/* Alert Variants */
.alert-success {
  background-color: var(--success-bg);
  border-color: var(--success-primary);
  color: var(--success-text);
}

.alert-success .alert-icon {
  color: var(--success-primary);
}

.alert-warning {
  background-color: var(--warning-bg);
  border-color: var(--warning-primary);
  color: var(--warning-text);
}

.alert-warning .alert-icon {
  color: var(--warning-primary);
}

.alert-error {
  background-color: var(--error-bg);
  border-color: var(--error-primary);
  color: var(--error-text);
}

.alert-error .alert-icon {
  color: var(--error-primary);
}

.alert-info {
  background-color: var(--info-bg);
  border-color: var(--info-primary);
  color: var(--info-text);
}

.alert-info .alert-icon {
  color: var(--info-primary);
}
```

---

## Animation & Motion

### Motion Principles

1. **Purposeful**: Every animation should communicate or guide
2. **Performant**: Use `transform` and `opacity` for best performance
3. **Subtle**: Animations should enhance, not distract
4. **Consistent**: Use the same durations and easings throughout

### Timing & Easing Matrix

| Categoría | Duración | Easing | Uso recomendado |
|-----------|----------|--------|-----------------|
| Micro feedback (hover, ripple) | 120–180 ms | `var(--ease-out)` | Respuesta inmediata en botones, chips, toggles |
| Estado intermedio (loaders, skeleton fade) | 200–320 ms | `var(--ease-in-out)` | Transiciones entre placeholder y contenido real |
| Cambios de layout (modals, drawers) | 280–420 ms | `var(--ease-spring)` | Entrada de elementos a pantalla, debe incluir atenuación |
| Navegación entre vistas | 320–450 ms | `var(--ease-in-out)` | Transiciones entre páginas o pestañas, usa desvanecimiento + slide |
| Feedback crítico (errores, éxito) | 150–250 ms | `var(--ease-out)` con `opacity` | Mostrar banners, toasts, validaciones inline |

**Guías clave**
- Limita el movimiento en áreas densas (tablas, formularios) a fades o cambios de color.
- Agrupa animaciones correlacionadas en timelines cortos (máximo 500 ms) para evitar cascadas.
- Da control al usuario: permite saltar animaciones largas (ej. tour interactivo) y honra `prefers-reduced-motion`.

### Micro-interactions

```css
/* Hover Lift */
.hover-lift {
  transition: transform var(--transition-base), box-shadow var(--transition-base);
}

.hover-lift:hover {
  transform: translateY(-2px);
  box-shadow: var(--shadow-lg);
}

/* Hover Scale */
.hover-scale {
  transition: transform var(--transition-base);
}

.hover-scale:hover {
  transform: scale(1.05);
}

/* Hover Brightness */
.hover-brightness {
  transition: filter var(--transition-base);
}

.hover-brightness:hover {
  filter: brightness(1.1);
}

/* Hover Glow */
.hover-glow {
  position: relative;
  overflow: hidden;
}

.hover-glow::after {
  content: '';
  position: absolute;
  top: 50%;
  left: 50%;
  width: 0;
  height: 0;
  border-radius: 50%;
  background: rgba(255, 255, 255, 0.5);
  transform: translate(-50%, -50%);
  transition: width var(--transition-slow), height var(--transition-slow);
}

.hover-glow:hover::after {
  width: 300px;
  height: 300px;
}

/* Ripple Effect */
.ripple {
  position: relative;
  overflow: hidden;
}

.ripple::after {
  content: '';
  position: absolute;
  top: 50%;
  left: 50%;
  width: 0;
  height: 0;
  border-radius: 50%;
  background: rgba(255, 255, 255, 0.5);
  transform: translate(-50%, -50%);
  opacity: 0;
}

.ripple:active::after {
  width: 200px;
  height: 200px;
  opacity: 1;
  transition: width 0.4s, height 0.4s, opacity 0.4s;
}
```

### Page Transitions

```css
/* Fade In */
.fade-in {
  animation: fadeIn var(--transition-base) var(--ease-out);
}

@keyframes fadeIn {
  from { opacity: 0; }
  to { opacity: 1; }
}

/* Slide In (from bottom) */
.slide-in-bottom {
  animation: slideInBottom var(--transition-base) var(--ease-out);
}

@keyframes slideInBottom {
  from {
    opacity: 0;
    transform: translateY(30px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

/* Slide In (from left) */
.slide-in-left {
  animation: slideInLeft var(--transition-base) var(--ease-out);
}

@keyframes slideInLeft {
  from {
    opacity: 0;
    transform: translateX(-30px);
  }
  to {
    opacity: 1;
    transform: translateX(0);
  }
}

/* Scale In */
.scale-in {
  animation: scaleIn var(--transition-base) var(--ease-out);
}

@keyframes scaleIn {
  from {
    opacity: 0;
    transform: scale(0.9);
  }
  to {
    opacity: 1;
    transform: scale(1);
  }
}

/* Stagger Children */
.stagger-children > * {
  opacity: 0;
  animation: fadeIn var(--transition-base) var(--ease-out) forwards;
}

.stagger-children > *:nth-child(1) { animation-delay: 0ms; }
.stagger-children > *:nth-child(2) { animation-delay: 100ms; }
.stagger-children > *:nth-child(3) { animation-delay: 200ms; }
.stagger-children > *:nth-child(4) { animation-delay: 300ms; }
.stagger-children > *:nth-child(5) { animation-delay: 400ms; }
```

### Loading States

```css
/* Pulse Animation */
.pulse {
  animation: pulse 2s cubic-bezier(0.4, 0, 0.6, 1) infinite;
}

@keyframes pulse {
  0%, 100% { opacity: 1; }
  50% { opacity: 0.5; }
}

/* Bounce Animation */
.bounce {
  animation: bounce 1s infinite;
}

@keyframes bounce {
  0%, 100% {
    transform: translateY(-25%);
    animation-timing-function: cubic-bezier(0.8, 0, 1, 1);
  }
  50% {
    transform: translateY(0);
    animation-timing-function: cubic-bezier(0, 0, 0.2, 1);
  }
}

/* Shimmer Effect */
.shimmer {
  background: linear-gradient(
    90deg,
    transparent 0%,
    rgba(255, 255, 255, 0.2) 50%,
    transparent 100%
  );
  background-size: 200% 100%;
  animation: shimmer 2s infinite;
}

@keyframes shimmer {
  0% { background-position: -200% 0; }
  100% { background-position: 200% 0; }
}
```

---

## Accessibility

### WCAG 2.1 AA Requirements

#### Color Contrast

```css
/* Minimum contrast ratios */
/* Normal text (< 18pt): 4.5:1 */
/* Large text (≥ 18pt or ≥ 14pt bold): 3:1 */

/* Ensure sufficient contrast */
.accessible-text {
  /* ✅ Good: #212529 on #ffffff = 15.66:1 */
  color: var(--text-primary);
  background: var(--bg-primary);
  
  /* ❌ Bad: #d1d5db on #ffffff = 1.82:1 */
  /* color: var(--gray-300);
  background: var(--white); */
}
```

#### Focus States

```css
/* Visible focus indicator (minimum 2px) */
*:focus-visible {
  outline: 2px solid var(--accent-primary);
  outline-offset: 2px;
}

/* Custom focus ring */
.focus-ring:focus-visible {
  outline: none;
  box-shadow: 0 0 0 3px var(--accent-primary-bg), 
              0 0 0 5px var(--accent-primary);
}

/* Remove focus for mouse users, keep for keyboard */
*:focus:not(:focus-visible) {
  outline: none;
}
```

#### Keyboard Navigation

```css
/* Skip to content link */
.skip-link {
  position: absolute;
  top: -40px;
  left: 0;
  background: var(--accent-primary);
  color: white;
  padding: var(--space-2) var(--space-4);
  text-decoration: none;
  z-index: 100;
}

.skip-link:focus {
  top: 0;
}

/* Ensure tabbable elements are clearly indicated */
button, a, input, select, textarea, [tabindex="0"] {
  /* Already styled with focus-visible */
}
```

#### Screen Reader Support

```html
<!-- Semantic HTML -->
<nav aria-label="Main navigation">...</nav>
<main>...</main>
<aside aria-label="Sidebar">...</aside>

<!-- ARIA Labels -->
<button aria-label="Close modal">
  <svg>...</svg>
</button>

<!-- Hidden content for screen readers -->
<span class="sr-only">Loading...</span>

<!-- Live regions for dynamic content -->
<div aria-live="polite" aria-atomic="true">
  <!-- Status messages -->
</div>
```

```css
/* Screen reader only content */
.sr-only {
  position: absolute;
  width: 1px;
  height: 1px;
  padding: 0;
  margin: -1px;
  overflow: hidden;
  clip: rect(0, 0, 0, 0);
  white-space: nowrap;
  border-width: 0;
}

/* Focusable screen reader content */
.sr-only-focusable:active,
  .sr-only-focusable:focus {
    position: static;
    width: auto;
    height: auto;
    overflow: visible;
    clip: auto;
    white-space: normal;
  }
```

#### Assistive Technology Playbook

- **Screen readers:** NVDA (Windows) + VoiceOver (macOS/iOS). Verifica navegación por headings, landmarks, y lectura de tablas/errores.
- **Teclado puro:** `Tab`, `Shift+Tab`, `Enter`, `Space`, flechas en menús y tablas. Documenta rutas clave y bloqueos.
- **Contraste:** Usa herramientas automáticas (axe, Stark) más validación manual en componentes dinámicos/bordes.
- **Color blindness:** Simula (protanopia, deuteranopia, tritanopia) y valida que las diferencias dependan también de iconografía o texto.
- **Zoom / reflow:** Prueba 200% y 400% sin pérdida de contenido ni scroll horizontal.

#### Accessibility QA Sprint

| Día | Actividad | Criterio de salida |
|-----|-----------|--------------------|
| 1 | Auditoría tokens (contraste, foco, tamaño) | Matriz de tokens aprobados fallidos documentada |
| 2 | Revisión de componentes interactivos (forms, tablas, modales) | Listado de issues por severidad + recomendaciones |
| 3 | Pruebas AT (screen readers, teclado, zoom) | Evidencias grabadas + acciones correctivas asignadas |
| 4 | Language & content | Microcopy inclusivo, mensajes de error accionables, traducciones consistentes |
| 5 | Regression check | Re-ejecutar axe/Storybook tests, actualizar documentación y changelog |

#### Touch Targets

```css
/* Minimum 44x44px touch targets (WCAG 2.1 Level AAA) */
.touch-target {
  min-width: 44px;
  min-height: 44px;
  
  /* For smaller visual elements, add padding */
  padding: var(--space-3);
}

/* Adequate spacing between touch targets */
.touch-group > * + * {
  margin-left: var(--space-2); /* Minimum 8px */
}
```

#### Motion Preferences

```css
/* Respect user's motion preferences */
@media (prefers-reduced-motion: reduce) {
  *,
  *::before,
  *::after {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
    scroll-behavior: auto !important;
  }
}
```

---

## Dark Mode

### Dark Mode Color Tokens

```css
@media (prefers-color-scheme: dark) {
  :root {
    /* Gray Scale (Dark Mode) */
    --bg-primary: var(--gray-950);
    --bg-secondary: var(--gray-900);
    --bg-tertiary: var(--gray-800);
    --bg-inverse: var(--white);
    --bg-overlay: rgba(0, 0, 0, 0.8);
    
    /* Text Colors (Dark Mode) */
    --text-primary: var(--gray-50);
    --text-secondary: var(--gray-300);
    --text-tertiary: var(--gray-400);
    --text-quaternary: var(--gray-500);
    --text-disabled: var(--gray-600);
    --text-inverse: var(--gray-900);
    
    /* Border Colors (Dark Mode) */
    --border-primary: var(--gray-800);
    --border-secondary: var(--gray-700);
    --border-tertiary: var(--gray-600);
    
    /* Shadows (Dark Mode - more subtle) */
    --shadow-xs: 0 1px 2px 0 rgba(0, 0, 0, 0.3);
    --shadow-sm: 0 1px 3px 0 rgba(0, 0, 0, 0.4), 0 1px 2px -1px rgba(0, 0, 0, 0.4);
    --shadow-base: 0 4px 6px -1px rgba(0, 0, 0, 0.5), 0 2px 4px -2px rgba(0, 0, 0, 0.5);
    --shadow-md: 0 10px 15px -3px rgba(0, 0, 0, 0.6), 0 4px 6px -4px rgba(0, 0, 0, 0.6);
    --shadow-lg: 0 20px 25px -5px rgba(0, 0, 0, 0.7), 0 8px 10px -6px rgba(0, 0, 0, 0.7);
    --shadow-xl: 0 25px 50px -12px rgba(0, 0, 0, 0.8);
    --shadow-2xl: 0 35px 60px -15px rgba(0, 0, 0, 0.9);
    
    /* Adjust accent colors for dark mode (slightly lighter) */
    --accent-primary: #3b82f6;  /* Blue-500 instead of Blue-600 */
    --accent-primary-hover: #2563eb;
    --accent-primary-bg: rgba(59, 130, 246, 0.1);
  }
}

/* Manual dark mode toggle */
[data-theme="dark"] {
  /* Same variables as above */
}
```

### Dark Mode Implementation

```javascript
// JavaScript for manual theme toggle
const themeToggle = document.getElementById('theme-toggle');
const htmlElement = document.documentElement;

// Check for saved theme preference or default to system preference
const currentTheme = localStorage.getItem('theme') 
  || (window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light');

htmlElement.setAttribute('data-theme', currentTheme);

themeToggle?.addEventListener('click', () => {
  const theme = htmlElement.getAttribute('data-theme');
  const newTheme = theme === 'dark' ? 'light' : 'dark';
  
  htmlElement.setAttribute('data-theme', newTheme);
  localStorage.setItem('theme', newTheme);
});
```

---

## Responsive Design

### Mobile-First Approach

```css
/* Base styles (mobile) */
.responsive-element {
  padding: var(--space-4);
  font-size: var(--text-base);
}

/* Tablet (768px+) */
@media (min-width: 768px) {
  .responsive-element {
    padding: var(--space-6);
    font-size: var(--text-lg);
  }
}

/* Desktop (1024px+) */
@media (min-width: 1024px) {
  .responsive-element {
    padding: var(--space-8);
  }
}
```

### Responsive Utilities

```css
/* Hide on mobile */
.hidden-mobile { display: none; }

@media (min-width: 768px) {
  .hidden-mobile { display: block; }
}

/* Show only on mobile */
.visible-mobile { display: block; }

@media (min-width: 768px) {
  .visible-mobile { display: none; }
}

/* Responsive text alignment */
.text-center-mobile {
  text-align: center;
}

@media (min-width: 768px) {
  .text-center-mobile {
    text-align: left;
  }
}
```

### Container Queries (Modern CSS)

```css
.card-container {
  container-type: inline-size;
}

.responsive-card {
  display: flex;
  flex-direction: column;
}

/* When container is wide enough, switch to row layout */
@container (min-width: 500px) {
  .responsive-card {
    flex-direction: row;
    gap: var(--space-6);
  }
}
```

---

## Tone & Voice Matrix

| Tono | Uso típico | Paleta sugerida | Microcopy guiado |
|------|------------|-----------------|------------------|
| **Corporate / Trust** | Fintech, banca, enterprise | Primario 600, neutrales fríos, acentos limitados | Verbos formales (“Gestiona”, “Autoriza”), claridad sobre emoción |
| **Friendly / Onboarding** | SaaS colaborativo, educación | Primario 500 + secundarios pastel, ilustraciones suaves | Mensajes en segunda persona, emojis puntuales en tooltips |
| **Alert / Critical** | Seguridad, monitoreo, incidentes | Error 600 + fondo neutro, iconografía clara | Lenguaje directo, incluye próximos pasos y SLA |
| **Celebration / Success** | Logros, upgrades, referidos | Success 500 + destellos controlados | Reforzar beneficio (“Listo, estamos procesando tu solicitud”) |

**Lineamientos**
- Mantén consistencia textual: define glosario de términos clave y sinónimos prohibidos.
- Usa componentes de tipografía (`.text-body-sm`, `.heading-4`) para reforzar jerarquía sin redefinir estilos.
- Documenta ejemplos de tono por canal (app, emails, notificaciones push) en el repositorio de contenido.

## Delivery Checklists

### Diseño → Desarrollo
- [ ] Tokens y estilos vinculados (Figma Variables ↔ código) actualizados.
- [ ] Estados completos documentados: hover, focus, disabled, error, loading.
- [ ] Reglas de responsive y breakpoints anotadas en el handoff.
- [ ] Accesibilidad validada (contrast, focus visible, tab order, texto alternativo).
- [ ] Motion especificado con duración/easing o marcado como “sin animación”.

### Pre-release QA
- [ ] Ejecutar pruebas automáticas (Storybook + a11y, unit tests visuales).
- [ ] Capturar referencias visuales (screenshots clave) para regresiones.
- [ ] Revisar rendimiento en dispositivos de referencia (low-end mobile, laptop).
- [ ] Validar contenido dinámico con datos reales o mocks representativos.
- [ ] Registrar hallazgos y excepciones en changelog de diseño/sistema.

---

## UX Patterns

### Pattern Heuristics

| Situación | Usa | Evita | Principios UX clave |
|-----------|-----|-------|---------------------|
| Confirmación crítica (ej. borrar registro) | Modal centrado con resumen + CTA primario | Toast auto-cierre | Mantén foco, incluye alternativa “Cancelar”, confirma con lenguaje claro |
| Flujo complejo con múltiples pasos | Drawer/panel lateral persistente | Diálogos encadenados | Mantén contexto, muestra progreso, guarda borradores parciales |
| Configuraciones densas / edición avanzada | Layout de 2 columnas + tabs o acordeones | Formularios infinitos de una sola columna | Agrupa por afinidad, usa anclajes y descripciones cortas |
| Tablas con acciones por fila | Acciones inline o menús tipo “...” con shortcuts | Botones redundantes en cada fila | Prioriza acciones más usadas, respeta foco de teclado, limita a 3 principales |
| Estados de error recurrentes | Inline + mensaje ligado al elemento | Alert genérico en top bar | Resalta campo, indica solución, evita tonos alarmistas |

**Checklist previo a seleccionar un patrón**
- ¿El usuario necesita contexto persistente? → Usa panel/drawer.
- ¿Cuántos pasos o bloques superan la pantalla? → Considera dividir en secciones o wizard.
- ¿Se afecta un dato irreversible? → Añade confirmación + plan de reversión.
- ¿El cambio necesita visibilidad global? → Usa banner/top notification con enlaces de acción.

### Empty States

```html
<div class="empty-state">
  <svg class="empty-state-icon"><!-- Icon --></svg>
  <h3 class="empty-state-title">No items found</h3>
  <p class="empty-state-description">
    Get started by creating your first item.
  </p>
  <button class="btn btn-primary">Create Item</button>
</div>
```

```css
.empty-state {
  text-align: center;
  padding: var(--space-16);
  max-width: 400px;
  margin: 0 auto;
}

.empty-state-icon {
  width: 64px;
  height: 64px;
  margin: 0 auto var(--space-6);
  color: var(--text-tertiary);
}

.empty-state-title {
  font-size: var(--text-2xl);
  font-weight: var(--font-semibold);
  color: var(--text-primary);
  margin-bottom: var(--space-3);
}

.empty-state-description {
  color: var(--text-tertiary);
  margin-bottom: var(--space-6);
}
```

### Error States

```html
<div class="error-state">
  <svg class="error-state-icon"><!-- Error Icon --></svg>
  <h3 class="error-state-title">Something went wrong</h3>
  <p class="error-state-description">
    We couldn't load the data. Please try again.
  </p>
  <div class="error-state-actions">
    <button class="btn btn-primary">Try Again</button>
    <button class="btn btn-ghost">Contact Support</button>
  </div>
</div>
```

### Loading States

```html
<!-- Skeleton Loader -->
<div class="card">
  <div class="skeleton skeleton-title"></div>
  <div class="skeleton skeleton-text"></div>
  <div class="skeleton skeleton-text"></div>
  <div class="skeleton skeleton-text" style="width: 60%;"></div>
</div>

<!-- Spinner -->
<div class="loading-state">
  <div class="spinner"></div>
  <p class="loading-text">Loading...</p>
</div>
```

### Search with Debounce

```javascript
// Efficient search with debounce
let debounceTimeout;

searchInput.addEventListener('input', (e) => {
  clearTimeout(debounceTimeout);
  
  debounceTimeout = setTimeout(() => {
    performSearch(e.target.value);
  }, 300); // 300ms debounce
});
```

### Infinite Scroll with Intersection Observer

```javascript
const observer = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      loadMoreItems();
    }
  });
}, {
  rootMargin: '100px' // Start loading 100px before reaching bottom
});

observer.observe(loadMoreTrigger);
```

---

## Implementation Guide

### Basic HTML Structure

```html
<!DOCTYPE html>
<html lang="en" data-theme="light">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Professional UI</title>
  
  <!-- Google Fonts (Optional) -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
  
  <style>
    /* Include all design system CSS here */
  </style>
</head>
<body>
  <!-- Your content -->
</body>
</html>
```

### CSS Reset (Include First)

```css
/* Modern CSS Reset */
*, *::before, *::after {
  box-sizing: border-box;
}

* {
  margin: 0;
  padding: 0;
}

html {
  font-size: 16px;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

body {
  font-family: var(--font-sans);
  font-size: var(--text-base);
  line-height: var(--leading-normal);
  color: var(--text-secondary);
  background-color: var(--bg-primary);
  min-height: 100vh;
}

img, picture, video, canvas, svg {
  display: block;
  max-width: 100%;
}

input, button, textarea, select {
  font: inherit;
}

p, h1, h2, h3, h4, h5, h6 {
  overflow-wrap: break-word;
}

ul, ol {
  list-style: none;
}

a {
  color: inherit;
  text-decoration: none;
}
```

### Performance Best Practices

```css
/* Use will-change sparingly for elements that will animate */
.animated-element {
  will-change: transform, opacity;
}

/* Remove will-change after animation */
.animated-element.animation-complete {
  will-change: auto;
}

/* Use transform and opacity for animations (GPU accelerated) */
.performant-animation {
  transition: transform 0.3s, opacity 0.3s;
}

/* Avoid animating expensive properties */
/* ❌ Bad */
.expensive-animation {
  transition: width 0.3s, height 0.3s, top 0.3s;
}

/* ✅ Good */
.efficient-animation {
  transition: transform 0.3s, opacity 0.3s;
}
```

---

## Checklist for Every Project

### Before Launch

- [ ] All interactive elements have hover, focus, active, and disabled states
- [ ] Color contrast meets WCAG 2.1 AA (4.5:1 for normal text, 3:1 for large)
- [ ] Touch targets are minimum 44x44px on mobile
- [ ] Keyboard navigation works throughout
- [ ] Focus indicators are clearly visible
- [ ] Screen reader testing completed
- [ ] Dark mode implemented (if applicable)
- [ ] Mobile responsive (tested on actual devices)
- [ ] Loading states for async operations
- [ ] Error states with helpful messages
- [ ] Empty states with clear CTAs
- [ ] Forms have proper validation and error messages
- [ ] Animations respect `prefers-reduced-motion`
- [ ] Images have alt text
- [ ] Semantic HTML used throughout
- [ ] No console errors or warnings

### Performance

- [ ] Images optimized (WebP format preferred)
- [ ] Fonts subset and optimized
- [ ] CSS minified
- [ ] JavaScript minified
- [ ] Critical CSS inlined
- [ ] Lazy loading for images below fold
- [ ] No layout shifts (CLS score)

---

## Common Mistakes to Avoid

### ❌ DON'T

1. **Multiple bright accent colors** - Stick to one primary color
2. **Generic gradients** - Especially blue/purple  
3. **Heavy shadows** - Keep them subtle and purposeful
4. **Text below 16px** - Readability suffers on mobile
5. **Black (#000) for text** - Too harsh; use dark gray
6. **Missing interactive states** - Every clickable needs feedback
7. **Ignore accessibility** - It's not optional
8. **Fixed pixel widths** - Use responsive units
9. **Skip empty/error states** - Users need guidance
10. **Animate expensive properties** - Stick to transform/opacity

### ✅ DO

1. **Systematic spacing** - Follow the 8px grid religiously
2. **Clear hierarchy** - Size, weight, and color denote importance
3. **Generous white space** - Let content breathe
4. **Test on real devices** - Simulators aren't enough
5. **Provide feedback** - Loading states, success messages
6. **Use semantic HTML** - Correct tags improve accessibility
7. **Optimize performance** - Fast sites feel better
8. **Progressive enhancement** - Start simple, enhance for capable devices
9. **Document components** - Future you will thank present you
10. **Iterate based on feedback** - Design is never truly "done"

---

## Quick Reference: Common Patterns

### Hero Section
```html
<section class="section section-lg bg-primary">
  <div class="container">
    <div class="grid grid-cols-1 lg:grid-cols-2 gap-12 items-center">
      <div>
        <h1 class="display-1 mb-6">Professional Design System</h1>
        <p class="text-body-lg text-secondary mb-8">
          Build exceptional interfaces with our comprehensive design system.
        </p>
        <div class="flex gap-4">
          <button class="btn btn-primary btn-lg">Get Started</button>
          <button class="btn btn-secondary btn-lg">Learn More</button>
        </div>
      </div>
      <div>
        <!-- Image or illustration -->
      </div>
    </div>
  </div>
</section>
```

### Feature Grid
```html
<section class="section">
  <div class="container">
    <h2 class="heading-2 text-center mb-12">Features</h2>
    <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
      <div class="card card-bordered text-center">
        <svg class="mx-auto mb-4"><!-- Icon --></svg>
        <h3 class="heading-4 mb-3">Fast</h3>
        <p class="text-body-sm text-tertiary">
          Lightning-fast performance out of the box.
        </p>
      </div>
      <!-- More cards... -->
    </div>
  </div>
</section>
```

### Pricing Table
```html
<section class="section bg-secondary">
  <div class="container">
    <h2 class="heading-2 text-center mb-12">Simple Pricing</h2>
    <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
      <div class="card card-elevated">
        <div class="text-label mb-2">Starter</div>
        <div class="mb-6">
          <span class="display-2">$29</span>
          <span class="text-tertiary">/month</span>
        </div>
        <ul class="space-y-3 mb-8">
          <li class="flex items-center gap-2">
            <svg><!-- Checkmark --></svg>
            <span>Feature 1</span>
          </li>
          <!-- More features... -->
        </ul>
        <button class="btn btn-primary w-full">Get Started</button>
      </div>
      <!-- More pricing tiers... -->
    </div>
  </div>
</section>
```

---

## Conclusion

This design system provides everything needed to create professional, accessible, and performant user interfaces. Remember:

1. **Consistency is key** - Use the design tokens everywhere
2. **Accessibility is mandatory** - Not an afterthought
3. **Performance matters** - Fast UIs feel better
4. **Test thoroughly** - Real devices, real users
5. **Iterate continuously** - Design systems evolve

The best design system is one that's actually used. Start with the basics, customize as needed, and always prioritize user experience over visual flair.
