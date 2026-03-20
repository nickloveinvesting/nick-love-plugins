---
name: vercel-deploy-preview
description: |
  Execute Vercel primary workflow: Deploy Preview.
  Use when Deploying a preview for a pull request,
  Testing changes before production, or Sharing preview URLs with stakeholders.
  Trigger with phrases like "vercel deploy preview",
  "create preview deployment with vercel".
allowed-tools: Read, Write, Edit, Bash(npm:*), Grep
version: 1.0.0
license: MIT
author: Jeremy Longshore <jeremy@intentsolutions.io>
compatible-with: claude-code, codex, openclaw
---
# Vercel Deploy Preview

## Overview
Deploy preview environments for pull requests and branches. This is the primary workflow for Vercel — instant previews for every commit. Vercel's preview deployment system gives every branch its own unique URL that updates automatically on each push, enabling stakeholders to review changes in a production-like environment without waiting for a release cycle. Preview environments inherit all project environment variables marked for preview, so they accurately reflect how the feature will behave in production.

## Prerequisites
- Completed `vercel-install-auth` setup
- Understanding of Vercel core concepts
- Valid API credentials configured

## Instructions

### Step 1: Initialize
Connect your repository to Vercel and configure the project settings for preview deployments. Verify that the correct build command and output directory are set for your framework. Ensure that environment variables needed by the preview build are marked with the Preview environment scope in the Vercel dashboard, not just Production.

```typescript
// Step 1 implementation
```

### Step 2: Execute
Push a branch commit or trigger a deployment via the Vercel API. Vercel will build the project, run any configured build checks, and publish to a unique preview URL. Monitor the deployment log for build errors. Retrieve the preview URL from the deployment response and share it with reviewers for feedback before merging.

```typescript
// Step 2 implementation
```

### Step 3: Finalize
After the pull request is reviewed and approved, confirm that the preview deployment passed all checks. When the branch is merged, Vercel will automatically trigger a production deployment. Archive or clean up stale preview deployments for closed PRs to keep your deployment history manageable.

```typescript
// Step 3 implementation
```

## Output
- Preview deployment created with a unique shareable URL
- Build log confirming successful compilation and deployment
- Production deployment triggered automatically on branch merge

## Error Handling
| Error | Cause | Solution |
|-------|-------|----------|
| Error 1 | Cause | Solution |
| Error 2 | Cause | Solution |

## Examples

### Complete Workflow
```typescript
// Complete workflow example
```

### Common Variations
- Variation 1: Description
- Variation 2: Description

## Resources
- [Vercel Documentation](https://vercel.com/docs)
- [Vercel API Reference](https://vercel.com/docs/api)

## Next Steps
For secondary workflow, see `vercel-edge-functions`.