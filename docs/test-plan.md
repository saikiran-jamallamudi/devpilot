# Test plan

## Unit tests
- Demo provider returns valid structured specification data.
- Planner converts a specification into a non-empty task list.
- Provider errors are surfaced safely.

## API integration tests
- Create and list projects.
- Submit a requirement and generate a specification.
- Generate tasks from a specification.
- Fetch agent run history.

## E2E
- Open dashboard.
- Create a project.
- Submit a requirement.
- Confirm specification output is displayed.

## Security checks
- Ensure .env is ignored.
- Ensure generated code is not executed.
- Ensure API errors do not expose secrets.
- Add authorization tests when authentication is implemented.
