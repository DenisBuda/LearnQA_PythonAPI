import requests

# Ex3: Создание репозитория
print('Hello from Denis')

#Ex4: GET-запрос
response = requests.get('https://playground.learnqa.ru/api/get_text')
print(response.text)

