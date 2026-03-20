---
name: openrouter-performance-tuning
description: |
  Optimize OpenRouter request latency and throughput. Use when performance is critical for your application. Trigger with phrases like 'openrouter performance', 'openrouter latency', 'openrouter speed', 'optimize openrouter'.
allowed-tools: Read, Write, Edit, Grep
version: 1.0.0
license: MIT
author: Jeremy Longshore <jeremy@intentsolutions.io>
compatible-with: claude-code, codex, openclaw
---
# Openrouter Performance Tuning

## Overview

This skill provides techniques for reducing latency, increasing throughput, and optimizing the performance of your OpenRouter integration.

## Prerequisites

- Working OpenRouter integration
- Performance metrics collection (response times, throughput)

## Instructions

1. **Measure baseline latency**: Log time-to-first-token (TTFT) and total response time for each request; establish a baseline before optimizing
2. **Use streaming for perceived speed**: Enable `stream: true` to display tokens as they arrive, reducing perceived latency even if total time is unchanged
3. **Choose faster models**: Smaller models (e.g., `google/gemma-2-9b-it:free`, `anthropic/claude-3-haiku`) have significantly lower latency than large reasoning models
4. **Parallelize independent requests**: When you need multiple completions, send requests concurrently using `Promise.all` or `asyncio.gather` instead of sequentially
5. **Reduce round trips**: Minimize the number of API calls by batching related prompts, using larger context windows, or combining multi-step tasks into single prompts

## Output

- Latency benchmarks (TTFT and total time) for each model you use
- Throughput metrics (requests per second) under concurrent load
- Optimized configuration with measurable performance improvements

## Error Handling

| Error | Cause | Fix |
|-------|-------|-----|
| High TTFT (>5s) | Model is cold-starting or overloaded | Switch to a different provider of the same model; use streaming |
| Timeout errors | Request exceeded client timeout | Increase timeout for large completions; reduce `max_tokens` |
| Throughput bottleneck | Sequential request processing | Implement connection pooling and concurrent requests |

See `${CLAUDE_SKILL_DIR}/references/errors.md` for full error reference.

## Examples

See `${CLAUDE_SKILL_DIR}/references/examples.md` for runnable code samples.

## Resources

- [OpenRouter Documentation](https://openrouter.ai/docs)
- [OpenRouter Models](https://openrouter.ai/models)
- [OpenRouter API Reference](https://openrouter.ai/docs/api-reference)
- [OpenRouter Status](https://status.openrouter.ai)
