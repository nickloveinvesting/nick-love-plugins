---
name: openrouter-model-availability
description: |
  Monitor model availability and implement health checks. Use when building reliable systems that depend on specific models. Trigger with phrases like 'openrouter model status', 'model availability', 'openrouter health check', 'is model available'.
allowed-tools: Read, Write, Edit, Grep
version: 1.0.0
license: MIT
author: Jeremy Longshore <jeremy@intentsolutions.io>
compatible-with: claude-code, codex, openclaw
---
# Openrouter Model Availability

## Overview

This skill covers monitoring model availability on OpenRouter, implementing health checks, and handling model downtime gracefully.

## Prerequisites

- OpenRouter integration
- List of models your application depends on

## Instructions

1. **Query model status**: Periodically call `GET /api/v1/models` and check if your required models are present; absent models are unavailable
2. **Implement health probes**: Send lightweight test requests (short prompt, `max_tokens: 1`) to each critical model on a schedule to verify end-to-end availability
3. **Track availability metrics**: Log probe results and calculate uptime percentages per model; detect patterns (e.g., models that go down at certain times)
4. **Set up alerts**: Trigger notifications when a critical model fails health checks or disappears from the models list
5. **Automate failover**: When a health check fails, automatically switch to a pre-configured fallback model and log the failover event

## Output

- Health check service that probes critical models on a regular schedule
- Availability dashboard showing uptime percentage per model
- Automated failover that activates when models become unavailable

## Error Handling

| Error | Cause | Fix |
|-------|-------|-----|
| Health check timeout | Model is slow or overloaded | Increase probe timeout to 30s; distinguish between "slow" and "down" |
| False positive alerts | Transient network issues triggering alerts | Require 2-3 consecutive failures before alerting; add probe from multiple locations |
| Model removed from catalog | Provider discontinued the model | Subscribe to OpenRouter changelogs; implement model ID aliasing for easy migration |

See `${CLAUDE_SKILL_DIR}/references/errors.md` for full error reference.

## Examples

See `${CLAUDE_SKILL_DIR}/references/examples.md` for runnable code samples.

## Resources

- [OpenRouter Documentation](https://openrouter.ai/docs)
- [OpenRouter Models](https://openrouter.ai/models)
- [OpenRouter API Reference](https://openrouter.ai/docs/api-reference)
- [OpenRouter Status](https://status.openrouter.ai)
