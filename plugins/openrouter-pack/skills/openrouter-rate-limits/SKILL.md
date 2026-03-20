---
name: openrouter-rate-limits
description: |
  Understand and handle OpenRouter rate limits effectively. Use when building high-throughput systems. Trigger with phrases like 'openrouter rate limit', 'openrouter 429', 'openrouter throttle', 'request limits'.
allowed-tools: Read, Write, Edit, Grep
version: 1.0.0
license: MIT
author: Jeremy Longshore <jeremy@intentsolutions.io>
compatible-with: claude-code, codex, openclaw
---
# Openrouter Rate Limits

## Overview

This skill covers OpenRouter's rate limiting behavior, how to read rate limit headers, and implementing retry strategies that respect limits.

## Prerequisites

- OpenRouter integration
- Understanding of HTTP 429 status codes and retry-after semantics

## Instructions

1. **Read rate limit headers**: Inspect `X-RateLimit-Limit`, `X-RateLimit-Remaining`, and `X-RateLimit-Reset` from each response to know your current limits
2. **Implement exponential backoff**: On 429 responses, wait `2^attempt * base_delay` seconds before retrying, with jitter to prevent thundering herd
3. **Pre-check remaining quota**: Before sending a batch of requests, check `X-RateLimit-Remaining` and pace requests to stay under the limit
4. **Use a token bucket or leaky bucket**: Implement client-side rate limiting to smooth request bursts and avoid hitting server limits
5. **Handle per-model limits**: Different models may have different rate limits; track limits per model ID separately

## Output

- Automatic retry logic that handles 429 responses gracefully
- Client-side rate limiter that prevents hitting server limits
- Dashboard or log output showing rate limit utilization over time

## Error Handling

| Error | Cause | Fix |
|-------|-------|-----|
| 429 Too Many Requests | Exceeded requests-per-minute or tokens-per-minute limit | Use exponential backoff with jitter; respect `Retry-After` header |
| Retry storm | Multiple clients retrying simultaneously | Add random jitter (0-1s) to each retry delay |
| Silent throttling | Responses slow down before 429 | Monitor response latency; proactively reduce request rate when latency increases |

See `${CLAUDE_SKILL_DIR}/references/errors.md` for full error reference.

## Examples

See `${CLAUDE_SKILL_DIR}/references/examples.md` for runnable code samples.

## Resources

- [OpenRouter Documentation](https://openrouter.ai/docs)
- [OpenRouter Models](https://openrouter.ai/models)
- [OpenRouter API Reference](https://openrouter.ai/docs/api-reference)
- [OpenRouter Status](https://status.openrouter.ai)
