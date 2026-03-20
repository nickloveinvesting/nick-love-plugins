---
name: supabase-reliability-patterns
description: |
  Implement Supabase reliability patterns including circuit breakers, idempotency, and graceful degradation.
  Use when building fault-tolerant Supabase integrations, implementing retry strategies,
  or adding resilience to production Supabase services.
  Trigger with phrases like "supabase reliability", "supabase circuit breaker",
  "supabase idempotent", "supabase resilience", "supabase fallback", "supabase bulkhead".
allowed-tools: Read, Write, Edit
version: 1.0.0
license: MIT
author: Jeremy Longshore <jeremy@intentsolutions.io>
compatible-with: claude-code, codex, openclaw
---
# Supabase Reliability Patterns

## Prerequisites
- Understanding of circuit breaker pattern
- opossum or similar library installed
- Queue infrastructure for DLQ
- Caching layer for fallbacks

## Instructions

Production Supabase integrations must be designed to handle two failure scenarios gracefully: temporary degradation (connection timeouts, brief overloads) and complete unavailability (platform outage). Circuit breakers address the first by preventing retry storms from amplifying degraded conditions. Idempotency keys address the second by making operations safe to replay after a failure, ensuring that a network timeout does not result in duplicated writes when the request is retried.

### Step 1: Implement Circuit Breaker
Wrap Supabase calls with a circuit breaker using a library like opossum. Configure the failure threshold (percentage of failures that trips the breaker), the reset timeout (how long to wait before testing recovery), and a fallback function that returns a cached or default response when the circuit is open. This prevents cascading failures from propagating to your entire application during Supabase degradation events.

### Step 2: Add Idempotency Keys
Generate deterministic keys for write operations using a hash of the input parameters or a client-provided UUID. Store the idempotency key alongside the result so that duplicate requests return the original response rather than executing the operation again. This is especially important for payment or provisioning workflows where duplicate execution has financial or resource consequences.

### Step 3: Configure Bulkheads
Separate queues for different operation priorities so that a surge in low-priority batch processing does not starve high-priority user-facing operations of Supabase connection capacity.

### Step 4: Set Up Dead Letter Queue
Handle permanent failures gracefully by routing operations that exceed the maximum retry count to a dead letter queue. Alert on DLQ depth and provide a replay mechanism so failed operations can be reprocessed after the underlying issue is resolved.

## Output
- Circuit breaker protecting Supabase calls with configured fallback behavior
- Idempotency preventing duplicate writes on retry scenarios
- Bulkhead isolation separating high and low-priority operation queues
- Dead letter queue capturing and alerting on permanent failures

## Error Handling

See `${CLAUDE_SKILL_DIR}/references/errors.md` for comprehensive error handling.

## Examples

See `${CLAUDE_SKILL_DIR}/references/examples.md` for detailed examples.

## Resources
- [Circuit Breaker Pattern](https://martinfowler.com/bliki/CircuitBreaker.html)
- [Opossum Documentation](https://nodeshift.dev/opossum/)
- [Supabase Reliability Guide](https://supabase.com/docs/reliability)

## Overview

Implement Supabase reliability patterns including circuit breakers, idempotency, and graceful degradation.