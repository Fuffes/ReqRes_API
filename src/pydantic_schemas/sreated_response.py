from datetime import datetime

from pydantic import BaseModel


class CreatedRespFull(BaseModel):
    name: str
    job: str
    id: int
    createdAt: datetime

class CreatedRespEmpt(BaseModel):
    id: int
    createdAt: datetime