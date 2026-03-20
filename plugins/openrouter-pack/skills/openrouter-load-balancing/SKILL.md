---
name: openrouter-load-balancing
description: |
  Distribute OpenRouter requests for high availability. Use when building scalable systems that need load distribution. Trigger with phrases like 'openrouter load balance', 'distribute requests', 'openrouter scaling', 'high availability'.
allowed-tools: Read, Write, Edit, Grep
version: 1.0.0
license: MIT
author: Jeremy Longshore <jeremy@intentsolutions.io>
compatible-with: claude-code, codex, openclaw
---
# Openrouter Load Balancing

## Overview

This skill covers strategies for distributing API requests across multiple keys, models, or instances for improved throughput and reliability.

## Prerequisites

- OpenRouter integration
- Multiple API keys or model options (for distribution)

## Instructions

1. **Use multiple API keys**: Create separate API keys for different services or teams; distribute requests across keys to multiply your rate limits
2. **Implement round-robin distribution**: Cycle through API keys or equivalent models on each request to spread load evenly
3. **Add health-based routing**: Track error rates and latency per key/model; route traffic away from unhealthy endpoints automatically
4. **Monitor per-key usage**: Track request counts and costs per API key to ensure balanced utilization and catch anomalies
5. **Implement circuit breakers**: When a key or model exceeds error thresholds, temporarily remove it from the pool and re-check after a cooldown period

## Output

- Load balancer distributing requests across multiple API keys or models
- Health dashboard showing per-key error rates and latency
- Automatic failover when individual keys or models become unhealthy

## Error Handling

| Error | Cause | Fix |
|-------|-------|-----|
| Uneven load distribution | Round-robin not accounting for request duration | Use weighted distribution based on current in-flight requests |
| All keys rate-limited | Traffic spike exceeded aggregate limits | Add more keys or implement request queuing with backpressure |
| Health check false positive | Transient errors marking a key as unhealthy | Use sliding window error rates (e.g., 5 errors in 60s) instead of single-error triggers |

See `${CLAUDE_SKILL_DIR}/references/errors.md` for full error reference.

## Examples

See `${CLAUDE_SKILL_DIR}/references/examples.md` for runnable code samples.

## Resources

- [OpenRouter Documentation](https://openrouter.ai/docs)
- [OpenRouter Models](https://openrouter.ai/models)
- [OpenRouter API Reference](https://openrouter.ai/docs/api-reference)
- [OpenRouter Status](https://status.openrouter.ai)
