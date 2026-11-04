# DevPilot

**From idea to tested code with AI agents.** DevPilot is a human-in-the-loop software engineering workspace that turns natural-language requirements into specifications, implementation plans, generated code drafts, test plans, and review findings.

> This repository is an MVP starter. Generated code is treated as untrusted output: it is displayed for review and is never executed by the API server.

## Features
- Project workspace and requirement intake
- Structured specification generation (functional requirements, non-functional requirements, acceptance criteria, edge cases)
- Task planning from specifications
- AI-provider integration with deterministic local fallback
- Code draft generation (review-only; no automatic execution)
- Test-plan generation and code-review findings
- Agent run history and status
- FastAPI backend, PostgreSQL-ready SQLAlchemy models, SQLite default for quick setup
- Next.js / TypeScript frontend
- Pytest backend tests and Playwright E2E starter
- GitHub Actions CI and `AGENTS.md` agent instructions

## Quick start

### Backend
```bash
cd backend
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
uvicorn app.main:app --reload
```
API: http://localhost:8000 · Swagger: http://localhost:8000/docs

### Frontend
```bash
cd frontend
npm install
cp .env.local.example .env.local
npm run dev
```
UI: http://localhost:3000

### Tests
```bash
cd backend
pytest
```

## AI provider
Set `OPENAI_API_KEY` and optionally `OPENAI_MODEL` in `backend/.env` to enable live generation. Without a key, DevPilot uses a deterministic local demo provider so the workflow remains testable. Do not commit secrets.

## Safety model
- AI outputs are untrusted drafts.
- Generated code is not run by the backend.
- GitHub writes and PR creation are not included in this MVP.
- Review outputs and tests before accepting code.
- Any future execution service should use disposable, network-restricted sandboxes with resource limits and explicit approval.

## Repository structure
- `frontend/`: Next.js App Router UI
- `backend/app/`: FastAPI routes, orchestration, providers and models
- `backend/tests/`: API tests
- `e2e/`: Playwright smoke test
- `docs/`: architecture, requirements and test plan

See `AGENTS.md` for AI coding-agent instructions.

## License
MIT
