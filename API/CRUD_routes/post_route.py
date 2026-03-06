from fastapi import APIRouter, HTTPException
from datetime import datetime
import config

from API.deployment_models import Deployment
from sql.postgres_deployment import Deployments, Status
from API.connect import SessionLocal, client

post_router = APIRouter()


def validate(data):
    if not data.db_name.startswith(config.PREFIX):
        raise HTTPException(status_code=400,
                            detail="db name has to start with the user prefix"
                            )
    if len(data.username) < config.MIN_LEN:
        raise HTTPException(status_code=400,
                            detail="username length has to be above 3"
                            )


@post_router.post("/deployments")
def create_deployment(data: Deployment):
    validate(data)

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

