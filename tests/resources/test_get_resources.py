import pytest
from src.base_classes.parser import ResponseParser
from src.pydantic_schemas.common_schema import CommonResourceSchema
from src.enums.error_messages import ErrorMessages
from src.enums.all_enums import TestData
from src.pydantic_schemas.data_schemas import ResourceData


def test_get_all_resources(get_resources):
    resources = ResponseParser(get_resources())\
        .validate_json_data(ResourceData)\
        .validate_full_json(CommonResourceSchema)
    assert resources.response_status_code == 200


@pytest.mark.parametrize(
    'id', TestData.VALID_ID.value
)
def test_get_valid_resource(id, get_resources):
    resource = ResponseParser(get_resources(id)).validate_json_data(ResourceData)
    assert resource.response_status_code == 200, ErrorMessages.WRONG_STATUS_CODE.value


@pytest.mark.parametrize(
    'id', TestData.INVALID_ID.value
)
def test_get_invalid_resource(id, get_resources):
    assert ResponseParser(get_resources(id)).response_json == {}
    assert ResponseParser(get_resources(id)).response_status_code == 404, ErrorMessages.WRONG_STATUS_CODE.value

