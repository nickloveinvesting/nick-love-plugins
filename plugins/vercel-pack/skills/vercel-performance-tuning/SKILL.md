---
name: vercel-performance-tuning
description: |
  Optimize Vercel API performance with caching, batching, and connection pooling.
  Use when experiencing slow API responses, implementing caching strategies,
  or optimizing request throughput for Vercel integrations.
  Trigger with phrases like "vercel performance", "optimize vercel",
  "vercel latency", "vercel caching", "vercel slow", "vercel batch".
allowed-tools: Read, Write, Edit
version: 1.0.0
license: MIT
author: Jeremy Longshore <jeremy@intentsolutions.io>
compatible-with: claude-code, codex, openclaw
---
# Vercel Performance Tuning

## Prerequisites
- Vercel SDK installed
- Understanding of async patterns
- Redis or in-memory cache available (optional)
- Performance monitoring in place

## Instructions

Performance tuning Vercel deployments centers on four levers: reducing JavaScript bundle size (which directly controls Time to Interactive), leveraging Vercel's edge caching for static and dynamic content, minimizing serverless function cold-start time, and moving latency-critical code to Edge Functions which run close to the user without cold-start penalties. Measuring before and after each optimization is essential to confirm impact and justify the added complexity.

### Step 1: Establish Baseline
Measure current performance metrics using Vercel's built-in analytics or Lighthouse. Record Core Web Vitals (LCP, FID, CLS), serverless function cold-start latency, and cache hit rates for the most-visited routes. Identify which pages or API routes account for the largest share of poor-performing user experiences.

### Step 2: Implement Caching
Configure Vercel's cache-control headers to maximize edge cache utilization for eligible responses. For dynamic pages generated with Next.js ISR or Vercel's `stale-while-revalidate` pattern, set revalidation intervals appropriate to how frequently the underlying data changes. Cache hit rate is the single most impactful metric to improve since it eliminates function invocations entirely.

### Step 3: Enable Batching
Use DataLoader or similar batching libraries to eliminate N+1 query patterns in serverless function handlers. Batching reduces the number of database round-trips per request, which has a multiplicative effect on function latency since each network hop adds cold connection overhead.

### Step 4: Optimize Connections
Configure connection pooling and keep-alive for database connections used inside serverless functions. Since functions may be invoked by many concurrent instances, use a connection pooler like PgBouncer to prevent connection exhaustion at the database level.

## Output
- Baseline Core Web Vitals and function latency documented for target routes
- Edge caching configured with optimized cache-control headers
- N+1 query patterns eliminated through request batching
- Connection pooling configured to prevent database connection exhaustion

## Error Handling

See `${CLAUDE_SKILL_DIR}/references/errors.md` for comprehensive error handling.

## Examples

See `${CLAUDE_SKILL_DIR}/references/examples.md` for detailed examples.

## Resources
- [Vercel Performance Guide](https://vercel.com/docs/performance)
- [DataLoader Documentation](https://github.com/graphql/dataloader)
- [LRU Cache Documentation](https://github.com/isaacs/node-lru-cache)

## Overview

Optimize Vercel API performance with caching, batching, and connection pooling.