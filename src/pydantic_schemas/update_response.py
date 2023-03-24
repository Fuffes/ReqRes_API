from datetime import datetime

from pydantic import BaseModel


class UpdatedResp(BaseModel):
    updatedAt: datetime
