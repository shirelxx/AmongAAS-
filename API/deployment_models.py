import uuid
from datetime import datetime

from pydantic import BaseModel


class Deployment(BaseModel):
    db_name: str
    username: str


class DeploymentWithoutUN(BaseModel):
    id: uuid.UUID
    db_name: str
    status: str
    creation_time: datetime
    class Config:
        orm_mode = True
