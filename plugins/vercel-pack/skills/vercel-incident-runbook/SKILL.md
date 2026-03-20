---
name: vercel-incident-runbook
description: |
  Execute Vercel incident response procedures with triage, mitigation, and postmortem.
  Use when responding to Vercel-related outages, investigating errors,
  or running post-incident reviews for Vercel integration failures.
  Trigger with phrases like "vercel incident", "vercel outage",
  "vercel down", "vercel on-call", "vercel emergency", "vercel broken".
allowed-tools: Read, Grep, Bash(kubectl:*), Bash(curl:*)
version: 1.0.0
license: MIT
author: Jeremy Longshore <jeremy@intentsolutions.io>
compatible-with: claude-code, codex, openclaw
---
# Vercel Incident Runbook

## Prerequisites
- Access to Vercel dashboard and status page
- kubectl access to production cluster
- Prometheus/Grafana access
- Communication channels (Slack, PagerDuty)

## Instructions

Incident response for Vercel deployments requires distinguishing between three root cause categories: Vercel platform issues (check vercel-status.com), build or deployment configuration issues (broken builds, missing environment variables, bad rollouts), and application-level issues (code bugs, dependency failures, third-party API outages affecting the deployed application). Accurate categorization determines whether the fix is a Vercel support escalation, a configuration rollback, or an application code fix.

### Step 1: Quick Triage
Run the triage commands to identify the issue source. Check the Vercel status page for active incidents. Review the deployment log for the current production build to identify any build warnings that may have introduced instability. Test the deployed application from multiple regions using the Vercel Functions tab to distinguish geographically isolated issues from global outages.

### Step 2: Follow Decision Tree
Determine if the issue is Vercel-side or internal. If the status page shows no active incident but your application is failing, the issue is internal. Check whether the problem started after a recent deployment — if so, a rollback to the last good deployment is the fastest mitigation.

### Step 3: Execute Immediate Actions
For deployment-related issues, use Vercel's instant rollback feature to revert to the previous production deployment without a new build. For application code issues that cannot be quickly fixed, enable a maintenance page using Vercel's rewrite rules to give users a clear error state rather than broken functionality.

### Step 4: Communicate Status
Update internal and external stakeholders with clear, jargon-free status updates. Specify the user impact, the current mitigation status, and the expected resolution timeline.

## Output
- Issue categorized as platform, deployment, or application layer
- Remediation applied (rollback, maintenance page, or code fix)
- Stakeholders notified with impact summary and timeline
- Postmortem evidence collected including deployment history and error logs

## Error Handling

See `${CLAUDE_SKILL_DIR}/references/errors.md` for comprehensive error handling.

## Examples

See `${CLAUDE_SKILL_DIR}/references/examples.md` for detailed examples.

## Resources
- [Vercel Status Page](https://www.vercel-status.com)
- [Vercel Support](https://support.vercel.com)

## Overview

Execute Vercel incident response procedures with triage, mitigation, and postmortem.