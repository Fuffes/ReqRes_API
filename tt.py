import requests

from configuration import USER_LIST
from src.pydantic_schemas.user_schema import User

rec = requests.get('https://reqres.in/api/users/2')
data = rec.json().get('data')
print(data['id'])