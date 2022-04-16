import requests
from lib.base_case import BaseCase
from lib.my_requests import MyRequests
from lib.assertions import Assertions
import json

class TestUserEdit(BaseCase):
    def test_edit_just_created_user_not_authorized_as_this_user(self):
        datas = BaseCase.get_my_data(5, "@gmail.com")
        result = MyRequests.send_request("POST","api/user/", data=datas)
        Assertions.assert_good_client_status_code(result.status_code, result.text, datas)

        ser_to_json = json.loads(result.text)
        just_created_user_id = ser_to_json["id"]

        # Попытка изменить данные пользователя, будучи неавторизованными
        edit_random_data = BaseCase.get_my_data(5, "@gmail.com")
        result2 = MyRequests.send_request("PUT", f"api/user/{just_created_user_id}", edit_random_data)
        Assertions.assert_cant_change_unauthorized_user(result2.text, just_created_user_id)

    # Попытаемся изменить данные пользователя, будучи авторизованными другим пользователем
    def test_edit_just_created_user_another_authorized_user(self):
        # Создаём пользователя №1
        print("\n")
        print("Пожалуйста подождите, создаётся первый пользователь")
        datas = BaseCase.get_my_data(5, "@gmail.com")
        first_random_user = BaseCase.create_random_user(datas)
        Assertions.assert_good_client_status_code(first_random_user.status_code, first_random_user.text, datas)
        ser_to_json = json.loads(first_random_user.text)

        just_created_user_id = ser_to_json["id"]
        my_email = datas["email"]
        my_password = datas['password']

        # Создаём пользователя №2
        print("Пожалуйста подождите, создаётся второй пользователь")
        datas2 = BaseCase.get_my_data(5, "@gmail.com")
        second_random_user = BaseCase.create_random_user(datas2)
        Assertions.assert_good_client_status_code(second_random_user.status_code, second_random_user.text, datas)
        ser_to_json = json.loads(second_random_user.text)

        just_created_user_id2 = ser_to_json["id"]
        my_email2 = datas2["email"]
        my_password2 = datas2['password']

        # Логинимся под пользователем №1
        my_new_data = {
            'email':my_email,
            'password':my_password

        }
        login_by_first_created_user = MyRequests.send_request("POST", "api/user/login", data=my_new_data)
        print(f"Авторизовались под первым пользователем с ID {just_created_user_id} \n", login_by_first_created_user.text)
        print("Status code:",login_by_first_created_user.status_code)
        self.auth_sid = self.get_cookie(login_by_first_created_user, "auth_sid")
        self.token = self.get_header(login_by_first_created_user, "x-csrf-token")

        #GET получаем данные первого
        print("Получаем данные для первого")
        user_info_for_first_user = MyRequests.send_request("GET",
                                           f"api/user/{just_created_user_id}",
                                           headers={"x-csrf-token":self.token},
                                           cookies={"auth_sid":self.auth_sid}
                                           )
        Assertions.assert_good_client_status_code(user_info_for_first_user.status_code, user_info_for_first_user.text)
        ser_to_json_info_about_first_user = json.loads(user_info_for_first_user.text)
        print(user_info_for_first_user.text)
        print("Status code:",user_info_for_first_user.status_code)

        #Логинимся под пользователем №2
        my_new_data2 = {
            'email':my_email2,
            'password':my_password2

        }
        login_by_second_created_user = MyRequests.send_request("POST", "api/user/login", data=my_new_data2)
        print(f"Авторизовались под вторым пользователем с ID {just_created_user_id2} \n", login_by_second_created_user.text)
        print("Status code:",login_by_second_created_user.status_code)
        self.auth_sid2 = self.get_cookie(login_by_second_created_user, "auth_sid")
        self.token2 = self.get_header(login_by_second_created_user, "x-csrf-token")

        #GET получаем данные второго
        print("Получаем данные для второго")
        user_info_for_second_user = MyRequests.send_request("GET",
                                           f"api/user/{just_created_user_id2}",
                                           headers={"x-csrf-token":self.token2},
                                           cookies={"auth_sid":self.auth_sid2}
                                           )
        ser_to_json_info_about_second_user = json.loads(user_info_for_second_user.text)
        print(user_info_for_second_user.text)
        print("Status code:",user_info_for_second_user.status_code)


        print("Пожалуйста подождите, изменяется данные для второго пользователя авторизованным первым пользователем")

        my_data_for_change_second_user = BaseCase.get_my_data(5, "@rambler.com")

        result_by_change_email_for_second_user = MyRequests.send_request("PUT",
                                          f"api/user/{just_created_user_id2}",
                                          headers={"x-csrf-token": self.token},
                                          cookies={"auth_sid": self.auth_sid},
                                          data=my_data_for_change_second_user
                                          )
        print("Изменили данные второму пользователю\n",
              result_by_change_email_for_second_user.text,
              "Status code:",result_by_change_email_for_second_user.status_code)


        # Снова получаем данные второго и первого пользователя
        print("Получаем данные для первого снова")
        user_info_for_first_user_again = MyRequests.send_request("GET",
                                           f"api/user/{just_created_user_id}",
                                           headers={"x-csrf-token":self.token},
                                           cookies={"auth_sid":self.auth_sid}
                                           )
        ser_to_json_info_about_first_user_again = json.loads(user_info_for_second_user.text)
        print(user_info_for_first_user_again.text)
        print("Status code:",user_info_for_first_user_again.status_code)

        print("Получаем данные для второго снова")
        user_info_for_second_user_again = MyRequests.send_request("GET",
                                           f"api/user/{just_created_user_id2}",
                                           headers={"x-csrf-token":self.token2},
                                           cookies={"auth_sid":self.auth_sid2}
                                           )
        ser_to_json_info_about_second_user_again = json.loads(user_info_for_second_user.text)
        print(user_info_for_second_user_again.text)
        print("Status code:",user_info_for_second_user_again.status_code)

        # Сравниваем ответы для второго пользака
        Assertions.assert_compare_two_jsons(ser_to_json_info_about_second_user, ser_to_json_info_about_second_user_again)
        # Сравниваем ответы для первого пользака
        Assertions.assert_compare_two_jsons(ser_to_json_info_about_first_user,
                                            ser_to_json_info_about_first_user_again, True)


    # Попытаемся изменить email пользователя, будучи авторизованными тем же пользователем, на новый email без символа @
    def test_edit_just_created_user_using_wrong_email(self):
        # Создаём пользователя №1
        print("\n")
        print("Пожалуйста подождите, создаётся первый пользователь")
        datas = BaseCase.get_my_data(5, "@gmail.com")
        first_random_user = BaseCase.create_random_user(datas)
        Assertions.assert_good_client_status_code(first_random_user.status_code, first_random_user.text, datas)
        ser_to_json = json.loads(first_random_user.text)

        just_created_user_id = ser_to_json["id"]
        my_email = datas["email"]
        my_password = datas['password']

        # Логинимся под пользователем №1
        my_new_data = {
            'email':my_email,
            'password':my_password

        }
        login_by_first_created_user = MyRequests.send_request("POST", "api/user/login", data=my_new_data)
        print(f"Авторизовались под первым пользователем с ID {just_created_user_id} \n", login_by_first_created_user.text)
        print("Status code:",login_by_first_created_user.status_code)
        self.auth_sid = self.get_cookie(login_by_first_created_user, "auth_sid")
        self.token = self.get_header(login_by_first_created_user, "x-csrf-token")

        #GET получаем данные первого
        print("Получаем данные для первого")
        user_info_for_first_user = MyRequests.send_request("GET",
                                           f"api/user/{just_created_user_id}",
                                           headers={"x-csrf-token":self.token},
                                           cookies={"auth_sid":self.auth_sid}
                                           )
        Assertions.assert_good_client_status_code(user_info_for_first_user.status_code, user_info_for_first_user.text)

        ser_to_json_info_about_first_user = json.loads(user_info_for_first_user.text)

        print(user_info_for_first_user.text)
        print("Status code:",user_info_for_first_user.status_code)

        # Изменяем данные первого используя email без @
        print("Пожалуйста подождите, изменяется данные для второго пользователя авторизованным первым пользователем")

        my_data_for_change_first_user = BaseCase.get_my_data(5, "rambler.com")

        result_by_change_email_for_current_user = MyRequests.send_request("PUT",
                                          f"api/user/{just_created_user_id}",
                                          headers={"x-csrf-token": self.token},
                                          cookies={"auth_sid": self.auth_sid},
                                          data=my_data_for_change_first_user
                                          )
        print("Изменили данные для первого пользака, email без символа @\n",
              result_by_change_email_for_current_user.text,
              "Status code:",result_by_change_email_for_current_user.status_code)

        # Проверили что мыло не изменилось
        Assertions.assert_for_edit_user_using_incorrect_email(result_by_change_email_for_current_user.text)

        print("Получаем данные для первого снова")
        user_info_for_first_user_again = MyRequests.send_request("GET",
                                           f"api/user/{just_created_user_id}",
                                           headers={"x-csrf-token":self.token},
                                           cookies={"auth_sid":self.auth_sid}
                                           )
        ser_to_json_info_about_first_user_again = json.loads(user_info_for_first_user_again.text)
        print(user_info_for_first_user_again.text)
        print("Status code:",user_info_for_first_user_again.status_code)

        # Данные для пользователя не изменились
        Assertions.assert_compare_two_jsons(ser_to_json_info_about_first_user, ser_to_json_info_about_first_user_again)


    # Попытаемся изменить firstName пользователя, будучи авторизованными тем же пользователем, на очень короткое значение в один символ
    def test_edit_username_for_just_created_user_on_short_user_name(self):
        # Создаём пользователя №1
        print("\n")
        print("Пожалуйста подождите, создаётся первый пользователь")
        datas = BaseCase.get_my_data(10, "@gmail.com")
        first_random_user = BaseCase.create_random_user(datas)
        Assertions.assert_good_client_status_code(first_random_user.status_code, first_random_user.text, datas)
        ser_to_json = json.loads(first_random_user.text)

        just_created_user_id = ser_to_json["id"]
        my_email = datas["email"]
        my_password = datas['password']

        # Логинимся под пользователем №1
        my_new_data = {
            'email':my_email,
            'password':my_password

        }
        login_by_first_created_user = MyRequests.send_request("POST", "api/user/login", data=my_new_data)
        print(f"Авторизовались под первым пользователем с ID {just_created_user_id} \n", login_by_first_created_user.text)
        print("Status code:",login_by_first_created_user.status_code)
        self.auth_sid = self.get_cookie(login_by_first_created_user, "auth_sid")
        self.token = self.get_header(login_by_first_created_user, "x-csrf-token")

        #GET получаем данные первого
        print("Получаем данные для первого")
        user_info_for_first_user = MyRequests.send_request("GET",
                                           f"api/user/{just_created_user_id}",
                                           headers={"x-csrf-token":self.token},
                                           cookies={"auth_sid":self.auth_sid}
                                           )
        Assertions.assert_good_client_status_code(user_info_for_first_user.status_code, user_info_for_first_user.text)

        print(user_info_for_first_user.text)
        print("Status code:",user_info_for_first_user.status_code)

        # Изменяем данные первого используя email без @
        print("Пожалуйста подождите, изменяется данные для второго пользователя авторизованным первым пользователем")

        my_data_for_change_first_user = BaseCase.get_my_data(1, "@rambler.com")

        result_by_change_email_for_current_user = MyRequests.send_request("PUT",
                                          f"api/user/{just_created_user_id}",
                                          headers={"x-csrf-token": self.token},
                                          cookies={"auth_sid": self.auth_sid},
                                          data=my_data_for_change_first_user
                                          )
        print("Изменили данные для первого пользака, email без символа @\n",
              result_by_change_email_for_current_user.text,
              "Status code:",result_by_change_email_for_current_user.status_code)

        ser_to_json_info_about_first_user_again = json.loads(result_by_change_email_for_current_user.text)
        extract_response_error = ser_to_json_info_about_first_user_again['error']

        # Проверили что нельзя изменить имя на столь короткое
        expected_answer = "Too short value for field username"
        Assertions.asserf_for_compare_two_response_text(expected_answer, extract_response_error)

        # Проверили что мыло не изменилось
        #Assertions.assert_for_edit_user_using_incorrect_email(result_by_change_email_for_second_user.text)

        print("Получаем данные для первого снова")
        user_info_for_first_user_again = MyRequests.send_request("GET",
                                           f"api/user/{just_created_user_id}",
                                           headers={"x-csrf-token":self.token},
                                           cookies={"auth_sid":self.auth_sid}
                                           )
        print(user_info_for_first_user_again.text)
        print("Status code:",user_info_for_first_user_again.status_code)
































