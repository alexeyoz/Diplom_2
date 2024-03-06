import allure
from faker import Faker
from data import Url

import requests


@allure.step(f'Генерация имени')
def create_name():
    name = Faker().first_name()
    return name


@allure.step(f'Генерация пароля')
def create_password():
    password = Faker().password(length=10)
    return password


@allure.step(f'Генерация email')
def create_email():
    email = Faker().first_name() + '@mail.ru'
    return email


@allure.step(f'Создание пользователя')
def create_test_user():
    email = create_email()
    password = create_password()
    name = create_name()
    payload = {
        'email': email,
        'password': password,
        'name': name
    }

    response = requests.post(Url.CREATE_USER, data=payload)

    test_user_data = {
        "email": email,
        "name": name,
        "password": password,
        "json": response.json()
    }

    return test_user_data


@allure.step(f'Авторизация пользователя')
def login_user(email, password):
    payload = {
        'email': email,
        'password': password
    }
    response = requests.post(Url.LOGIN_USER, data=payload)
    return response


@allure.step(f'Удаление пользователя')
def del_user(access_token):
    response = requests.delete(Url.AUTH_USER, headers={'Authorization': access_token})
    return response.json()


@allure.step(f'Создание заказа')
def creating_order(ingredients, access_token=None):
    payload = {"ingredients": [ingredients]}
    response = requests.post(Url.ORDER, data=payload, headers={'Authorization': access_token})
    return response


@allure.step(f'Получение списка заказов')
def get_order_list(access_token=None):
    response = requests.get(Url.ORDER, headers={'Authorization': access_token})
    return response
