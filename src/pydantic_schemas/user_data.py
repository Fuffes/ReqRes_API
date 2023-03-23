from pydantic import BaseModel, validator


class UserData(BaseModel):
    id: int
    email: str
    first_name: str
    last_name: str
    avatar: str