from pydantic import BaseModel
from pydantic.color import Color
from pydantic.types import PastDate


class ResourceData(BaseModel):
    id: int
    name: str
    year: PastDate.year
    color: Color
    pantone_value: str
