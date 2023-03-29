from src.base_classes.parser import ResponseParser
from src.enums.all_enums import TestData
from src.pydantic_schemas.update_response import UpdatedResp


def test_delete_existing_resource(delete_resource):
    assert delete_resource(TestData.VALID_ID.value[0]).status_code == 204

def test_delete_non_existent_resource(delete_resource):
    assert delete_resource(TestData.INVALID_ID.value[0]).status_code == 204
