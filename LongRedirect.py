import requests

response = requests.get("https://playground.learnqa.ru/api/long_redirect", allow_redirects=True)

if response.history:
    print("Request was redirected")
    for resp in response.history:
        print(resp.status_code, resp.url)
    print("Final destination:")
    print(response.status_code, response.url)
else:
    print("Request was not redirected")