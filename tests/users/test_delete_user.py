from src.base_classes.parser import ResponseParser
from src.enums.all_enums import TestData
from src.pydantic_schemas.update_response import UpdatedResp


def test_delete_existing_user(delete_user):
    assert delete_user(TestData.VALID_ID.value[0]).status_code == 204

def test_delete_non_existent_user(delete_user):
    assert delete_user(TestData.INVALID_ID.value[0]).status_code == 204
