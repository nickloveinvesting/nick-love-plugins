---
name: vercel-reliability-patterns
description: |
  Implement Vercel reliability patterns including circuit breakers, idempotency, and graceful degradation.
  Use when building fault-tolerant Vercel integrations, implementing retry strategies,
  or adding resilience to production Vercel services.
  Trigger with phrases like "vercel reliability", "vercel circuit breaker",
  "vercel idempotent", "vercel resilience", "vercel fallback", "vercel bulkhead".
allowed-tools: Read, Write, Edit
version: 1.0.0
license: MIT
author: Jeremy Longshore <jeremy@intentsolutions.io>
compatible-with: claude-code, codex, openclaw
---
# Vercel Reliability Patterns

## Prerequisites
- Understanding of circuit breaker pattern
- opossum or similar library installed
- Queue infrastructure for DLQ
- Caching layer for fallbacks

## Instructions

Building reliable Vercel-deployed services requires addressing reliability at two levels: the reliability of calls made from your serverless functions to external dependencies, and the reliability of the Vercel deployment itself as seen by end users. Circuit breakers protect against dependency degradation propagating to user-facing failures. Idempotency keys make operations safe to retry after function timeouts. Vercel's edge caching and instant rollback capabilities protect against deployment-level failures.

### Step 1: Implement Circuit Breaker
Wrap calls to external services (databases, third-party APIs) inside your serverless functions with a circuit breaker. When a dependency is degraded, the circuit opens and subsequent calls immediately return a fallback response rather than waiting for the full timeout, which keeps your Vercel function execution time low and prevents cascading failures. Use a library like opossum and configure the failure threshold based on the dependency's expected reliability.

### Step 2: Add Idempotency Keys
Generate deterministic keys for state-modifying API operations by hashing the request payload and user identity. Return the cached result for duplicate requests rather than executing the operation again. This is critical for mutation endpoints that may be retried by clients after a network error or Vercel function timeout.

### Step 3: Configure Bulkheads
Separate processing queues for background operations so that a surge in low-priority work does not consume all available function concurrency and starve real-time user-facing requests.

### Step 4: Set Up Dead Letter Queue
Route background operations that exceed their retry budget to a dead letter queue rather than silently dropping them. Alert on DLQ depth and provide a replay interface so failed operations can be reprocessed after the underlying issue is resolved.

## Output
- Circuit breakers protecting all external dependency calls from cascading failures
- Idempotency implemented on all state-modifying API endpoints
- Bulkhead concurrency isolation between real-time and background workloads
- Dead letter queue capturing and alerting on permanently failed operations

## Error Handling

See `${CLAUDE_SKILL_DIR}/references/errors.md` for comprehensive error handling.

## Examples

See `${CLAUDE_SKILL_DIR}/references/examples.md` for detailed examples.

## Resources
- [Circuit Breaker Pattern](https://martinfowler.com/bliki/CircuitBreaker.html)
- [Opossum Documentation](https://nodeshift.dev/opossum/)
- [Vercel Reliability Guide](https://vercel.com/docs/reliability)

## Overview

Implement Vercel reliability patterns including circuit breakers, idempotency, and graceful degradation.