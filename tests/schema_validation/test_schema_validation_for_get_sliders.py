import requests
from resources.models_by_schemas.output_model_for_first_slider import Model
from resources.models_by_schemas.second_model_from_online_converter import Model2
from pydantic import ValidationError
from lib.assertions import assert_valid_schema
import json
from lib.constants import CONST_PATH_FOR_SCHEMAS
from pydantic import validator, BaseModel


@validator("title")
def no_some_film_in_title(self, values: str):
    if 'Какой-то фильм' in values:
        return ValueError('Great day')
    return values

class TestGetSliders():
    def test_schema_validation_for_sliders(self):
        # using pydentic
        response = requests.get("https://api.dev.more.tv/app/Sliders/1")
        print(response.text)
        try:
            # compare = Model.parse_raw(response.text)
            compare = Model2.parse_raw(response.text)

        except ValidationError as e:
            print(e.json())

        # using jsonschema validate
        # response = requests.get("https://api.dev.more.tv/app/Sliders/1")
        # my_data = json.loads(response.text)
        # assert_valid_schema(my_data, "json_schema_for_first_slider.json", CONST_PATH_FOR_SCHEMAS)


