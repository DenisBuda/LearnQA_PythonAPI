from requests import Response
import json

class Assertions:
    @staticmethod
    def assert_json_value_by_name(response: Response, name, expected_value, error_message):
        try:
            response_as_dict = response.json()
        except json.JSONDecodeError:
            assert False, f"Response is not in json format {response.text}"

        assert name in response_as_dict, f"Response JSON doesn't have key {name}"
        assert response_as_dict[name] == expected_value, error_message

    @staticmethod
    def assert_bad_client_status_code(my_status_code:int, response_text:str, data_or_params_value:dict):
        assert my_status_code == 400, f"Error! Status code is not equal to 400. Status code is: {my_status_code}" \
                                      f"\nText from response: {response_text}" \
                                      f"\nData or params value: {data_or_params_value}"
    @staticmethod
    def assert_good_response_text_for_response_with_incorrect_email(response_text:str):
        assert response_text == "Invalid email format", f"{response_text}"

    @staticmethod
    def assert_good_client_status_code(my_status_code:int, response_text:str, data_or_params_value:dict):
        assert my_status_code == 200, f"Error! Status code is not equal to 200. Status code is: {my_status_code}" \
                                      f"\nText from response: {response_text}" \
                                      f"\nData or params value: {data_or_params_value}"

    @staticmethod
    def assert_short_username(my_status_code:int, response_text:str, data_or_params_value:dict):
        assert my_status_code == 400, f"Error! Status code is not equal to 400. Status code is: {my_status_code}" \
                                      f"\nText from response: {response_text}" \
                                      f"\nData or params value: {data_or_params_value}"
        assert response_text == "The value of 'username' field is too short", f"{response_text}"

    @staticmethod
    def assert_long_username(my_status_code:int, response_text:str, data_or_params_value:dict):
        assert my_status_code == 400, f"Error! Status code is not equal to 400. Status code is: {my_status_code}" \
                                      f"\nText from response: {response_text}" \
                                      f"\nData or params value: {data_or_params_value}"
        assert response_text == "The value of 'username' field is too long", f"{response_text}"