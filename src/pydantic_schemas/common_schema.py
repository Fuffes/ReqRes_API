from pydantic import BaseModel, HttpUrl
from pydantic.types import List

from ex import ee
from src.pydantic_schemas.support import Support
from src.pydantic_schemas.data_schemas import UserData, ResourceData



class CommonUserSchema(BaseModel):
    page: int
    per_page: int
    total: int
    total_pages: int
    data: List[UserData]
    support: Support

class CommonResourceSchema(BaseModel):
    page: int
    per_page: int
    total: int
    total_pages: int
    data: List[ResourceData]
    support: Support

# cop = CommonUserSchema.parse_obj(ee)
# print(cop)