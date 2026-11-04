# AGENTS.md — DevPilot contributor instructions

## Mission
Build DevPilot as a reliable, human-in-the-loop AI software engineering workspace.

## Architecture
- Frontend: Next.js App Router + TypeScript in frontend/.
- Backend: FastAPI in backend/app/.
- Keep HTTP routes thin. Put orchestration and provider logic in services.
- Use Pydantic schemas for request/response validation.
- Persist project and agent-run state through SQLAlchemy.

## Engineering rules
1. Inspect the existing structure before changing files.
2. Prefer small, focused changes. Do not rewrite unrelated modules.
3. TypeScript strict mode must remain enabled.
4. Add or update tests for every behavior change.
5. Never commit API keys, tokens, passwords or .env files.
6. Treat LLM output and user-submitted code as untrusted input.
7. Never execute generated code inside the API process.
8. Do not add shell execution unless it uses an isolated sandbox and explicit approval.
9. Validate external input and handle provider/network errors.
10. Keep API responses structured and versionable.

## Definition of done
- Relevant tests pass.
- New endpoints are documented.
- README and architecture docs are updated when behavior changes.
- No secrets or real user data are added.
