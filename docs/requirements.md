# Product requirements

## Goal
Help developers move from natural-language software requirements to reviewable engineering artifacts using specialized AI agents.

## Functional requirements
- Create and list projects.
- Submit requirements to a project.
- Generate structured specifications.
- Generate implementation tasks from specifications.
- Generate code drafts, test plans and code-review reports.
- Track agent run status and history.
- Provide deterministic demo behavior when no LLM key is configured.

## Non-functional requirements
- Validate API inputs and outputs.
- Keep secrets outside source control.
- Do not execute generated code in the API process.
- Keep services modular and testable.
- Support SQLite locally and PostgreSQL through configuration.

## Acceptance criteria
- A user can create a project from the UI.
- A user can submit a requirement and receive a specification.
- The specification contains functional requirements, non-functional requirements, acceptance criteria and edge cases.
- A user can generate a plan and inspect task outputs.
- The API stores agent runs and exposes their status.
- Backend tests pass without an external LLM key.
