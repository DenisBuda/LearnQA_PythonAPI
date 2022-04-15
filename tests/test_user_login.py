import requests
from lib.my_requests import MyRequests
from lib.base_case import BaseCase
from lib.assertions import Assertions
import json

class TestUserLogin:
    def test_get_user_details_auth_as_different_user(self):
        # Авторизация под пользователем с id == 2
        my_data = BaseCase.data2
        result = MyRequests.send_request("POST", "api/user/login", data=my_data)

        # Создание другого рандомного пользователя
        datas = BaseCase.get_my_data(5, "@gmail.com")
        result2 = MyRequests.send_request("POST","api/user/", data=datas)
        Assertions.assert_good_client_status_code(result2.status_code, result2.text, datas)

        ser_to_json = json.loads(result2.text)
        new_user_id = ser_to_json["id"]
        expected_user_name = datas['username']

        # Получение данных созданного рандомного пользователя
        result3 = MyRequests.send_request("GET", f"api/user/{new_user_id}")

        ser_to_json = json.loads(result3.text)
        received_user_name = ser_to_json["username"]
        Assertions.assert_get_only_username(result3.status_code, result3.text, new_user_id, expected_user_name, received_user_name)
        Assertions.assert_compare_jsons_for_get_only_username_from_response(ser_to_json, expected_user_name)

