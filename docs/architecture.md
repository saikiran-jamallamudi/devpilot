# Architecture

## Request flow
1. A user creates a project and submits a requirement.
2. The API persists the requirement and creates an agent run.
3. The orchestrator calls the selected provider (live LLM or deterministic demo provider).
4. The agent returns structured content.
5. DevPilot stores the result and exposes it for human review.

## Agent responsibilities
- Specification agent: requirements, acceptance criteria, edge cases and constraints.
- Planning agent: implementation tasks and dependencies.
- Coding agent: illustrative code drafts; never executed by the server.
- Testing agent: unit/integration/E2E test suggestions.
- Review agent: potential correctness, security and maintainability findings.

## Trust boundaries
LLM output is untrusted. Validate schemas, display it as text, and require human approval. The MVP does not execute code or create GitHub PRs. A future execution service must use disposable, network-restricted sandboxes.
