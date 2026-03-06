from pydantic import BaseModel


class Deployment(BaseModel):
    db_name: str
    username: str