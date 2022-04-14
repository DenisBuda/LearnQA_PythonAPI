import json.decoder
from requests import Response
import random
import string

class BaseCase:
    def get_cookie(self, response: Response, cookie_name):
        assert cookie_name in response.cookies, f"Cannot find cookie with name {cookie_name}"
        return response.cookies[cookie_name]

    def get_header(self, response: Response, headers_name):
        assert headers_name in response.headers, f"Cannot find header {headers_name}"
        return response.headers[headers_name]

    def get_json_value(self, response: Response, name):
        try:
            response_as_dict = response.json()
        except json.decoder.JSONDecodeError:
            assert False, f"Response not in json format. Json text is {json.text}"

        assert name in response_as_dict, f"Response JSON doesn't have key {name}"
        return response_as_dict[name]

    @staticmethod
    def random_char(length):
        return ''.join(random.choice(string.ascii_letters) for x in range(length))

    def get_my_data(length_of_rnd_chars,
                    mailbox:str):
        my_data = {
            "username": BaseCase.random_char(length_of_rnd_chars),
            "firstName": BaseCase.random_char(length_of_rnd_chars),
            "lastName": BaseCase.random_char(length_of_rnd_chars),
            "email": BaseCase.random_char(7) + f"{mailbox}",
            "password": BaseCase.random_char(10)
        }
        return my_data

    my_data_new = [
        # Without username
        {"firstName": random_char(9),
         "lastName": random_char(9),
         "email": random_char(7) + f"@gmail.com",
         "password": random_char(9)+"\n"},
        # Without firstName
        {"username": random_char(9),
         "lastName": random_char(9),
         "email": random_char(7) + f"@gmail.com",
         "password": random_char(9)+"\n"},
        # Without lastName
        {"username": random_char(9),
         "firstName": random_char(9),
         "email": random_char(7) + f"@gmail.com",
         "password": random_char(9)+"\n"},
        # Without email
        {"firstName": random_char(9),
         "lastName": random_char(9),
         "username": random_char(9),
         "password": random_char(9)+"\n"},
        # Without password
        {"username": random_char(9),
         "lastName": random_char(9),
         "email": random_char(7) + f"@gmail.com",
         "firstName": random_char(9)+"\n"}
    ]




