# Changelog

Daily change log for the Databricks Feature Preview Status Tracker.

## 2026-03-09

**342 features tracked** (1 status changes)

### Status transitions
- [MCP (Model Context Protocol) on Databricks](https://learn.microsoft.com/en-gb/azure/databricks/generative-ai/mcp/connect-external-services): EXPERIMENTAL → PUBLIC_PREVIEW

---
## 2026-03-08

**350 features tracked** (11 new, 1 removed, 4 status changes)

### New features
- Expiring service principal access token notifications (BETA) — Uncategorized
- [MLflow system tables](https://learn.microsoft.com/en-gb/azure/databricks/admin/system-tables/mlflow) (PUBLIC_PREVIEW) — Administration
- [Manage identities](https://learn.microsoft.com/en-gb/azure/databricks/admin/users-groups/groups) (PUBLIC_PREVIEW) — Administration
- [Create a workspace](https://learn.microsoft.com/en-gb/azure/databricks/admin/workspace/create-workspace) (PUBLIC_PREVIEW) — Administration
- [Serverless JARs](https://learn.microsoft.com/en-gb/azure/databricks/jobs/jar) (PUBLIC_PREVIEW) — Compute
- [Scoped personal access tokens](https://learn.microsoft.com/en-us/azure/databricks/dev-tools/auth/pat#create-personal-access-tokens-for-workspace-users) (BETA) — Developers
- [Discover Page](https://learn.microsoft.com/en-us/azure/databricks/discover/discover-page) (BETA) — Uncategorized
- [Lakeflow Connect for HubSpot](https://learn.microsoft.com/en-us/azure/databricks/ingestion/lakeflow-connect/hubspot-overview) (BETA) — Data engineering
- [Lakeflow Connect for TikTok Ads](https://learn.microsoft.com/en-us/azure/databricks/ingestion/lakeflow-connect/tiktok-ads-overview) (BETA) — Data engineering
- [Microsoft OneLake Federation](https://learn.microsoft.com/en-us/azure/databricks/query-federation/onelake) (BETA) — Uncategorized
- [Vector Search High QPS](https://learn.microsoft.com/en-us/azure/databricks/vector-search/create-vector-search) (BETA) — AI and machine learning

### Removed features
- [Context-based Ingress Control](https://learn.microsoft.com/en-us/azure/databricks/security/network/front-end/context-based-ingress) (was PUBLIC_PREVIEW) — Uncategorized

### Status transitions
- [Enable Extended Models (Qwen)](https://docs.databricks.com/aws/en/machine-learning/foundation-model-apis/supported-models#qwen3-next-instruct): BETA → PUBLIC_PREVIEW
- [Allow users to enable the new SQL editor for queries](https://learn.microsoft.com/en-gb/azure/databricks/sql/user/sql-editor/custom-format): PUBLIC_PREVIEW → GA
- [Databricks Apps - Install Apps from Git](https://learn.microsoft.com/en-us/azure/databricks/dev-tools/databricks-apps/deploy/#deploy-from-a-git-repository): BETA → GA
- [Lakebase Postgres](https://learn.microsoft.com/en-us/azure/databricks/oltp): PUBLIC_PREVIEW → GA

---
## 2026-03-07

**341 features tracked** (no changes)

---
## 2026-02-13

**351 features tracked** (24 new, 22 status changes)

### New features
- [serverless budget policies](https://learn.microsoft.com/en-gb/azure/databricks/admin/account-settings/budgets) (PUBLIC_PREVIEW) — Administration
- [Natural language sample data exploration](https://learn.microsoft.com/en-gb/azure/databricks/catalog-explorer/) (PUBLIC_PREVIEW) — Data guides
- [Local disk encryption](https://learn.microsoft.com/en-gb/azure/databricks/compute/custom-containers) (PUBLIC_PREVIEW) — Compute
- [Serverless GPU compute](https://learn.microsoft.com/en-gb/azure/databricks/compute/serverless/) (BETA) — Compute
- [Monitor long fetch times](https://learn.microsoft.com/en-gb/azure/databricks/compute/sql-warehouse/monitor) (BETA) — Compute
- [Shallow clones in federated catalogs](https://learn.microsoft.com/en-gb/azure/databricks/connect/jdbc-connection) (PUBLIC_PREVIEW) — Data guides
- [Governance Hub results display](https://learn.microsoft.com/en-gb/azure/databricks/data-quality-monitoring/anomaly-detection/results) (PRIVATE_PREVIEW) — Data guides
- [Foreign schemas or tables](https://learn.microsoft.com/en-gb/azure/databricks/delta-sharing/create-share) (BETA) — Data sharing
- [Identity columns](https://learn.microsoft.com/en-gb/azure/databricks/delta/variant-shredding) (PUBLIC_PREVIEW) — Tables
- [Knowledge Assistant](https://learn.microsoft.com/en-gb/azure/databricks/generative-ai/agent-bricks/) (GA) — AI and machine learning
- [MCP server tools](https://learn.microsoft.com/en-gb/azure/databricks/generative-ai/agent-framework/external-connection-tools) (PUBLIC_PREVIEW) — AI and machine learning
- [Computer Use](https://learn.microsoft.com/en-gb/azure/databricks/generative-ai/external-models/) (BETA) — AI and machine learning
- [File uploads](https://learn.microsoft.com/en-gb/azure/databricks/genie/) (PUBLIC_PREVIEW) — Business intelligence
- [Delta Lake core operations](https://learn.microsoft.com/en-gb/azure/databricks/iceberg/iceberg-v3) (GA) — Tables
- [Salesforce ingestion pipeline](https://learn.microsoft.com/en-gb/azure/databricks/ingestion/lakeflow-connect/confluence-faq) (GA) — Data engineering
- [streaming_observability](https://learn.microsoft.com/en-gb/azure/databricks/jobs/configure-task) (PUBLIC_PREVIEW) — Data engineering
- [Migrate online tables to online feature store](https://learn.microsoft.com/en-gb/azure/databricks/machine-learning/feature-store/) (PUBLIC_PREVIEW) — AI and machine learning
- [Webhooks](https://learn.microsoft.com/en-gb/azure/databricks/mlflow/databricks-autologging) (PUBLIC_PREVIEW) — AI and machine learning
- [Monitor apps in production](https://learn.microsoft.com/en-gb/azure/databricks/mlflow3/genai/eval-monitor/) (BETA) — AI and machine learning
- [General notebook functionality and code development](https://learn.microsoft.com/en-gb/azure/databricks/notebooks/ds-agent) (GA) — Notebooks
- [Git CLI](https://learn.microsoft.com/en-gb/azure/databricks/repos/git-operations-with-repos) (BETA) — Developers
- [Unknown](https://learn.microsoft.com/en-gb/azure/databricks/security/network/classic/service-endpoints) (PUBLIC_PREVIEW) — Security & compliance
- [REFRESH POLICY](https://learn.microsoft.com/en-gb/azure/databricks/sql/language-manual/sql-ref-syntax-ddl-create-materialized-view) (BETA) — Reference
- [UDFs in Unity Catalog](https://learn.microsoft.com/en-gb/azure/databricks/udf/python-batch-udf) (PUBLIC_PREVIEW) — Developers

### Status transitions
- [Table lineage](https://learn.microsoft.com/en-gb/azure/databricks/admin/system-tables/): PUBLIC_PREVIEW → GA
- [pipelines](https://learn.microsoft.com/en-gb/azure/databricks/admin/system-tables/jobs): GA → PUBLIC_PREVIEW
- [Usage tracking](https://learn.microsoft.com/en-gb/azure/databricks/ai-gateway/): PUBLIC_PREVIEW → GA
- [Cluster configuration (legacy)](https://learn.microsoft.com/en-gb/azure/databricks/archive/compute/configure): PUBLIC_PREVIEW → GA
- [Dedicated compute group access](https://learn.microsoft.com/en-gb/azure/databricks/compute/dedicated-overview): GA → PUBLIC_PREVIEW
- [Zendesk Support connector](https://learn.microsoft.com/en-gb/azure/databricks/connect/managed-ingestion): GA → BETA
- [Certified and deprecated system tags](https://learn.microsoft.com/en-gb/azure/databricks/data-governance/): GA → PRIVATE_PREVIEW
- [Manual assignment per table](https://learn.microsoft.com/en-gb/azure/databricks/data-governance/unity-catalog/filters-and-masks/): PUBLIC_PREVIEW → GA
- [Genie Research Agent](https://learn.microsoft.com/en-gb/azure/databricks/databricks-ai/partner-powered): GA → BETA
- [Read data in shared foreign table or foreign schema](https://learn.microsoft.com/en-gb/azure/databricks/delta-sharing/read-data-databricks): GA → BETA
- [Dynamic partition overwrites with partitionOverwriteMode (legacy)](https://learn.microsoft.com/en-gb/azure/databricks/delta/selective-overwrite): GA → PUBLIC_PREVIEW
- [databricks functions create](https://learn.microsoft.com/en-gb/azure/databricks/dev-tools/cli/bundle-commands): PUBLIC_PREVIEW → EXPERIMENTAL
- [sparklyr and RStudio Desktop](https://learn.microsoft.com/en-gb/azure/databricks/dev-tools/databricks-connect-legacy): GA → PUBLIC_PREVIEW
- [query_tags](https://learn.microsoft.com/en-gb/azure/databricks/dev-tools/go-sql-driver): GA → PRIVATE_PREVIEW
- [JDK 21 support for Databricks Runtime 18.0](https://learn.microsoft.com/en-gb/azure/databricks/dev-tools/sdk-go): BETA → GA
- [Dynamic Client Registration](https://learn.microsoft.com/en-gb/azure/databricks/generative-ai/mcp/connect-external-services): PUBLIC_PREVIEW → EXPERIMENTAL
- [Streaming observability for Lakeflow Jobs](https://learn.microsoft.com/en-gb/azure/databricks/jobs/configure-job): GA → PUBLIC_PREVIEW
- [refresh_policy](https://learn.microsoft.com/en-gb/azure/databricks/ldp/developer/ldp-python-ref-materialized-view): GA → BETA
- [serverless_budget_policy](https://learn.microsoft.com/en-gb/azure/databricks/ldp/serverless): GA → PUBLIC_PREVIEW
- [Install package from a volume with %pip](https://learn.microsoft.com/en-gb/azure/databricks/libraries/notebooks-python-libraries): GA → PUBLIC_PREVIEW
- [Window measures](https://learn.microsoft.com/en-gb/azure/databricks/metric-views/data-modeling/): GA → EXPERIMENTAL
- [Full-text search](https://learn.microsoft.com/en-gb/azure/databricks/vector-search/query-vector-search): PUBLIC_PREVIEW → BETA

---
## 2026-02-11

**215 features tracked** (2 new, 1 removed)

### New features
- [EventBridge support for file events](https://docs.databricks.com/aws/en/connect/unity-catalog/cloud-storage/manage-external-locations#using-a-provided-queue) (PUBLIC_PREVIEW) — Data guides
- [Lakeflow Connect for Zendesk Support](https://learn.microsoft.com/en-us/azure/databricks/ingestion/lakeflow-connect/zendesk-support-overview) (BETA) — Data engineering

### Removed features
- [Use the dashboard authoring agent](https://learn.microsoft.com/en-gb/azure/databricks/dashboards/dashboard-agent) (was BETA) — Business intelligence

---
