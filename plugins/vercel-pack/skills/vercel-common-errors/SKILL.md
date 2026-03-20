---
name: vercel-common-errors
description: |
  Execute diagnose and fix Vercel common errors and exceptions.
  Use when encountering Vercel errors, debugging failed requests,
  or troubleshooting integration issues.
  Trigger with phrases like "vercel error", "fix vercel",
  "vercel not working", "debug vercel".
allowed-tools: Read, Grep, Bash(curl:*)
version: 1.0.0
license: MIT
author: Jeremy Longshore <jeremy@intentsolutions.io>
compatible-with: claude-code, codex, openclaw
---
# Vercel Common Errors

## Prerequisites
- Vercel SDK installed
- API credentials configured
- Access to error logs

## Instructions

Vercel errors typically originate from one of three layers: the build pipeline (configuration errors, dependency failures), the serverless function runtime (timeouts, memory limits, environment variable issues), or the edge network (routing mismatches, header size limits). Identifying which layer is responsible saves significant debugging time before you start making changes.

### Step 1: Identify the Error
Check the error message and code in your Vercel deployment logs or function logs. Build errors appear in the deployment log with exit codes and compilation output. Runtime errors appear in the function log with request context. Note the HTTP status code if the error came from a deployed function — 504 typically means a function timeout, 413 means a request payload exceeded Vercel's size limit, and 500 means an uncaught exception in your function code.

### Step 2: Find Matching Error Below
Match your error to one of the documented cases in the references file. Distinguish between errors that occur on every request (deterministic, require a code fix) and errors that occur intermittently (potentially cold-start related or caused by external service degradation). Deterministic errors should be fixed before promoting to production; intermittent errors may require retry logic or graceful degradation.

### Step 3: Apply Solution
Follow the solution steps for your specific error. After applying a fix, trigger a new deployment and test the affected endpoint or route. If the error was related to environment variables, verify the variable is present in both preview and production environments in the Vercel dashboard.

## Output
- Identified error cause and the layer (build, runtime, or edge network) where it originated
- Applied fix with verification via a new deployment
- Environment variable or configuration change confirmed in all required environments

## Error Handling

See `${CLAUDE_SKILL_DIR}/references/errors.md` for comprehensive error handling.

## Examples

See `${CLAUDE_SKILL_DIR}/references/examples.md` for detailed examples.

## Resources
- [Vercel Status Page](https://www.vercel-status.com)
- [Vercel Support](https://vercel.com/docs/support)
- [Vercel Error Codes](https://vercel.com/docs/errors)

## Overview

Execute diagnose and fix Vercel common errors and exceptions.