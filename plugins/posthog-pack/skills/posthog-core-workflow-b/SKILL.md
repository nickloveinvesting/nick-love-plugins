---
name: posthog-core-workflow-b
description: |
  Execute PostHog secondary workflow: Core Workflow B.
  Use when implementing secondary use case,
  or complementing primary workflow.
  Trigger with phrases like "posthog secondary workflow",
  "secondary task with posthog".
allowed-tools: Read, Write, Edit, Bash(npm:*), Grep
version: 1.0.0
license: MIT
author: Jeremy Longshore <jeremy@intentsolutions.io>
compatible-with: claude-code, codex, openclaw
---
# PostHog Core Workflow B

## Overview
Secondary workflow for PostHog. Complements the event capture workflow by focusing on feature flag management, A/B experiment evaluation, and cohort analysis. Use this skill when you need to roll out a feature to a percentage of users, evaluate whether an A/B test reached statistical significance, or build a cohort of users who performed a specific sequence of actions for targeted communication.

## Prerequisites
- Completed `posthog-install-auth` setup
- Familiarity with `posthog-core-workflow-a`
- Valid API credentials configured

## Instructions

### Step 1: Setup
Define the feature flag or experiment configuration you want to work with. For feature flags, set the rollout percentage, target cohort filters, and any override rules for internal testing. For experiments, identify the control and variant conditions, select the primary metric to optimize, and calculate the minimum detectable effect size to determine how long the test needs to run before making a decision.

```typescript
// Step 1 implementation
```

### Step 2: Process
Use the PostHog API to evaluate feature flag states for users or retrieve experiment results. For flag evaluation, call the decide endpoint with the user's distinct ID and inspect which flags are active. For experiment analysis, query the funnel or trend data for each variant, calculate conversion rates, and apply significance testing to determine if the observed difference is statistically reliable.

```typescript
// Step 2 implementation
```

### Step 3: Complete
Document the experiment outcome: record the winning variant, the lift observed on the primary metric, and the confidence level. If a winner is declared, update the feature flag to fully roll out the winning variant and archive the experiment. For cohort analysis, export the cohort member list for use in targeted email or in-app messaging campaigns.

```typescript
// Step 3 implementation
```

## Output
- Completed Core Workflow B execution
- Feature flag evaluation results or A/B experiment significance report
- Cohort export or experiment conclusion with recommended action
- Success confirmation or error details

## Error Handling
| Aspect | Workflow A | Workflow B |
|--------|------------|------------|
| Use Case | Primary | Secondary |
| Complexity | Medium | Lower |
| Performance | Standard | Optimized |

## Examples

### Complete Workflow
```typescript
// Complete workflow example
```

### Error Recovery
```typescript
// Error handling code
```

## Resources
- [PostHog Documentation](https://docs.posthog.com)
- [PostHog API Reference](https://docs.posthog.com/api)

## Next Steps
For common errors, see `posthog-common-errors`.