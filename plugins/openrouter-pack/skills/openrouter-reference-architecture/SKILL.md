---
name: openrouter-reference-architecture
description: |
  Design scalable architectures using OpenRouter. Use when planning system design or reviewing architecture. Trigger with phrases like 'openrouter architecture', 'openrouter system design', 'openrouter infrastructure', 'openrouter at scale'.
allowed-tools: Read, Write, Edit, Grep
version: 1.0.0
license: MIT
author: Jeremy Longshore <jeremy@intentsolutions.io>
compatible-with: claude-code, codex, openclaw
---
# Openrouter Reference Architecture

## Overview

This skill provides reference architecture patterns for building production-grade systems with OpenRouter, from simple single-service setups to distributed microservice architectures.

## Prerequisites

- OpenRouter integration
- Understanding of distributed system patterns

## Instructions

1. **Design the API gateway layer**: Place a gateway in front of OpenRouter calls that handles authentication, rate limiting, request validation, and routing
2. **Implement the service layer**: Create dedicated AI service(s) that encapsulate all OpenRouter interactions, exposing clean internal APIs to your application
3. **Add async processing**: Use a message queue (Redis, SQS, RabbitMQ) for non-real-time AI tasks; process them with worker services that can retry and scale independently
4. **Build the caching layer**: Add Redis or Memcached between your service and OpenRouter for response caching, with cache-aside pattern and TTL-based invalidation
5. **Deploy observability**: Implement distributed tracing (OpenTelemetry) across all layers so you can trace a user request through gateway -> service -> OpenRouter and back

## Output

- Architecture diagram showing API gateway, AI service, cache, queue, and observability layers
- Service-level configuration templates for each component
- Capacity planning estimates based on expected request volume

## Error Handling

| Error | Cause | Fix |
|-------|-------|-----|
| Single point of failure | No redundancy in AI service layer | Deploy at least 2 instances behind a load balancer |
| Queue backlog growing | Worker throughput < incoming rate | Scale workers horizontally; implement backpressure signaling |
| Cache stampede | Many requests for same uncached key simultaneously | Use cache locking or probabilistic early expiration |

See `${CLAUDE_SKILL_DIR}/references/errors.md` for full error reference.

## Examples

See `${CLAUDE_SKILL_DIR}/references/examples.md` for runnable code samples.

## Resources

- [OpenRouter Documentation](https://openrouter.ai/docs)
- [OpenRouter Models](https://openrouter.ai/models)
- [OpenRouter API Reference](https://openrouter.ai/docs/api-reference)
- [OpenRouter Status](https://status.openrouter.ai)
