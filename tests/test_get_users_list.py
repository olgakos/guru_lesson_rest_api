import logging
import requests
from pytest_voluptuous import S
from requests import Response
from voluptuous import Schema, PREVENT_EXTRA

#https://reqres.in/
# 3 course

import requests
from pytest_voluptuous import S


from schemas.user import users_list_schema


def test_get_users_list_schema_base():
    result = requests.get("https://reqres.in/api/users?page=2")

    assert S(users_list_schema) == result.json()


def test_get_users_list_schema():
    # кол-во записей на странице №2
    result = requests.get("https://reqres.in/api/users", params={"page": 2})
    print(result.text) # [100%]{"page":2,"per_page":6,"total":12,"total_pages":2,"data":[{"id":7,.....

    assert S(users_list_schema) == result.json()

def test_get_users_list_schema_with_logs():
    # кол-во записей на странице №2
    result = requests.get("https://reqres.in/api/users", params={"page": 2})
    logging.info(result.text)  # перчать логирование (+ pytest.ini)

    assert S(users_list_schema) == result.json()

def test_users_default_count_on_page():
    """Проверка дефолтного количества пользователей на странице."""
    response = requests.get("https://reqres.in/api/users", params={"page": 1})
    per_page = response.json()["per_page"]
    data = response.json()["data"]

    assert per_page == 6
    assert len(data) == 6