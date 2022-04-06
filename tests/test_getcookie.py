import requests

class TestGetMyCookie:
    def setup(self):
        self.etalon_cookie = "hw_value"

    def test_get_cookies(self):
        url = "https://playground.learnqa.ru/api/homework_cookie"
        response = requests.get(url)
        print(response.cookies)
        my_cookie = response.cookies.get("HomeWork")
        print(f"The value of cookie is: {my_cookie}")
        assert my_cookie != None, "Error! Cookies are empty"
        assert my_cookie == self.etalon_cookie, "Error! Invalid cookie received"