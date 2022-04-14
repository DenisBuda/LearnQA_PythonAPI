import requests
from lib.base_case import BaseCase
from lib.assertions import Assertions
from lib.my_requests import MyRequests
from lib.base_class import BaseClass
import pytest

class TestUserRegister:
    # Создание пользователя с некорректным email - без символа @
    def test_create_user_with_incorrect_email(self):
        datas = BaseCase.get_my_data(7, "gmail.com")

        result = MyRequests.send_request("POST","api/user/", data=datas)

        Assertions.assert_bad_client_status_code(result.status_code, result.text, datas)
        Assertions.assert_good_response_text_for_response_with_incorrect_email(result.text)

    # Создание пользователя без указания одного из полей
    data_without_some_key = BaseCase.my_data_new
    @pytest.mark.parametrize('my_data', data_without_some_key)

    def test_create_user_without_one_of_the_fields(self, my_data):
        result = MyRequests.send_request("POST","api/user/", data=my_data)
        Assertions.assert_bad_client_status_code(result.status_code, result.text, my_data)

    # Создание пользователя с очень коротким именем в один символ
    def test_ctreate_user_with_short_name_one_character(self):
        datas = BaseCase.get_my_data(1, "@gmail.com")

        result = MyRequests.send_request("POST","api/user/", data=datas)
        Assertions.assert_short_username(result.status_code, result.text, datas)

    # Создание пользователя с очень длинным именем - длиннее 250 символов
    def test_ctreate_user_with_long_name_more_than_250_characters(self):
        datas = BaseCase.get_my_data(251, "@gmail.com")

        result = MyRequests.send_request("POST","api/user/", data=datas)
        Assertions.assert_long_username(result.status_code, result.text, datas)
