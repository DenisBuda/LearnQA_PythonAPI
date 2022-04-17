from requests import Response
import json
import deepdiff

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
    def assert_good_client_status_code(my_status_code:int, response_text:str, data_or_params_value:dict = None):
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

    @staticmethod
    def assert_get_only_username(my_status_code:int, response_text:str, data_or_params_value:dict, username_expected:str, username_received:str):
        assert my_status_code == 200, f"Error! Status code is not equal to 400. Status code is: {my_status_code}" \
                                      f"\nText from response: {response_text}" \
                                      f"\nData or params value: {data_or_params_value}"
        assert username_expected == username_received, f"Error! Expected: {username_expected} Received: {username_received}"


    @staticmethod
    def assert_compare_jsons_for_get_only_username_from_response(dict_from_response:json, username_expected:str):
        expected_json = {
            "username": username_expected
        }

        diff = deepdiff.DeepDiff(expected_json, dict_from_response)
        assert diff == {}, f"Error! Invalid values received: {diff}"

    @staticmethod
    def assert_cookies_keyses_from_response(cookies:dict, user_name:str):
        assert cookies == [], f"Error! We get some keys from cookie for not authorized user: {user_name}"

    @staticmethod
    def assert_not_token_from_heafers_response_for_unauthorized_user(headers:dict, user_name:str):
        assert headers == None, f"Error! We got token for unauthorized user: {user_name}"

    @staticmethod
    def assert_cant_change_unauthorized_user(response_text:str, user_id:str):
        assert response_text == "Auth token not supplied", f"Error! User has been changed {user_id}"

    @staticmethod
    def assert_compare_username_and_email(expected_user_name:str,
                                          expected_user_email:str,
                                          received_user_name:str,
                                          received_user_email:str
                                          ):
        assert expected_user_email == received_user_email, f"Invalid emails: Expected {expected_user_email}, Received: {received_user_email}"
        assert expected_user_name == received_user_name, f"Invalid names: Expected {expected_user_name}, Received: {received_user_name}"

    @staticmethod
    def assert_compare_two_jsons(expected_json:dict, received_json:dict, after_edit:bool = False):
        if after_edit == False:
            diff = deepdiff.DeepDiff(expected_json, received_json)
            assert diff == {}, f"Error! Invalid values received: {diff}"
        else:
            assert expected_json != {}, f"Error! Jsons are equals: {expected_json}, {received_json}"

    @staticmethod
    def assert_for_edit_user_using_incorrect_email(response_text:str):
        etalon_response_text = "Invalid email format"
        assert response_text == etalon_response_text, f"Error! Response text not equal to {etalon_response_text}"

    @staticmethod
    def asserf_for_compare_two_response_text(expected_response_text:str, received_response_text:str):
        assert expected_response_text == received_response_text, f"Error! Texts are not equal{expected_response_text}&{received_response_text}"

    @staticmethod
    def assert_delete_user_with_id_2(response_text:str):
        response_text == "Please, do not delete test users with ID 1, 2, 3, 4 or 5.", f"Error! We got another text from response {response_text}"

    @staticmethod
    def assert_not_found_delete_user(response_text:str):
        response_text == "User not found", "Error! Text from response not equal to expected text"