import requests
import requests

class MyRequests:
    @staticmethod
    def send_request(method:str, url:str, data:dict = None, cookies:dict = None, headers:dict = None):
        url = f"https://playground.learnqa.ru/{url}"

        if method == "GET":
            response = requests.get(url=url, params=data, cookies=cookies, headers=headers)
        elif method == "POST":
            response = requests.post(url=url, data=data, cookies=cookies, headers=headers)
        elif method == "PUT":
            response = requests.post(url=url, data=data, cookies=cookies, headers=headers)
        elif method == "DELETE":
            response = requests.post(url=url, data=data, cookies=cookies, headers=headers)
        else:
            raise Exception(f"Bad HTTP method 'method' was received")

        return response

