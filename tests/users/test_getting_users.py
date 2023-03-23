import pytest
import requests
from configuration import *
from src.base_classes.parser import ResponseParser
from src.pydantic_schemas.common_schema import CommonUserSchema
from src.pydantic_schemas.user_data import UserData


def test_get_all_users():
    responce = requests.get(USER_LIST)
    text = responce.json()
    print(text)
    cop = CommonUserSchema.parse_obj(text)


# @pytest.mark.parametrize(
#     'ids', [1, 100, 'asd']
# )
# def test_get_single_user(ids, get_user_list):
#     rec = requests.get(f'https://reqres.in/api/users/{ids}')
#     total = ResponseParser(get_user_list).response_total_count
#     if isinstance(ids, str) or ids not in range(1, total+1):
#         ResponseParser(rec).validate_status_code(404)
#     else:
#         ResponseParser(rec).validate_json(User)
#         assert ResponseParser(rec).response_data['id'] == ids



