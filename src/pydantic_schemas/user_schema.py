from pydantic import BaseModel, validator


class User(BaseModel):
    id: int
    email: str
    first_name: str
    last_name: str
    avatar: str

    @validator('email')
    def email_check(cls, email):
        if '@' in email:
            return email
        else:
            raise ValueError('wrong email')
