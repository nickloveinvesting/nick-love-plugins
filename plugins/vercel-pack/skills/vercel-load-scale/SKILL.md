---
name: vercel-load-scale
description: |
  Implement Vercel load testing, auto-scaling, and capacity planning strategies.
  Use when running performance tests, configuring horizontal scaling,
  or planning capacity for Vercel integrations.
  Trigger with phrases like "vercel load test", "vercel scale",
  "vercel performance test", "vercel capacity", "vercel k6", "vercel benchmark".
allowed-tools: Read, Write, Edit, Bash(k6:*), Bash(kubectl:*)
version: 1.0.0
license: MIT
author: Jeremy Longshore <jeremy@intentsolutions.io>
compatible-with: claude-code, codex, openclaw
---
# Vercel Load Scale

## Prerequisites
- k6 load testing tool installed
- Kubernetes cluster with HPA configured
- Prometheus for metrics collection
- Test environment API keys

## Instructions

Load testing Vercel deployments requires understanding the platform's auto-scaling model: serverless functions scale horizontally without configuration, but they have per-invocation concurrency limits and cold-start penalties that can cause latency spikes under sudden traffic bursts. Load tests should simulate both sustained load (to measure steady-state performance) and spike scenarios (to measure cold-start amplification) to give a complete picture of behavior under production traffic patterns.

### Step 1: Create Load Test Script
Write a k6 test script that models your realistic traffic pattern including the read/write ratio, request size distribution, and geographic origin if applicable. Set thresholds for P95 and P99 latency at values aligned to your user experience SLAs. Include a warm-up phase to establish a baseline before the peak load phase to isolate cold-start latency from steady-state latency.

### Step 2: Configure Auto-Scaling
Vercel serverless functions scale automatically, but you may need to configure concurrency limits or use Vercel's Edge Functions for lower-latency scaling at the edge. For workloads with predictable spikes, consider pre-warming strategies or migrating latency-critical paths to edge functions which eliminate cold starts entirely.

### Step 3: Run Load Test
Execute the test against a staging deployment that mirrors production configuration. Collect function invocation metrics from the Vercel dashboard alongside your k6 output. Watch for error rate increases at high concurrency levels and log cold-start occurrences to quantify their frequency and duration.

### Step 4: Analyze and Document
Record results in the benchmark template documenting throughput, latency percentiles, cold-start frequency, and error rate at each load level. Derive capacity recommendations identifying the traffic volume at which latency SLAs are breached.

## Output
- Load test script covering steady-state and spike traffic scenarios
- Scaling configuration aligned to traffic patterns and latency requirements
- Benchmark results documenting performance at each load level
- Capacity recommendations with identified SLA breach thresholds

## Error Handling

See `${CLAUDE_SKILL_DIR}/references/errors.md` for comprehensive error handling.

## Examples

See `${CLAUDE_SKILL_DIR}/references/examples.md` for detailed examples.

## Resources
- [k6 Documentation](https://k6.io/docs/)
- [Kubernetes HPA](https://kubernetes.io/docs/tasks/run-application/horizontal-pod-autoscale/)
- [Vercel Rate Limits](https://vercel.com/docs/rate-limits)

## Overview

Implement Vercel load testing, auto-scaling, and capacity planning strategies.