---
name: supabase-performance-tuning
description: |
  Optimize Supabase API performance with caching, batching, and connection pooling.
  Use when experiencing slow API responses, implementing caching strategies,
  or optimizing request throughput for Supabase integrations.
  Trigger with phrases like "supabase performance", "optimize supabase",
  "supabase latency", "supabase caching", "supabase slow", "supabase batch".
allowed-tools: Read, Write, Edit
version: 1.0.0
license: MIT
author: Jeremy Longshore <jeremy@intentsolutions.io>
compatible-with: claude-code, codex, openclaw
---
# Supabase Performance Tuning

## Prerequisites
- Supabase SDK installed
- Understanding of async patterns
- Redis or in-memory cache available (optional)
- Performance monitoring in place

## Instructions

Performance tuning a Supabase integration should follow a measurement-first discipline. Applying optimizations without a baseline makes it impossible to quantify impact, and premature optimization often targets the wrong bottleneck. Start with profiling, then apply targeted improvements in order of expected impact.

### Step 1: Establish Baseline
Measure current latency for critical Supabase operations using application-level instrumentation or the Supabase query editor's explain analyze output. Record P50, P95, and P99 latencies for each operation under representative load. Identify the three to five slowest operations as your primary targets.

### Step 2: Implement Caching
Add response caching for frequently accessed data that changes infrequently. Use TTL-based invalidation for data that has a predictable freshness requirement and event-driven invalidation for data that must be immediately consistent after writes. An LRU cache in memory is appropriate for single-instance applications; Redis is needed for multi-instance deployments.

### Step 3: Enable Batching
Use DataLoader or a similar batching library to coalesce multiple individual record lookups into a single Supabase query with an `IN` clause. This is especially effective in GraphQL resolvers where N+1 query problems are common. Verify the batch size does not exceed Supabase's row limit per request.

### Step 4: Optimize Connections
Configure connection pooling with keep-alive settings appropriate for your deployment environment. Serverless functions require aggressive connection reuse via PgBouncer in transaction mode; long-running servers can use session-mode pooling with a larger pool size.

## Output
- Measured baseline latency documented for the top critical operations
- Caching layer implemented with appropriate invalidation strategy
- Request batching eliminating N+1 query patterns
- Connection pooling configured for the deployment environment

## Error Handling

See `${CLAUDE_SKILL_DIR}/references/errors.md` for comprehensive error handling.

## Examples

See `${CLAUDE_SKILL_DIR}/references/examples.md` for detailed examples.

## Resources
- [Supabase Performance Guide](https://supabase.com/docs/performance)
- [DataLoader Documentation](https://github.com/graphql/dataloader)
- [LRU Cache Documentation](https://github.com/isaacs/node-lru-cache)

## Overview

Optimize Supabase API performance with caching, batching, and connection pooling.