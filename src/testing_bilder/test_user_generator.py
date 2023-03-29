import json

from pydantic import BaseModel
from pydantic.types import List

class Data(BaseModel):
    first_name: str
    last_name: str

    def set_first(self,f):
        self.first_name = f
class User(BaseModel):
    email: str = None
    password: str = None
    data: List[Data]


    def set_email(self, email):
        self.email = email

    def pars_to_jsonStr(self):
        jsonStr = json.dumps(self.__dict__)  # str
        return jsonStr

    def pars_to_dict(self):
        pure_json = json.loads(self.pars_to_jsonStr())  # dict
        return pure_json