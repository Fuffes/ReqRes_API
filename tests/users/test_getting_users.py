import pytest
import requests
from configuration import *
from src.base_classes.parser import ResponseParser
from src.pydantic_schemas.common_schema import CommonUserSchema
from src.pydantic_schemas.user_data import UserData
from src.enums.all_enums import TestData


def test_get_all_users(get_user):
    assert ResponseParser(get_user()).response_status_code == 200


@pytest.mark.parametrize(
    'ids', TestData.VALID_IDS
)
def test_get_valid_user(ids, get_user):
    assert ResponseParser(get_user(ids)).response_status_code == 200


@pytest.mark.parametrize(
    'ids', TestData.INVALID_IDS
)
def test_get_invalid_user(ids, get_user):
    assert ResponseParser(get_user(ids)).response_status_code == 200

