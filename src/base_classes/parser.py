from src.enums.error_messages import ErrorMessages


class ResponseParser:

    def __init__(self, response):
        self.response = response
        self.response_status_code = response.status_code
        self.response_json = response.json()
        self.response_data = response.json().get('data')
        self.response_total_count = response.json().get('total')
        self.response_full_obj = None

    def validate_full_json(self, schema):
        schema.parse_obj(self.response_json)
        return self

    def validate_json_data(self, schema):
        if isinstance(self.response_data, list):
            for item in self.response_data:
                schema.parse_obj(item)
        else:
            schema.parse_obj(self.response_data)
        return self

    def validate_status_code(self, expected_status_code):
        if isinstance(expected_status_code, list):
            assert self.response_status_code in expected_status_code, ErrorMessages.WRONG_STATUS_CODE
        else:
            assert self.response_status_code == expected_status_code, ErrorMessages.WRONG_STATUS_CODE





    # def validate_json(self, schema):
    #     if isinstance(self.response_data, list):
    #         for item in self.response:
    #             self.response_full_obj = schema.parse_obj(item)
    #     else:
    #         self.response_full_obj = schema.parse_obj(self.response)
    #     return self
