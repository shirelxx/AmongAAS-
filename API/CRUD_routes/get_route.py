from fastapi import APIRouter, HTTPException

from API.connect import SessionLocal
from API.deployment_models import DeploymentWithoutUN
from sql.postgres_deployment import Deployments

get_router = APIRouter()


@get_router.get('/deployments/{deployment_id}', response_model=DeploymentWithoutUN)
def create_deployment(deployment_id: str):
    session = SessionLocal()
    deployment = session.query(Deployments).filter(Deployments.id == deployment_id).first()
    if deployment is None:
        raise HTTPException(status_code=404, detail="deployment not found")
    return deployment
