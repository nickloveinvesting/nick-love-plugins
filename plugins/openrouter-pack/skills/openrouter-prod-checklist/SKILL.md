---
name: openrouter-prod-checklist
description: |
  Validate production readiness of your OpenRouter integration. Use before deploying to production. Trigger with phrases like 'openrouter production', 'openrouter launch checklist', 'production ready', 'openrouter deploy'.
allowed-tools: Read, Write, Edit, Grep
version: 1.0.0
license: MIT
author: Jeremy Longshore <jeremy@intentsolutions.io>
compatible-with: claude-code, codex, openclaw
---
# Openrouter Prod Checklist

## Overview

This skill provides a comprehensive production readiness checklist covering security, reliability, observability, and cost management for OpenRouter deployments.

## Prerequisites

- Working OpenRouter integration in staging/development
- Production infrastructure ready

## Instructions

1. **Security review**: Verify API keys are in a secrets manager (not env files on disk), HTTPS is enforced, and no sensitive data leaks into logs
2. **Reliability setup**: Configure fallback models, retry logic with exponential backoff, circuit breakers, and request timeouts for every API call
3. **Observability**: Set up structured logging for every API call (request ID, model, latency, tokens, cost), alerting on error rate spikes, and a monitoring dashboard
4. **Cost controls**: Set account spending limits in the OpenRouter dashboard, implement per-request `max_tokens`, and deploy budget enforcement middleware
5. **Load testing**: Run load tests at 2x expected peak traffic to verify rate limits, latency under load, and fallback behavior; document capacity limits

## Output

- Production readiness checklist with pass/fail for each category
- Monitoring dashboard with key metrics (latency, error rate, cost, token usage)
- Documented runbooks for common failure scenarios (rate limiting, provider outages, credit exhaustion)

## Error Handling

| Error | Cause | Fix |
|-------|-------|-----|
| Production key exposed | Key logged or committed to source | Rotate immediately; deploy from secrets manager; add secret scanning |
| No fallback configured | Primary model goes down in production | Add at least one fallback model before launch; test failover |
| Missing monitoring | Errors go undetected | Set up alerting on 4xx/5xx rates and latency P95 before launch |

See `${CLAUDE_SKILL_DIR}/references/errors.md` for full error reference.

## Examples

See `${CLAUDE_SKILL_DIR}/references/examples.md` for runnable code samples.

## Resources

- [OpenRouter Documentation](https://openrouter.ai/docs)
- [OpenRouter Models](https://openrouter.ai/models)
- [OpenRouter API Reference](https://openrouter.ai/docs/api-reference)
- [OpenRouter Status](https://status.openrouter.ai)
