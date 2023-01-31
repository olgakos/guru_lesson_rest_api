from msilib import schema
from pprint import pprint
import requests
from pytest_voluptuous import S
from requests import Response

from voluptuous import Schema, PREVENT_EXTRA

#https://reqres.in/
# 3 course

#Step 1
response = requests.get(url="https://reqres.in/api/users")
print(response)
#<Response [200]>

#Step 2 после импорта (from requests import Response)
# появились многие новые возможности “представления ответа”,
# см МНОГО разных методов из (response.***)
response: Response = requests.get(url="https://reqres.in/api/users")
print(response.headers) #{'Date': 'Tue, 31 Jan 2023 09:34:35 GMT', 'Content-Type': 'application/json; charset=utf-8', ... }
print(response.elapsed) #сколько времени заняло выполение 0:00:00.111713
print(response.text) #{"page":1,"per_page":6,"total":12,"total_pages":2,"data":[{"id":1,"email":"george.......

#Step 3 Test with Assert
def test_get_users():
    response: Response = requests.get(url='https://reqres.in/api/users/2')
    print(response.status_code)
    pprint(response.request.headers)
    # проверяем 200:
    assert response.status_code == 200 #сравненеи с ожидаемым
    # проверяем id:
    assert response.json()["data"]["id"] == 2  #json возвращает словари, в них ключи
    # проверяем mail:
    assert response.json()["data"]["email"] == "janet.weaver@reqres.in" #json возвращает словари, в них ключи
    # проверяем данные не пустые:
    assert len(response.json()['data']) != 0

def test_avatar():
    response: Response = requests.get(url='https://reqres.in/api/users/2')
    print(response.status_code)
    avatar = response.json().get("data").get("avatar", None) #... аватра1 нет
    # проверяем аватарку:
    assert response.json()["data"]["avatar"] == "https://reqres.in/img/faces/2-image.jpg"
    # проверяем аватарку переемнная avatar (??) 27_00+ пи3
    assert avatar

#проверяем, что 1 шт поле аватар ИМЕЕТСЯ
def test_get_users_has_avatar_field():
    response: Response = requests.get(url="https://reqres.in/api/users/2")
    assert response.status_code == 200
    assert response.json().get("data").get("avatar", None)

#проверяем, что 1 шт поле аватар НЕ пусто
def test_avatar_exists():
    response: Response = requests.get(url='https://reqres.in/api/users/2')
    avatar = response.json().get("data").get("avatar", None)
    result = requests.get(avatar)
    assert result.status_code == 200
    assert len(response.content) != 0 #длина контената !=0
    assert len(response.content) == 280 #длина контената = 280пикс

# сшема шаг 1 (описываем, заполенем данными из ответа "data")
def test_get_users_schema1():
    schema = Schema(
        {
            "data":
                {
                    "id": 2,
                    "email": "janet.weaver@reqres.in",
                    "first_name": "Janet",
                    "last_name": "Weaver",
                    "avatar": "https://reqres.in/img/faces/2-image.jpg"
                },
            "support":
                {
                    "url": "https://reqres.in/#support-heading",
                    "text": "To keep ReqRes free, contributions towards server costs are appreciated!"
                }
        }
    )
    response = requests.get("https://reqres.in/api/users/2")



#сшема шаг 2 обезличиваем и сравниваем данные
def test_get_users_schema2():
    schema = Schema(
        {
            "data":
                {
                    "id": int,
                    "email": str,
                    "first_name": str,
                    "last_name": str,
                    "avatar": str
                },
            "support":
                {
                    "url": str,
                    "text": str
                }
        }
        ,
        required = True, #фиксируем, что все перечисленыне поля ОБЯЗАТЕЛЬНЫН
        extra = PREVENT_EXTRA, #что это уточнить?
    )
    print()
    response = requests.get("https://reqres.in/api/users/2")
    assert S(schema) == response.json()

