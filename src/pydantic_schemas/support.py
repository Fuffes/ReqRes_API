from pydantic import BaseModel, HttpUrl

class Support(BaseModel):
    url: HttpUrl
    text: str