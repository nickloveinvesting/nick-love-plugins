---
name: openrouter-cost-controls
description: |
  Implement cost control mechanisms for OpenRouter usage. Use when managing budgets or preventing overspend. Trigger with phrases like 'openrouter budget', 'openrouter spending limit', 'cost control', 'openrouter limit spend'.
allowed-tools: Read, Write, Edit, Grep
version: 1.0.0
license: MIT
author: Jeremy Longshore <jeremy@intentsolutions.io>
compatible-with: claude-code, codex, openclaw
---
# Openrouter Cost Controls

## Overview

This skill demonstrates setting up spending limits, per-request budgets, and automated cost monitoring to prevent unexpected charges.

## Prerequisites

- OpenRouter account with credit management access
- Understanding of model pricing tiers

## Instructions

1. **Set account-level limits**: Configure spending limits in the OpenRouter dashboard under Settings > Limits to cap total monthly spend
2. **Use per-request max_tokens**: Always set `max_tokens` in every request to cap completion length and prevent runaway costs
3. **Track costs per request**: Read the `usage` field in each response and multiply by model pricing to track cumulative spend in your application
4. **Implement budget middleware**: Create a middleware that checks cumulative spend before each request and rejects requests that would exceed the budget
5. **Set up alerts**: Query `/api/v1/auth/key` periodically to check remaining credits and alert when balance drops below a threshold

## Output

- Per-request cost tracking integrated into your application
- Budget enforcement middleware that blocks requests over the limit
- Automated alerts when spending approaches configured thresholds

## Error Handling

| Error | Cause | Fix |
|-------|-------|-----|
| 402 Payment Required | Account credits exhausted | Top up credits or switch to free models |
| Budget exceeded locally | Middleware blocked the request | Increase budget limit or optimize prompts to reduce token usage |
| Inaccurate cost tracking | Using stale pricing data | Refresh model pricing from `/models` endpoint daily |

See `${CLAUDE_SKILL_DIR}/references/errors.md` for full error reference.

## Examples

See `${CLAUDE_SKILL_DIR}/references/examples.md` for runnable code samples.

## Resources

- [OpenRouter Documentation](https://openrouter.ai/docs)
- [OpenRouter Models](https://openrouter.ai/models)
- [OpenRouter API Reference](https://openrouter.ai/docs/api-reference)
- [OpenRouter Status](https://status.openrouter.ai)
