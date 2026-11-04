from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"

def test_project_requirement_and_agent_flow():
    project = client.post("/api/projects", json={"name": "Test project", "description": "API test"})
    assert project.status_code == 200
    project_id = project.json()["id"]
    spec = client.post(f"/api/projects/{project_id}/requirements", json={"content": "Build a REST API for tracking tasks with status and due dates."})
    assert spec.status_code == 200
    assert "acceptance_criteria" in spec.json()["result"]
    plan = client.post(f"/api/projects/{project_id}/agents/planning", json={"content": "Build a REST API for tracking tasks with status and due dates."})
    assert plan.status_code == 200
    assert len(plan.json()["result"]["tasks"]) > 0
    runs = client.get(f"/api/projects/{project_id}/runs")
    assert runs.status_code == 200
    assert len(runs.json()) >= 2
