import allure

from lib.my_requests import MyRequests
import json
from lib.base_case import BaseCase
from lib.assertions import Assertions

class TestUserDelete(BaseCase):

    @allure.id("123") # Вывод айдишника конкретной задачи в Jira
    @allure.title("This test has a simple title") # Вывод title для конкретного теста
    @allure.feature('feature_2')
    @allure.story('story_2')
    @allure.severity(allure.severity_level.NORMAL) #Можно формировать по приоритету для регресса
    def test_delete_user_with_some_id(self):
        # Авторизуемся под пользователем
        my_new_data = BaseCase.data2
        my_id = BaseCase.id
        login_by_user = MyRequests.send_request("POST", "api/user/login", data=my_new_data)

        self.auth_sid = self.get_cookie(login_by_user, "auth_sid")
        self.token = self.get_header(login_by_user, "x-csrf-token")

        #GET получаем данные
        get_user_info = MyRequests.send_request("GET",
                                           f"api/user/{my_id}",
                                           headers={"x-csrf-token":self.token},
                                           cookies={"auth_sid":self.auth_sid}
                                           )

        Assertions.assert_good_client_status_code(get_user_info.status_code, get_user_info.text, my_id)

        # Удаляем пользователя с id == 2
        result = MyRequests.send_request("DELETE",
                                         f"api/user/{my_id}",
                                         headers={"x-csrf-token": self.token},
                                         cookies={"auth_sid": self.auth_sid}
                                         )
        Assertions.assert_delete_user_with_id_2(result.text)
        Assertions.assert_bad_client_status_code(result.status_code, result.text, my_id)

    @allure.id("123") # Вывод айдишника конкретной задачи в Jira
    @allure.title("This test has a simple title") # Вывод title для конкретного теста
    @allure.feature('feature_2')
    @allure.story('story_2')
    @allure.severity(allure.severity_level.NORMAL) #Можно формировать по приоритету для регресса
    def test_delete_just_created_user(self):
        # Создаём пользователя
        datas = BaseCase.get_my_data(5, "@gmail.com")
        random_user = BaseCase.create_random_user(datas)
        Assertions.assert_good_client_status_code(random_user.status_code, random_user.text, datas)
        ser_to_json = json.loads(random_user.text)

        just_created_user_id = ser_to_json["id"]
        my_email = datas["email"]
        my_password = datas['password']
        # Авторизуемся под ним
        my_new_data = {
            'email':my_email,
            'password':my_password

        }
        login_by_user = MyRequests.send_request("POST", "api/user/login", data=my_new_data)

        self.auth_sid = self.get_cookie(login_by_user, "auth_sid")
        self.token = self.get_header(login_by_user, "x-csrf-token")
        # Получаем данные
        get_user_info = MyRequests.send_request("GET",
                                           f"api/user/{just_created_user_id}",
                                           headers={"x-csrf-token":self.token},
                                           cookies={"auth_sid":self.auth_sid}
                                           )
        Assertions.assert_good_client_status_code(get_user_info.status_code, get_user_info.text, just_created_user_id)

        # Удаляем
        result = MyRequests.send_request("DELETE",
                                         f"api/user/{just_created_user_id}",
                                         headers={"x-csrf-token": self.token},
                                         cookies={"auth_sid": self.auth_sid}
                                         )

        Assertions.assert_good_client_status_code(result.status_code, result.text, just_created_user_id)

        # Получаем данные снова
        get_user_info_again = MyRequests.send_request("GET",
                                           f"api/user/{just_created_user_id}",
                                           headers={"x-csrf-token":self.token},
                                           cookies={"auth_sid":self.auth_sid}
                                           )
        Assertions.assert_not_found_delete_user(get_user_info_again.text)

    @allure.id("123") # Вывод айдишника конкретной задачи в Jira
    @allure.title("This test has a simple title") # Вывод title для конкретного теста
    @allure.feature('feature_2')
    @allure.story('story_2')
    @allure.severity(allure.severity_level.NORMAL) #Можно формировать по приоритету для регресса
    def test_delete_user_with_another_user_authorization_token(self):
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
        try:
            self.auth_sid = self.get_cookie(login_by_first_created_user, "auth_sid")
            self.token = self.get_header(login_by_first_created_user, "x-csrf-token")
        except:
            Assertions.assert_good_client_status_code(login_by_first_created_user.status_code, login_by_first_created_user.text, my_new_data)


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
        try:
            self.auth_sid2 = self.get_cookie(login_by_second_created_user, "auth_sid")
            self.token2 = self.get_header(login_by_second_created_user, "x-csrf-token")
        except:
            Assertions.assert_good_client_status_code(login_by_second_created_user.status_code, login_by_second_created_user.text, my_new_data2)


        #GET получаем данные второго
        print("Получаем данные для второго")
        user_info_for_second_user = MyRequests.send_request("GET",
                                           f"api/user/{just_created_user_id2}",
                                           headers={"x-csrf-token":self.token2},
                                           cookies={"auth_sid":self.auth_sid2}
                                           )
        Assertions.assert_good_client_status_code(user_info_for_second_user.status_code, user_info_for_second_user.text)
        ser_to_json_info_about_second_user = json.loads(user_info_for_second_user.text)
        print(user_info_for_second_user.text)
        print("Status code:",user_info_for_second_user.status_code)



        print("Пожалуйста подождите, удаляем второго пользователя авторизованным первым пользователем")
        result_by_delete_second_user = MyRequests.send_request("DELETE",
                                          f"api/user/{just_created_user_id2}",
                                          headers={"x-csrf-token": self.token},
                                          cookies={"auth_sid": self.auth_sid}
                                          )
        Assertions.assert_good_client_status_code(result_by_delete_second_user.status_code, result_by_delete_second_user.text, just_created_user_id2)
        print("Якобы удалили второго пользователю\n",
              result_by_delete_second_user.text,
              "Status code:",result_by_delete_second_user.status_code)


        # Снова получаем данные второго и первого пользователя
        print("Получаем данные для первого снова")
        user_info_for_first_user_again = MyRequests.send_request("GET",
                                           f"api/user/{just_created_user_id}",
                                           headers={"x-csrf-token":self.token},
                                           cookies={"auth_sid":self.auth_sid}
                                           )
        # Проверили что в действительности удалился пользователь первый а не второй
        Assertions.assert_not_found_delete_user(user_info_for_first_user_again.text)

        print(user_info_for_first_user_again.text)
        print("Status code:",user_info_for_first_user_again.status_code)

        print("Получаем данные для второго снова")
        user_info_for_second_user_again = MyRequests.send_request("GET",
                                           f"api/user/{just_created_user_id2}",
                                           headers={"x-csrf-token":self.token2},
                                           cookies={"auth_sid":self.auth_sid2}
                                           )
        Assertions.assert_good_client_status_code(user_info_for_second_user_again.status_code,
                                                  user_info_for_second_user_again.text)
        ser_to_json_info_about_second_user_again = json.loads(user_info_for_second_user.text)

        # Сверим тело ответа изначальное для пользака 2 и после удаления
        Assertions.assert_compare_two_jsons(ser_to_json_info_about_second_user,
                                            ser_to_json_info_about_second_user_again)
        print(user_info_for_second_user_again.text)
        print("Status code:",user_info_for_second_user_again.status_code)