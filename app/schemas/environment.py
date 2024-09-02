from pydantic import BaseModel


class EnvironmentCreate(BaseModel):
    name: str
