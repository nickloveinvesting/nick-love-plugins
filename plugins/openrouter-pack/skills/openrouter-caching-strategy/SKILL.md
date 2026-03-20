---
name: openrouter-caching-strategy
description: |
  Implement response caching to reduce costs and latency. Use when dealing with repeated queries or high-volume scenarios. Trigger with phrases like 'openrouter cache', 'cache responses', 'openrouter caching', 'reduce api calls'.
allowed-tools: Read, Write, Edit, Grep
version: 1.0.0
license: MIT
author: Jeremy Longshore <jeremy@intentsolutions.io>
compatible-with: claude-code, codex, openclaw
---
# Openrouter Caching Strategy

## Overview

This skill shows how to implement caching layers for OpenRouter responses to reduce costs, lower latency, and handle repeated queries efficiently.

## Prerequisites

- OpenRouter integration
- Cache storage (in-memory, Redis, or filesystem)

## Instructions

1. **Generate cache keys**: Hash the model ID, messages array, and key parameters (temperature, max_tokens) into a deterministic cache key
2. **Implement exact-match caching**: Store responses keyed by the hash; return cached responses for identical requests (works best with `temperature: 0`)
3. **Add TTL-based expiration**: Set cache entries to expire after a configurable period (e.g., 1 hour for factual queries, 5 minutes for dynamic content)
4. **Consider semantic caching**: For fuzzy matching, use embedding similarity to find cached responses for semantically similar (but not identical) prompts
5. **Track cache hit rates**: Log cache hits vs misses to measure cost savings and tune your caching strategy

## Output

- Cache hit rate metrics showing percentage of requests served from cache
- Cost savings report comparing cached vs uncached request costs
- Latency improvement measurements (cached responses return in <5ms vs 500ms+ for API calls)

## Error Handling

| Error | Cause | Fix |
|-------|-------|-----|
| Stale cached responses | TTL too long for dynamic content | Reduce TTL or add cache invalidation triggers |
| Cache key collisions | Hash function not including all relevant parameters | Include model, messages, temperature, max_tokens, and tools in the key |
| Memory pressure | In-memory cache growing unbounded | Set max cache size with LRU eviction; use Redis for large caches |

See `${CLAUDE_SKILL_DIR}/references/errors.md` for full error reference.

## Examples

See `${CLAUDE_SKILL_DIR}/references/examples.md` for runnable code samples.

## Resources

- [OpenRouter Documentation](https://openrouter.ai/docs)
- [OpenRouter Models](https://openrouter.ai/models)
- [OpenRouter API Reference](https://openrouter.ai/docs/api-reference)
- [OpenRouter Status](https://status.openrouter.ai)
