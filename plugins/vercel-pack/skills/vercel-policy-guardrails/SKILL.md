---
name: vercel-policy-guardrails
description: |
  Implement Vercel lint rules, policy enforcement, and automated guardrails.
  Use when setting up code quality rules for Vercel integrations, implementing
  pre-commit hooks, or configuring CI policy checks for Vercel best practices.
  Trigger with phrases like "vercel policy", "vercel lint",
  "vercel guardrails", "vercel best practices check", "vercel eslint".
allowed-tools: Read, Write, Edit, Bash(npx:*)
version: 1.0.0
license: MIT
author: Jeremy Longshore <jeremy@intentsolutions.io>
compatible-with: claude-code, codex, openclaw
---
# Vercel Policy Guardrails

## Prerequisites
- ESLint configured in project
- Pre-commit hooks infrastructure
- CI/CD pipeline with policy checks
- TypeScript for type enforcement

## Instructions

Policy guardrails for Vercel deployments protect against the most common failure modes: accidental secret exposure in client bundles, deployment to wrong environments, incompatible edge runtime API usage, and runaway serverless function costs. Implementing guardrails at multiple enforcement points (lint, pre-commit, CI, and runtime) ensures that issues are caught as early as possible in the development lifecycle rather than discovered in production.

### Step 1: Create ESLint Rules
Implement custom lint rules that flag Vercel-specific anti-patterns: using `process.env` variables prefixed with `NEXT_PUBLIC_` for secrets (which exposes them in the client bundle), importing Node.js-only modules in files with `export const runtime = 'edge'`, and omitting explicit region configuration for latency-sensitive edge functions. Rules should provide error messages that clearly state what is wrong and suggest the correct approach.

### Step 2: Configure Pre-Commit Hooks
Set up pre-commit hooks that scan staged files for Vercel project IDs, deployment tokens, or other credentials that should not enter version control. Pair with a `.env.example` file that documents required variables without values so contributors know what to configure without copying secrets.

### Step 3: Add CI Policy Checks
Implement CI checks that validate the Vercel configuration file (`vercel.json`) schema, confirm that all environment variables referenced in code are declared in your deployment configuration, and run bundle size analysis to alert when the JavaScript bundle crosses your performance budget thresholds.

### Step 4: Enable Runtime Guardrails
Add middleware that enforces authentication on all routes matching your protected path patterns, with a fallback to a clear error page for unauthenticated requests rather than a broken UI state.

## Output
- ESLint rules detecting secret exposure and edge runtime incompatibilities
- Pre-commit hooks preventing credentials from entering version control
- CI checks validating configuration schema and bundle size budgets
- Middleware enforcing authentication on all protected routes

## Error Handling

See `${CLAUDE_SKILL_DIR}/references/errors.md` for comprehensive error handling.

## Examples

See `${CLAUDE_SKILL_DIR}/references/examples.md` for detailed examples.

## Resources
- [ESLint Plugin Development](https://eslint.org/docs/latest/extend/plugins)
- [Pre-commit Framework](https://pre-commit.com/)
- [Open Policy Agent](https://www.openpolicyagent.org/)

## Overview

Implement Vercel lint rules, policy enforcement, and automated guardrails.