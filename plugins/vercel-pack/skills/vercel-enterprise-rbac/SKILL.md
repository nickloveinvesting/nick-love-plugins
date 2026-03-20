---
name: vercel-enterprise-rbac
description: |
  Configure Vercel enterprise SSO, role-based access control, and organization management.
  Use when implementing SSO integration, configuring role-based permissions,
  or setting up organization-level controls for Vercel.
  Trigger with phrases like "vercel SSO", "vercel RBAC",
  "vercel enterprise", "vercel roles", "vercel permissions", "vercel SAML".
allowed-tools: Read, Write, Edit
version: 1.0.0
license: MIT
author: Jeremy Longshore <jeremy@intentsolutions.io>
compatible-with: claude-code, codex, openclaw
---
# Vercel Enterprise Rbac

## Prerequisites
- Vercel Enterprise tier subscription
- Identity Provider (IdP) with SAML/OIDC support
- Understanding of role-based access patterns
- Audit logging infrastructure

## Instructions

Enterprise RBAC for Vercel involves two distinct access control planes: team-level access control (who can deploy to which projects and environments) managed in the Vercel dashboard, and application-level access control (who can access what content within deployed applications) implemented in your application code and middleware. Both planes must be configured deliberately to prevent unauthorized deployments and to protect sensitive application routes.

### Step 1: Define Roles
Map organizational roles to Vercel permissions. Vercel's team roles (Owner, Member, Developer, Viewer) control deployment and project management access. Define which roles are permitted to deploy to the production environment versus preview-only, and document the business justification for each role's production access level.

### Step 2: Configure SSO
Set up SAML or OIDC integration with your Identity Provider so that Vercel team membership is controlled through your centralized directory. This ensures that when an employee is offboarded, their Vercel access is revoked automatically as part of the IdP deprovisioning flow.

### Step 3: Implement Middleware
Add permission checks to API endpoints and protected application routes using Vercel Edge Middleware. Middleware runs before the request reaches your application, enabling you to enforce authentication and authorization at the network edge with minimal latency overhead.

### Step 4: Enable Audit Logging
Track all deployment events, team membership changes, and environment variable access for compliance. Vercel's audit log captures who deployed what and when. Export audit logs to your SIEM for centralized security monitoring.

## Output
- Role definitions implemented and documented with business justification
- SSO integration configured with automatic deprovisioning on offboarding
- Edge Middleware enforcing authentication on protected routes
- Audit logs exported to SIEM for centralized compliance monitoring

## Error Handling

See `${CLAUDE_SKILL_DIR}/references/errors.md` for comprehensive error handling.

## Examples

See `${CLAUDE_SKILL_DIR}/references/examples.md` for detailed examples.

## Resources
- [Vercel Enterprise Guide](https://vercel.com/docs/enterprise)
- [SAML 2.0 Specification](https://wiki.oasis-open.org/security/FrontPage)
- [OpenID Connect Spec](https://openid.net/specs/openid-connect-core-1_0.html)

## Overview

Configure Vercel enterprise SSO, role-based access control, and organization management.