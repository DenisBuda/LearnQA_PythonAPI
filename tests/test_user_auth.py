import requests
import json
from lib.base_case import BaseCase
from lib.assertions import Assertions

class TestUserAuth(BaseCase):
    def setup(self):
        data = {
            'email': 'vinkotov@example.com',
            'password': '1234'
        }

        url = "https://playground.learnqa.ru/api/user/login"

        response = requests.post(url=url, data=data)

        values_from_response = response.text
        ser_to_json = json.loads(values_from_response)
        self.my_id = ser_to_json["user_id"]

        self.auth_sid = self.get_cookie(response, "auth_sid")

        self.token = self.get_header(response, "x-csrf-token")

        self.my_user_id_from_response = response.json()["user_id"]

        self.my_user_id_from_response = self.get_json_value(response, "user_id")


    def test_auth_user(self):
        response2 = requests.get("https://playground.learnqa.ru/api/user/auth",
                                 headers={"x-csrf-token":self.token},
                                 cookies={"auth_sid":self.auth_sid}
                                 )
        Assertions.assert_json_value_by_name(
            response2,
            "user_id",
            self.my_user_id_from_response,
            "User id from auth method is not equal to user id from check method"
        )

