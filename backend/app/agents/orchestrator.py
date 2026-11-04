import json
from sqlalchemy.orm import Session
from app.agents.provider import get_provider
from app.models import AgentRun

AGENTS = {"specification", "planning", "coding", "testing", "code_review"}

def run_agent(db: Session, project_id: int, agent_type: str, payload: dict) -> tuple[AgentRun, dict]:
    if agent_type not in AGENTS:
        raise ValueError("Unsupported agent type")
    result = get_provider().generate(agent_type, payload)
    run = AgentRun(project_id=project_id, agent_type=agent_type, status="completed", input_summary=str(payload.get("requirement", ""))[:500], output_json=json.dumps(result))
    db.add(run)
    db.commit()
    db.refresh(run)
    return run, result
