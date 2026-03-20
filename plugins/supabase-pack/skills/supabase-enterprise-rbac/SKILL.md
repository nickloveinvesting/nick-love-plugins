---
name: supabase-enterprise-rbac
description: |
  Configure Supabase enterprise SSO, role-based access control, and organization management.
  Use when implementing SSO integration, configuring role-based permissions,
  or setting up organization-level controls for Supabase.
  Trigger with phrases like "supabase SSO", "supabase RBAC",
  "supabase enterprise", "supabase roles", "supabase permissions", "supabase SAML".
allowed-tools: Read, Write, Edit
version: 1.0.0
license: MIT
author: Jeremy Longshore <jeremy@intentsolutions.io>
compatible-with: claude-code, codex, openclaw
---
# Supabase Enterprise Rbac

## Prerequisites
- Supabase Enterprise tier subscription
- Identity Provider (IdP) with SAML/OIDC support
- Understanding of role-based access patterns
- Audit logging infrastructure

## Instructions

Enterprise RBAC for Supabase involves coordinating three systems: your Identity Provider (IdP) for authentication, Supabase's Row Level Security for data authorization, and your application middleware for API-level enforcement. Getting these layers aligned correctly is critical — a misconfigured RLS policy can either block legitimate users or expose data to unauthorized roles, so testing each role definition against real queries before going to production is essential.

### Step 1: Define Roles
Map organizational roles to Supabase permissions. Document each role's data access requirements, which tables they can read or write, and which operations require elevated privileges. Use Postgres roles to enforce separation at the database level.

### Step 2: Configure SSO
Set up SAML or OIDC integration with your IdP. Ensure that the IdP passes the correct group or role claims in the token so Supabase can map them to the appropriate Postgres role at session start.

### Step 3: Implement Middleware
Add permission checks to API endpoints. Middleware should extract the user's role from the JWT and reject requests that attempt operations the role is not authorized for before they reach the database.

### Step 4: Enable Audit Logging
Track all access for compliance. Log the authenticated user, role, operation type, and timestamp for every data-modifying request so you have a complete audit trail for security reviews.

## Output
- Role definitions implemented and tested against representative queries
- SSO integration configured with verified claim mapping
- Permission middleware active and rejecting unauthorized operations
- Audit trail enabled and capturing all data-modifying events

## Error Handling

See `${CLAUDE_SKILL_DIR}/references/errors.md` for comprehensive error handling.

## Examples

See `${CLAUDE_SKILL_DIR}/references/examples.md` for detailed examples.

## Resources
- [Supabase Enterprise Guide](https://supabase.com/docs/enterprise)
- [SAML 2.0 Specification](https://wiki.oasis-open.org/security/FrontPage)
- [OpenID Connect Spec](https://openid.net/specs/openid-connect-core-1_0.html)

## Overview

Configure Supabase enterprise SSO, role-based access control, and organization management.