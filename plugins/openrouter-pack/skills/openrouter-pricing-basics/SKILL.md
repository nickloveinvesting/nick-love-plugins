---
name: openrouter-pricing-basics
description: |
  Understand OpenRouter model pricing tiers and cost calculation. Use when budgeting or comparing model costs. Trigger with phrases like 'openrouter pricing', 'openrouter cost', 'model pricing', 'openrouter budget'.
allowed-tools: Read, Write, Edit, Grep
version: 1.0.0
license: MIT
author: Jeremy Longshore <jeremy@intentsolutions.io>
compatible-with: claude-code, codex, openclaw
---
# Openrouter Pricing Basics

## Overview

This skill explains OpenRouter's per-token pricing model, how to calculate costs for different models, and strategies for staying within budget.

## Prerequisites

- OpenRouter account with credits
- Understanding of token concepts (prompt vs completion tokens)

## Instructions

1. **Understand the pricing model**: OpenRouter charges per token with separate rates for prompt (input) and completion (output) tokens, listed as price per 1M tokens
2. **Query model pricing**: Use the `/models` endpoint and inspect `pricing.prompt` and `pricing.completion` fields for each model
3. **Estimate request costs**: Calculate cost as `(prompt_tokens * prompt_price + completion_tokens * completion_price)` using the `usage` object from each response
4. **Track cumulative spend**: Use the `X-OpenRouter-Cost` response header or query `/api/v1/auth/key` to check remaining credits
5. **Optimize costs**: Use cheaper models for simple tasks (e.g., `google/gemma-2-9b-it:free`) and reserve expensive models for complex reasoning

## Output

- Cost-per-request calculations for your chosen models
- Credit balance and usage tracking setup
- Model pricing comparison table sorted by cost

## Error Handling

| Error | Cause | Fix |
|-------|-------|-----|
| 402 Payment Required | Insufficient credits for the chosen model | Top up credits or switch to a cheaper/free model |
| Unexpected costs | Completion tokens exceeded max_tokens | Always set `max_tokens` to cap output length |
| Price mismatch | Using outdated pricing data | Re-query `/models` endpoint; pricing updates dynamically |

See `${CLAUDE_SKILL_DIR}/references/errors.md` for full error reference.

## Examples

See `${CLAUDE_SKILL_DIR}/references/examples.md` for runnable code samples.

## Resources

- [OpenRouter Documentation](https://openrouter.ai/docs)
- [OpenRouter Models](https://openrouter.ai/models)
- [OpenRouter API Reference](https://openrouter.ai/docs/api-reference)
- [OpenRouter Status](https://status.openrouter.ai)
