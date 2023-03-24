import pytest
import requests
from configuration import *
from src.base_classes.parser import ResponseParser
from src.pydantic_schemas.common_schema import CommonUserSchema

from src.enums.all_enums import TestData
from src.pydantic_schemas.data_schemas import UserData


def test_get_all_users(get_users):
    users = ResponseParser(get_users())\
        .validate_json_data(UserData)\
        .validate_full_json(CommonUserSchema)
    assert users.response_status_code == 200


@pytest.mark.parametrize(
    'id', TestData.VALID_ID.value
)
def test_get_valid_user(id, get_users):
    user = ResponseParser(get_users(id)).validate_json_data(UserData)
    assert user.response_status_code == 200


@pytest.mark.parametrize(
    'id', TestData.INVALID_ID.value
)
def test_get_invalid_user(id, get_users):
    assert ResponseParser(get_users(id)).response_json == {}
    assert ResponseParser(get_users(id)).response_status_code == 404

