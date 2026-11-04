import json
from fastapi import Depends, FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from app.config import settings
from app.database import Base, engine, get_db
from app.models import Project, Requirement, AgentRun
from app.schemas import ProjectCreate, ProjectOut, RequirementCreate, GenerateResponse, AgentRunOut
from app.agents.orchestrator import run_agent

Base.metadata.create_all(bind=engine)
app = FastAPI(title="DevPilot API", version="0.1.0", description="Human-in-the-loop AI software engineering workspace")
app.add_middleware(CORSMiddleware, allow_origins=[x.strip() for x in settings.cors_origins.split(",")], allow_credentials=True, allow_methods=["*"], allow_headers=["*"])

def serialize_run(run: AgentRun, output: dict | None = None):
    return AgentRunOut(id=run.id, project_id=run.project_id, agent_type=run.agent_type, status=run.status, input_summary=run.input_summary, output=output if output is not None else json.loads(run.output_json), created_at=run.created_at)

@app.get("/health")
def health():
    return {"status": "ok", "service": "devpilot-api"}

@app.post("/api/projects", response_model=ProjectOut)
def create_project(data: ProjectCreate, db: Session = Depends(get_db)):
    project = Project(name=data.name, description=data.description)
    db.add(project); db.commit(); db.refresh(project)
    return project

@app.get("/api/projects", response_model=list[ProjectOut])
def list_projects(db: Session = Depends(get_db)):
    return db.query(Project).order_by(Project.created_at.desc()).all()

@app.get("/api/projects/{project_id}", response_model=ProjectOut)
def get_project(project_id: int, db: Session = Depends(get_db)):
    project = db.get(Project, project_id)
    if not project: raise HTTPException(404, "Project not found")
    return project

@app.post("/api/projects/{project_id}/requirements", response_model=GenerateResponse)
def create_requirement(project_id: int, data: RequirementCreate, db: Session = Depends(get_db)):
    if not db.get(Project, project_id): raise HTTPException(404, "Project not found")
    requirement = Requirement(project_id=project_id, content=data.content)
    db.add(requirement); db.commit(); db.refresh(requirement)
    try:
        run, result = run_agent(db, project_id, "specification", {"requirement": data.content})
    except Exception as exc:
        raise HTTPException(502, f"Specification generation failed: {type(exc).__name__}") from exc
    requirement.specification_json = json.dumps(result); db.commit()
    return GenerateResponse(requirement_id=requirement.id, run=serialize_run(run, result), result=result)

@app.post("/api/projects/{project_id}/agents/{agent_type}", response_model=GenerateResponse)
def execute_agent(project_id: int, agent_type: str, data: RequirementCreate, db: Session = Depends(get_db)):
    if not db.get(Project, project_id): raise HTTPException(404, "Project not found")
    try:
        run, result = run_agent(db, project_id, agent_type, {"requirement": data.content})
    except ValueError as exc: raise HTTPException(404, str(exc)) from exc
    except Exception as exc: raise HTTPException(502, f"Agent execution failed: {type(exc).__name__}") from exc
    return GenerateResponse(run=serialize_run(run, result), result=result)

@app.get("/api/projects/{project_id}/runs", response_model=list[AgentRunOut])
def list_runs(project_id: int, db: Session = Depends(get_db)):
    if not db.get(Project, project_id): raise HTTPException(404, "Project not found")
    runs = db.query(AgentRun).filter_by(project_id=project_id).order_by(AgentRun.created_at.desc()).all()
    return [serialize_run(run) for run in runs]
