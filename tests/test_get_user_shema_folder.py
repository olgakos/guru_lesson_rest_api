import requests
from pytest_voluptuous import S
from requests import Response
from voluptuous import Schema, PREVENT_EXTRA

#https://reqres.in/
# 3 course

# сшема шаг 1 (описываем, заполенем данными из ответа "data")
from schemas.user import get_single_user_schema


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
    response = requests.get("https://reqres.in/api/users/2")
    assert S(schema) == response.json()


#сшема шаг 3 перенос в папку
def test_get_users_schema3():
    #кусок унесен в папку shcema
    response = requests.get("https://reqres.in/api/users/2")
    assert S(get_single_user_schema) == response.json()