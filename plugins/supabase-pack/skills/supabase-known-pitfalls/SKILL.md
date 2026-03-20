---
name: supabase-known-pitfalls
description: |
  Execute identify and avoid Supabase anti-patterns and common integration mistakes.
  Use when reviewing Supabase code for issues, onboarding new developers,
  or auditing existing Supabase integrations for best practices violations.
  Trigger with phrases like "supabase mistakes", "supabase anti-patterns",
  "supabase pitfalls", "supabase what not to do", "supabase code review".
allowed-tools: Read, Grep
version: 1.0.0
license: MIT
author: Jeremy Longshore <jeremy@intentsolutions.io>
compatible-with: claude-code, codex, openclaw
---
# Supabase Known Pitfalls

## Prerequisites
- Access to Supabase codebase for review
- Understanding of async/await patterns
- Knowledge of security best practices
- Familiarity with rate limiting concepts

## Instructions

Supabase anti-patterns typically cluster into three risk categories: security risks (exposing service role keys, missing RLS policies, over-privileged anon access), performance risks (N+1 queries, missing indexes, fetching more columns than needed), and reliability risks (no retry logic, synchronous auth checks in every request, missing error handling). Addressing security issues first prevents data exposure, while performance fixes have the greatest impact on user experience.

### Step 1: Review for Anti-Patterns
Scan the codebase for each pitfall pattern listed in the references. Use grep or a code search tool to find all locations where Supabase client calls are made. Look specifically for service role key usage in client-side code, missing `.select()` column lists that fetch entire rows, and `await` chains that make multiple sequential queries where a single join would suffice.

### Step 2: Prioritize Fixes
Address security issues first: any client-side exposure of the service role key or missing RLS policies on tables containing user data are critical. Then tackle performance issues that affect P95 latency. Finally, address reliability gaps like missing error handling.

### Step 3: Implement Better Approach
Replace anti-patterns with recommended patterns. Document the change in a PR description so reviewers understand why the old approach was problematic.

### Step 4: Add Prevention
Set up linting and CI checks to prevent recurrence. Add ESLint rules that flag service key usage in frontend bundles and require `.select()` calls to specify columns explicitly.

## Output
- Anti-patterns identified with severity classification
- Security, performance, and reliability fixes implemented
- ESLint and CI prevention measures active
- Code quality measurably improved with documented rationale

## Error Handling

See `${CLAUDE_SKILL_DIR}/references/errors.md` for comprehensive error handling.

## Examples

See `${CLAUDE_SKILL_DIR}/references/examples.md` for detailed examples.

## Resources
- [Supabase Security Guide](https://supabase.com/docs/security)
- [Supabase Best Practices](https://supabase.com/docs/best-practices)

## Overview

Execute identify and avoid Supabase anti-patterns and common integration mistakes.