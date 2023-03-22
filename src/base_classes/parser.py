class ResponseParser:

    def __init__(self, response):
        self.response = response
        self.response_status_code = response.status_code
        self.response_data = response.json().get('data')
        self.response_total_count = response.json().get('total')

    def validate_json(self, schema):
        if isinstance(self.response_data, list):
            print('hi from list')
            for item in self.response_data:
                schema.parse_obj(item)
        else:
            print('hi from single obj')
            schema.parse_obj(self.response_data)
        return self

    def validate_status_code(self, expected_status_code):
        if isinstance(expected_status_code, list):
            assert self.response_status_code in expected_status_code
        else:
            assert self.response_status_code == expected_status_code

