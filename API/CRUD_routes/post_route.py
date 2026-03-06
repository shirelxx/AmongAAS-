from datetime import datetime

from fastapi import APIRouter
from API.validate import validate_prefix, validate_min_length
from API.connect import SessionLocal, client
from API.deployment_models import Deployment
from sql.postgres_deployment import Deployments, Status

post_router = APIRouter()


@post_router.post("/deployments")
def create_deployment(data: Deployment):
    validate_prefix(data)
    validate_min_length(data)

    db = client[data.db_name]
    collection = db["deployment"]
    collection.insert_one({'database_name': data.db_name, 'user_name': data.username})
    session = SessionLocal()

    new_deployment = Deployments(
        db_name=data.db_name,
        username=data.username,
        status=Status.CREATED,
        creation_time=datetime.utcnow()
    )

    session.add(new_deployment)
    session.commit()
    session.refresh(new_deployment)
    return {"deployment_id": str(new_deployment.id)}

