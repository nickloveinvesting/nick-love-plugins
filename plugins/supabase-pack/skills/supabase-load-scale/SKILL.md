---
name: supabase-load-scale
description: |
  Implement Supabase load testing, auto-scaling, and capacity planning strategies.
  Use when running performance tests, configuring horizontal scaling,
  or planning capacity for Supabase integrations.
  Trigger with phrases like "supabase load test", "supabase scale",
  "supabase performance test", "supabase capacity", "supabase k6", "supabase benchmark".
allowed-tools: Read, Write, Edit, Bash(k6:*), Bash(kubectl:*)
version: 1.0.0
license: MIT
author: Jeremy Longshore <jeremy@intentsolutions.io>
compatible-with: claude-code, codex, openclaw
---
# Supabase Load Scale

## Prerequisites
- k6 load testing tool installed
- Kubernetes cluster with HPA configured
- Prometheus for metrics collection
- Test environment API keys

## Instructions

Load testing a Supabase integration requires testing the right layers: your application code, connection pooling behavior, Supabase's own rate limits, and Postgres query performance under concurrent load. Testing only the application layer without observing database-level metrics can miss connection exhaustion and query plan degradation, which are the most common failure modes under high traffic.

### Step 1: Create Load Test Script
Write a k6 test script that models your realistic traffic pattern — not just a flat ramp but the spike behavior and read/write ratio you expect at peak. Set thresholds for P95 and P99 latency at values that match your SLAs. Include both read-heavy and write-heavy scenarios since they stress different parts of the Supabase stack.

### Step 2: Configure Auto-Scaling
Set up HPA with CPU and custom metrics tied to request queue depth or active connection count. Configure scale-up and scale-down policies that avoid oscillation under sustained moderate load. Ensure your Supabase connection pool size is aligned with the maximum expected replica count so you do not exhaust database connections during scale-out events.

### Step 3: Run Load Test
Execute the test against a staging environment that mirrors production configuration. Collect metrics at the application, connection pool, and database levels simultaneously. Watch for connection timeout errors and query latency increases as indicators of bottlenecks before they cause outages.

### Step 4: Analyze and Document
Record results in the benchmark template, including throughput, latency percentiles, error rate, and peak connection count. Derive capacity recommendations stating the safe maximum requests-per-second before SLA thresholds are breached.

## Output
- Load test script created covering realistic traffic patterns
- HPA configured with alignment to Supabase connection pool limits
- Benchmark results documented with latency percentiles and error rates
- Capacity recommendations defined with confidence from empirical data

## Error Handling

See `${CLAUDE_SKILL_DIR}/references/errors.md` for comprehensive error handling.

## Examples

See `${CLAUDE_SKILL_DIR}/references/examples.md` for detailed examples.

## Resources
- [k6 Documentation](https://k6.io/docs/)
- [Kubernetes HPA](https://kubernetes.io/docs/tasks/run-application/horizontal-pod-autoscale/)
- [Supabase Rate Limits](https://supabase.com/docs/rate-limits)

## Overview

Implement Supabase load testing, auto-scaling, and capacity planning strategies.