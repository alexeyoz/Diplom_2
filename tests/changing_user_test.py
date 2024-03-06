import allure
import pytest
import requests

import helpers
from data import Url, ErrorMessage


@allure.story('Проверка изменения пользователя')
class TestChangingUser:
    @allure.title('Проверка изменения пользователя')
    @pytest.mark.parametrize('test', ['name', 'email', 'password'])
    def test_can_change_user(self, user, test):
        payload = {test: 'new_' + test}
        response = requests.patch(Url.AUTH_USER, data=payload, headers={'Authorization': user["json"]["accessToken"]})
        assert response.status_code == 200
        assert response.json()['success']

    @allure.title('Проверка запрета изменения данных неавторизованного пользователя')
    @pytest.mark.parametrize('test', ['name', 'email', 'password'])
    def test_can_not_change_user(self, user, test):
        payload = {test: helpers.create_test_user()}
        response = requests.patch(Url.AUTH_USER, data=payload)
        assert response.status_code == 401
        assert response.json()['message'] == ErrorMessage.NOT_AUTHORIZED