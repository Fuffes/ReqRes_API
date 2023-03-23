import pytest
import requests
from configuration import *
from src.base_classes.parser import ResponseParser
from src.pydantic_schemas.resource_schema import Resource
from src.enums.all_enums import TestData


def test_get_all_resources(get_resources_list):
    ResponseParser(get_resources_list).validate_json(Resource).validate_status_code(200)


@pytest.mark.parametrize(
    'ids', TestData.VALID_IDS.value
)
def test_get_single_resource(ids, get_resources_list):
    rec = requests.get(f'https://reqres.in/api/unknown/{ids}')
    total = ResponseParser(get_resources_list).response_total_count
    if isinstance(ids, str) or ids not in range(1, total+1):
        ResponseParser(rec).validate_status_code(404)
    else:
        ResponseParser(rec).validate_json(Resource)
        assert ResponseParser(rec).response_data['id'] == ids



