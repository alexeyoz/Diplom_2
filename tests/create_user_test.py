import pytest
from data import ErrorMessage
import allure
from helpers import *


@allure.story('Проверка создания пользователя')
class TestCreateUser:

    @allure.title('Создание уникального пользователя')
    def test_create_user(self):
        email = create_email()
        password = create_password()
        name = create_name()
        payload = {
            'email': email,
            'password': password,
            'name': name
        }
        response = requests.post(Url.CREATE_USER, data=payload)
        assert response.status_code == 200

    @allure.title('Создание пользователя, который уже зарегистрирован')
    def test_create_user_exists(self):
        payload = {
            'email': 'email',
            'password': 'password',
            'name': 'name'
        }
        response = requests.post(Url.CREATE_USER, data=payload)
        assert response.status_code == 403
        assert response.json()['message'] == ErrorMessage.USER_EXISTS

    @allure.title('Создание пользователя без одного из обязательных полей.')
    @pytest.mark.parametrize('email, password, name',
                             [['', 'create_email', 'create_email'],
                              ['create_password', '', 'create_password'],
                              ['create_name', 'create_name', '']])
    def test_creating_user_not_enough_data(self, email, password, name):
        payload = {
            'email': email,
            'password': password,
            'name': name
        }

        response = requests.post(Url.CREATE_USER, data=payload)
        assert response.status_code == 403
        assert response.json()['message'] == ErrorMessage.NOT_ALL_FIELDS
