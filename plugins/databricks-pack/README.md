# Databricks Skill Pack

> Claude Code skill pack for Databricks integration (24 skills)

## Installation

```bash
/plugin install databricks-pack@claude-code-plugins-plus
```

## Skills Included

### Standard Skills (S01-S12)
| Skill | Description |
|-------|-------------|
| `databricks-install-auth` | Install CLI and configure authentication |
| `databricks-hello-world` | First cluster and notebook |
| `databricks-local-dev-loop` | Local dev with dbx and IDE |
| `databricks-sdk-patterns` | Python/REST SDK patterns |
| `databricks-core-workflow-a` | Delta Lake ETL pipelines |
| `databricks-core-workflow-b` | MLflow model training |
| `databricks-common-errors` | Common errors and fixes |
| `databricks-debug-bundle` | Debug bundle collection |
| `databricks-rate-limits` | API rate limits and backoff |
| `databricks-security-basics` | Secrets and access control |
| `databricks-prod-checklist` | Production deployment checklist |
| `databricks-upgrade-migration` | Version upgrades and migrations |

### Pro Skills (P13-P18)
| Skill | Description |
|-------|-------------|
| `databricks-ci-integration` | GitHub Actions CI/CD |
| `databricks-deploy-integration` | Asset Bundles deployment |
| `databricks-webhooks-events` | Job events and notifications |
| `databricks-performance-tuning` | Cluster and query optimization |
| `databricks-cost-tuning` | Cost optimization strategies |
| `databricks-reference-architecture` | Reference project architecture |

### Flagship Skills (F19-F24)
| Skill | Description |
|-------|-------------|
| `databricks-multi-env-setup` | Dev/staging/prod environments |
| `databricks-observability` | Metrics, logging, and alerting |
| `databricks-incident-runbook` | Incident response procedures |
| `databricks-data-handling` | Delta Lake data management |
| `databricks-enterprise-rbac` | Unity Catalog RBAC |
| `databricks-migration-deep-dive` | Platform migration strategies |

## Usage

Skills trigger automatically when you discuss Databricks topics. For example:

- "Help me set up Databricks" -> triggers `databricks-install-auth`
- "Debug this Databricks error" -> triggers `databricks-common-errors`
- "Deploy my Databricks jobs" -> triggers `databricks-deploy-integration`
- "Optimize my Spark cluster" -> triggers `databricks-performance-tuning`
- "Set up Unity Catalog permissions" -> triggers `databricks-enterprise-rbac`

## Key Concepts

- **Clusters**: Managed Spark compute resources
- **Notebooks**: Interactive development environment
- **Jobs**: Scheduled/triggered workflows
- **Delta Lake**: ACID-compliant data lake storage
- **MLflow**: ML experiment tracking and model registry
- **Unity Catalog**: Unified governance for data and AI

## License

MIT
