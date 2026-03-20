---
name: supabase-policy-guardrails
description: |
  Implement Supabase lint rules, policy enforcement, and automated guardrails.
  Use when setting up code quality rules for Supabase integrations, implementing
  pre-commit hooks, or configuring CI policy checks for Supabase best practices.
  Trigger with phrases like "supabase policy", "supabase lint",
  "supabase guardrails", "supabase best practices check", "supabase eslint".
allowed-tools: Read, Write, Edit, Bash(npx:*)
version: 1.0.0
license: MIT
author: Jeremy Longshore <jeremy@intentsolutions.io>
compatible-with: claude-code, codex, openclaw
---
# Supabase Policy Guardrails

## Prerequisites
- ESLint configured in project
- Pre-commit hooks infrastructure
- CI/CD pipeline with policy checks
- TypeScript for type enforcement

## Instructions

Policy guardrails for Supabase work best as a defense-in-depth system where violations are caught at the earliest possible stage: lint rules catch issues at code authoring time, pre-commit hooks catch issues before they enter the repository, CI checks enforce policy on every pull request, and runtime guardrails prevent dangerous operations from executing in production even if earlier checks were bypassed.

### Step 1: Create ESLint Rules
Implement custom lint rules that flag Supabase-specific anti-patterns: using the service role key in files under `src/`, calling `.select()` without specifying column names, and making Supabase queries outside the designated service layer. Rules should provide actionable error messages that explain the problem and suggest the correct alternative.

### Step 2: Configure Pre-Commit Hooks
Set up hooks using Husky or a similar tool to scan staged files for hardcoded Supabase keys or connection strings before they enter the commit history. Once a secret is committed, rotation is the only safe remediation, so catching it pre-commit is far less disruptive than discovering it post-push.

### Step 3: Add CI Policy Checks
Implement policy-as-code checks in CI that verify RLS is enabled on all non-public tables and that migration files do not contain data-destructive statements without explicit approval annotations.

### Step 4: Enable Runtime Guardrails
Add production safeguards that block bulk-delete operations on tables above a certain row threshold unless a `--force` flag is explicitly passed, preventing accidental mass deletions.

## Output
- ESLint plugin with Supabase-specific rules active in the editor and CI
- Pre-commit hooks blocking secrets from entering the repository
- CI policy checks enforcing RLS and migration safety standards
- Runtime guardrails preventing accidental bulk-destructive operations

## Error Handling

See `${CLAUDE_SKILL_DIR}/references/errors.md` for comprehensive error handling.

## Examples

See `${CLAUDE_SKILL_DIR}/references/examples.md` for detailed examples.

## Resources
- [ESLint Plugin Development](https://eslint.org/docs/latest/extend/plugins)
- [Pre-commit Framework](https://pre-commit.com/)
- [Open Policy Agent](https://www.openpolicyagent.org/)

## Overview

Implement Supabase lint rules, policy enforcement, and automated guardrails.