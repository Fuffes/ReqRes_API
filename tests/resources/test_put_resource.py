from src.base_classes.parser import ResponseParser
from src.enums.all_enums import TestData
from src.pydantic_schemas.update_response import UpdatedResp


def test_update_existing_resource(put_resource):
    users = ResponseParser(put_resource(TestData.VALID_ID.value[0])).validate_full_json(UpdatedResp)
    assert users.response_status_code == 200

def test_update_non_existent_resource(put_resource):
    users = ResponseParser(put_resource(TestData.INVALID_ID.value[0])).validate_full_json(UpdatedResp)
    assert users.response_status_code == 404
