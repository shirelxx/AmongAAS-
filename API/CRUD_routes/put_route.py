from API.connect import SessionLocal
from sql.postgres_deployment import Deployments
from fastapi import APIRouter, HTTPException
from API.validate import validate_prefix

put_router = APIRouter()


@put_router.put('/deployments/{deployment_id}')
def create_deployment(deployment_id: str, db_name_body: dict):
    session = SessionLocal()
    deployment = session.query(Deployments).filter(Deployments.id == deployment_id).first()
    if deployment is None:
        raise HTTPException(status_code=404, detail="deployment not found")
    new_db_name = db_name_body.get("db_name")
    validate_prefix(new_db_name)
    deployment.db_name = new_db_name
    session.commit()

    return {"deployment_id": str(deployment.id)}