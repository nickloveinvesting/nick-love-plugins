---
name: supabase-common-errors
description: |
  Execute diagnose and fix Supabase common errors and exceptions.
  Use when encountering Supabase errors, debugging failed requests,
  or troubleshooting integration issues.
  Trigger with phrases like "supabase error", "fix supabase",
  "supabase not working", "debug supabase".
allowed-tools: Read, Grep, Bash(curl:*)
version: 1.0.0
license: MIT
author: Jeremy Longshore <jeremy@intentsolutions.io>
compatible-with: claude-code, codex, openclaw
---
# Supabase Common Errors

## Prerequisites
- Supabase SDK installed
- API credentials configured
- Access to error logs

## Instructions

Supabase errors typically originate from one of three layers: the PostgREST API layer (HTTP 4xx/5xx responses), the Supabase client SDK (JavaScript exceptions), or the underlying PostgreSQL database (constraint violations, permission denials). Identifying which layer the error comes from narrows your troubleshooting path significantly before you start making changes.

### Step 1: Identify the Error
Check error message and code in your logs or console. Note the HTTP status code if the error came from a network request — 401 means authentication failed, 403 means row-level security denied the operation, 409 means a uniqueness constraint was violated, and 500 means the database query itself failed. For SDK errors, check the `error.message` and `error.code` properties on the returned error object.

### Step 2: Find Matching Error Below
Match your error to one of the documented cases in the references file. Pay attention to whether the error is transient (network timeout, temporary overload) or deterministic (bad credentials, schema mismatch). Transient errors warrant a retry strategy; deterministic errors require a code or configuration fix.

### Step 3: Apply Solution
Follow the solution steps for your specific error. After applying a fix, test the exact operation that failed to confirm resolution before closing the issue. If the error recurs intermittently, add structured logging around the Supabase call to capture the full error context for the next occurrence.

## Output
- Identified error cause and the layer (API, SDK, or database) where it originated
- Applied fix with verification that the operation now succeeds
- Structured logging added for intermittent errors to aid future diagnosis

## Error Handling

See `${CLAUDE_SKILL_DIR}/references/errors.md` for comprehensive error handling.

## Examples

See `${CLAUDE_SKILL_DIR}/references/examples.md` for detailed examples.

## Resources
- [Supabase Status Page](https://status.supabase.com)
- [Supabase Support](https://supabase.com/docs/support)
- [Supabase Error Codes](https://supabase.com/docs/errors)

## Overview

Execute diagnose and fix Supabase common errors and exceptions.