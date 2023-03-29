from pydantic import BaseModel, HttpUrl
from pydantic.color import Color
from pydantic.networks import email_validator, EmailStr
from pydantic.types import PastDate
from pydantic import FileUrl


class ResourceData(BaseModel):
    id: int
    name: str
    year: str
    color: Color
    pantone_value: str


class UserData(BaseModel):
    id: int
    email: EmailStr
    first_name: str
    last_name: str
    avatar: HttpUrl




