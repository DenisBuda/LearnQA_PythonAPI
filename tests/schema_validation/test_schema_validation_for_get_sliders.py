import requests
from resources.models_by_schemas.output_model_for_first_slider import Model
from pydantic import ValidationError
# from lib.assertions import assert_valid_schema
from jsonschema import validate
from os.path import join, dirname
import json

class TestGetSliders():
    def test_schema_validation_for_sliders(self):
        # using pydentic
        # response = requests.get("https://api.dev.more.tv/app/Sliders/1")
        # try:
        #     compare = Model.parse_raw(response.text)
        # except ValidationError as e:
        #     print(e.json())

        # using jsonschema validate
        def assert_valid_schema(data, schema_file):
            """ Checks whether the given data matches the schema """

            schema = _load_json_schema(schema_file)
            return validate(data, schema)

        def _load_json_schema(filename):
            """ Loads the given schema file """

            relative_path = join('schemas', filename)
            absolute_path = join(dirname(__file__), relative_path)

            with open(absolute_path) as schema_file:
                return json.loads(schema_file.read())

        response = requests.get("https://api.dev.more.tv/app/Sliders/1")
        my_data = json.loads(response.text)
        assert_valid_schema(my_data, "json_schema_for_first_slider.json")

