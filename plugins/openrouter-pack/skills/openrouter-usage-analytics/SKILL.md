---
name: openrouter-usage-analytics
description: |
  Track and analyze OpenRouter API usage patterns. Use when optimizing costs or understanding usage trends. Trigger with phrases like 'openrouter analytics', 'openrouter usage', 'openrouter metrics', 'track openrouter'.
allowed-tools: Read, Write, Edit, Grep
version: 1.0.0
license: MIT
author: Jeremy Longshore <jeremy@intentsolutions.io>
compatible-with: claude-code, codex, openclaw
---
# Openrouter Usage Analytics

## Overview

This skill demonstrates building usage analytics for OpenRouter to track costs, token usage, model popularity, and performance metrics over time.

## Prerequisites

- OpenRouter integration with logging
- Data storage for metrics (database, time-series DB, or analytics service)

## Instructions

1. **Instrument API calls**: Add middleware that captures timestamp, model, prompt/completion token counts, cost, latency, and status for every request
2. **Store metrics efficiently**: Write metrics to a time-series database (InfluxDB, TimescaleDB) or append-only table with proper indexing on timestamp and model
3. **Build aggregation queries**: Create queries for daily/weekly cost by model, average latency trends, token usage distribution, and error rates
4. **Create a dashboard**: Visualize key metrics — total spend over time, cost per model, average latency, requests per hour, and error rate trends
5. **Set up automated reports**: Schedule daily or weekly summary emails/alerts with top-line metrics and any anomalies detected

## Output

- Analytics pipeline capturing cost, latency, and usage per request
- Dashboard with charts for spend, token usage, model distribution, and errors
- Automated weekly report summarizing key usage trends and anomalies

## Error Handling

| Error | Cause | Fix |
|-------|-------|-----|
| Missing metrics for some requests | Instrumentation middleware not covering all paths | Centralize all API calls through a single instrumented client |
| Metric storage growing too fast | High request volume with verbose logging | Aggregate metrics hourly/daily; keep raw data only for recent period |
| Dashboard showing stale data | Query or aggregation pipeline lagging | Check pipeline health; add alerting on data freshness |

See `${CLAUDE_SKILL_DIR}/references/errors.md` for full error reference.

## Examples

See `${CLAUDE_SKILL_DIR}/references/examples.md` for runnable code samples.

## Resources

- [OpenRouter Documentation](https://openrouter.ai/docs)
- [OpenRouter Models](https://openrouter.ai/models)
- [OpenRouter API Reference](https://openrouter.ai/docs/api-reference)
- [OpenRouter Status](https://status.openrouter.ai)
