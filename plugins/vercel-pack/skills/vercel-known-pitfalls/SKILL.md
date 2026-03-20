---
name: vercel-known-pitfalls
description: |
  Execute identify and avoid Vercel anti-patterns and common integration mistakes.
  Use when reviewing Vercel code for issues, onboarding new developers,
  or auditing existing Vercel integrations for best practices violations.
  Trigger with phrases like "vercel mistakes", "vercel anti-patterns",
  "vercel pitfalls", "vercel what not to do", "vercel code review".
allowed-tools: Read, Grep
version: 1.0.0
license: MIT
author: Jeremy Longshore <jeremy@intentsolutions.io>
compatible-with: claude-code, codex, openclaw
---
# Vercel Known Pitfalls

## Prerequisites
- Access to Vercel codebase for review
- Understanding of async/await patterns
- Knowledge of security best practices
- Familiarity with rate limiting concepts

## Instructions

Vercel anti-patterns cluster around three areas: configuration mistakes (hardcoded secrets in code instead of environment variables, wrong output directory settings, ignoring build cache directives), serverless function mistakes (performing expensive work outside the handler instead of warming it lazily, not handling cold starts, setting unrealistic timeout limits), and edge runtime mistakes (using Node.js-only APIs that are not available in the edge runtime). Addressing these systematically reduces deployment failures and cold-start latency.

### Step 1: Review for Anti-Patterns
Scan the codebase for each pitfall pattern. Look for environment-specific URLs or API keys hardcoded in source files rather than referenced via `process.env`. Check serverless function files for module-level initialization of heavy objects like database connection pools, which bloats cold-start time. Audit any files using the `export const runtime = 'edge'` directive for incompatible Node.js API usage.

### Step 2: Prioritize Fixes
Address security issues first: any hardcoded secrets must be rotated and moved to environment variables immediately. Then fix cold-start performance issues since they directly impact user experience on first load. Finally, address configuration issues that cause intermittent build failures.

### Step 3: Implement Better Approach
Replace anti-patterns with recommended patterns. Move all secrets to Vercel environment variables, initialize heavy resources lazily inside handler functions, and use the `@vercel/edge` compatible API surface in edge runtime files.

### Step 4: Add Prevention
Set up ESLint rules that flag hardcoded URL patterns matching your environments and add a CI step that validates edge runtime compatibility before deployment.

## Output
- Anti-patterns identified and classified by severity
- Security, performance, and configuration fixes implemented
- ESLint and CI prevention measures blocking future regressions
- Code quality improved with documented rationale for each change

## Error Handling

See `${CLAUDE_SKILL_DIR}/references/errors.md` for comprehensive error handling.

## Examples

See `${CLAUDE_SKILL_DIR}/references/examples.md` for detailed examples.

## Resources
- [Vercel Security Guide](https://vercel.com/docs/security)
- [Vercel Best Practices](https://vercel.com/docs/best-practices)

## Overview

Execute identify and avoid Vercel anti-patterns and common integration mistakes.