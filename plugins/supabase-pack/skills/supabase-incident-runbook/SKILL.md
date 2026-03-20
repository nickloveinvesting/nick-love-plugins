---
name: supabase-incident-runbook
description: |
  Execute Supabase incident response procedures with triage, mitigation, and postmortem.
  Use when responding to Supabase-related outages, investigating errors,
  or running post-incident reviews for Supabase integration failures.
  Trigger with phrases like "supabase incident", "supabase outage",
  "supabase down", "supabase on-call", "supabase emergency", "supabase broken".
allowed-tools: Read, Grep, Bash(kubectl:*), Bash(curl:*)
version: 1.0.0
license: MIT
author: Jeremy Longshore <jeremy@intentsolutions.io>
compatible-with: claude-code, codex, openclaw
---
# Supabase Incident Runbook

## Prerequisites
- Access to Supabase dashboard and status page
- kubectl access to production cluster
- Prometheus/Grafana access
- Communication channels (Slack, PagerDuty)

## Instructions

Incident response for Supabase integrations requires distinguishing quickly between platform-side outages (check status.supabase.com) and issues in your own integration code or infrastructure. Misattributing a platform outage as an internal bug wastes critical time during an incident. Always verify the Supabase status page before investing engineering effort in local remediation.

### Step 1: Quick Triage
Run the triage commands to identify the issue source. Check Supabase status page, verify your API credentials have not expired, and run a minimal health check query against your Supabase instance. Compare error rates against your baseline metrics to understand the scope and onset time.

### Step 2: Follow Decision Tree
Determine if the issue is Supabase-side or internal. Platform outages require monitoring the status page and communicating degraded service to users. Internal issues require examining your application logs, recent deployments, and configuration changes for the root cause.

### Step 3: Execute Immediate Actions
Apply the appropriate remediation for the error type. For connection failures, enable circuit breakers and fallback responses. For data inconsistencies, pause write operations to prevent further corruption while you investigate.

### Step 4: Communicate Status
Update internal and external stakeholders. Provide clear, jargon-free status updates at regular intervals. Avoid speculation about root cause until confirmed by investigation.

## Output
- Issue identified and categorized as platform-side or internal
- Remediation applied with evidence of restored service
- Stakeholders notified with timeline and impact summary
- Evidence collected for postmortem including timeline and root cause

## Error Handling

See `${CLAUDE_SKILL_DIR}/references/errors.md` for comprehensive error handling.

## Examples

See `${CLAUDE_SKILL_DIR}/references/examples.md` for detailed examples.

## Resources
- [Supabase Status Page](https://status.supabase.com)
- [Supabase Support](https://support.supabase.com)

## Overview

Execute Supabase incident response procedures with triage, mitigation, and postmortem.