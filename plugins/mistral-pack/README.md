# Mistral AI Skill Pack

> Claude Code skill pack for Mistral AI integration (24 skills)

## Installation

```bash
/plugin install mistral-pack@claude-code-plugins-plus
```

## Skills Included

### Standard Skills (S01-S12)
| Skill | Description |
|-------|-------------|
| `mistral-install-auth` | Install and configure Mistral SDK authentication |
| `mistral-hello-world` | Create minimal working Mistral chat completion |
| `mistral-local-dev-loop` | Configure local development with hot reload |
| `mistral-sdk-patterns` | Production-ready SDK patterns for TypeScript/Python |
| `mistral-core-workflow-a` | Execute chat completions and streaming responses |
| `mistral-core-workflow-b` | Implement embeddings and function calling |
| `mistral-common-errors` | Diagnose and fix common Mistral API errors |
| `mistral-debug-bundle` | Collect debug evidence for support tickets |
| `mistral-rate-limits` | Implement rate limiting and backoff strategies |
| `mistral-security-basics` | Security best practices for API key management |
| `mistral-prod-checklist` | Production deployment checklist |
| `mistral-upgrade-migration` | SDK version upgrades and breaking changes |

### Pro Skills (P13-P18)
| Skill | Description |
|-------|-------------|
| `mistral-ci-integration` | CI/CD integration with GitHub Actions |
| `mistral-deploy-integration` | Deploy to Vercel, Fly.io, Cloud Run |
| `mistral-webhooks-events` | Webhook handling (if applicable) |
| `mistral-performance-tuning` | Optimize latency and throughput |
| `mistral-cost-tuning` | Token optimization and cost management |
| `mistral-reference-architecture` | Best-practice project structure |

### Flagship Skills (F19-F24)
| Skill | Description |
|-------|-------------|
| `mistral-multi-env-setup` | Multi-environment configuration |
| `mistral-observability` | Metrics, traces, and alerting |
| `mistral-incident-runbook` | Incident response procedures |
| `mistral-data-handling` | PII handling and GDPR compliance |
| `mistral-enterprise-rbac` | Enterprise SSO and access control |
| `mistral-migration-deep-dive` | Major migration strategies |

## Usage

Skills trigger automatically when you discuss Mistral AI topics. For example:

- "Help me set up Mistral" triggers `mistral-install-auth`
- "Debug this Mistral error" triggers `mistral-common-errors`
- "Deploy my Mistral integration" triggers `mistral-deploy-integration`

## Mistral AI Models

| Model | Context | Best For |
|-------|---------|----------|
| mistral-large-latest | 128k | Complex reasoning, code generation |
| mistral-medium-latest | 32k | Balanced performance and cost |
| mistral-small-latest | 32k | Fast, cost-effective tasks |
| open-mistral-7b | 32k | Open-source, self-hosting |
| open-mixtral-8x7b | 32k | Open-source mixture of experts |
| mistral-embed | - | Text embeddings (1024 dimensions) |

## License

MIT
