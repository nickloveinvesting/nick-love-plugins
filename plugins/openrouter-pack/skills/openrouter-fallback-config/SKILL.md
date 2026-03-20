---
name: openrouter-fallback-config
description: |
  Configure model fallback chains for reliability. Use when building resilient systems that need high availability. Trigger with phrases like 'openrouter fallback', 'model fallback', 'openrouter backup model', 'failover config'.
allowed-tools: Read, Write, Edit, Grep
version: 1.0.0
license: MIT
author: Jeremy Longshore <jeremy@intentsolutions.io>
compatible-with: claude-code, codex, openclaw
---
# Openrouter Fallback Config

## Overview

This skill shows how to configure fallback model chains so requests automatically retry with alternative models when the primary model is unavailable or errors.

## Prerequisites

- OpenRouter integration
- Multiple models identified as primary and fallback options

## Instructions

1. **Use OpenRouter's native fallback**: Pass an array of model IDs in the `models` field (instead of `model`) — OpenRouter will try each in order until one succeeds
2. **Set per-model parameters**: Use the `route` field with `"fallback"` strategy to let OpenRouter handle failover automatically
3. **Implement client-side fallback**: For more control, catch 5xx or timeout errors and retry with the next model in your own fallback list
4. **Configure timeout thresholds**: Set `request_timeout` per attempt so slow models fail fast and the fallback triggers quickly
5. **Test the chain**: Temporarily use an invalid model ID as primary to verify your fallback chain activates correctly

## Output

- A fallback chain that transparently retries with alternative models
- Reduced downtime when individual models or providers have outages
- Logs showing which model ultimately served each request

## Error Handling

| Error | Cause | Fix |
|-------|-------|-----|
| All fallbacks exhausted | Every model in the chain failed | Add more diverse fallbacks across providers; alert on full chain failure |
| Slow cascading retries | Each model timing out sequentially | Reduce per-model timeout to 10-15 seconds; use parallel fallback instead |
| Inconsistent responses | Different models in the chain have different capabilities | Ensure all fallback models support the features your prompt uses (e.g., tool calling) |

See `${CLAUDE_SKILL_DIR}/references/errors.md` for full error reference.

## Examples

See `${CLAUDE_SKILL_DIR}/references/examples.md` for runnable code samples.

## Resources

- [OpenRouter Documentation](https://openrouter.ai/docs)
- [OpenRouter Models](https://openrouter.ai/models)
- [OpenRouter API Reference](https://openrouter.ai/docs/api-reference)
- [OpenRouter Status](https://status.openrouter.ai)
