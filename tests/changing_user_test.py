import allure
import pytest
import requests

from data import Url, ErrorMessage


@allure.story('Проверка изменения пользователя')
class TestChangingUser:
    @allure.story('Проверка изменения пользователя')
    @pytest.mark.parametrize('test', ['name', 'email', 'password'])
    def test_can_change_user(self, user, test):
        payload = {test: 'new_' + test}
        response = requests.patch(Url.AUTH_USER, data=payload, headers={'Authorization': user["json"]["accessToken"]})
        assert response.status_code == 200

    @allure.story('Проверка изменения неавторизованного пользователя')
    @pytest.mark.parametrize('test', ['name', 'email', 'password'])
    def test_can_not_change_user(self, test):
        payload = {test: 'new_' + test}
        response = requests.patch(Url.AUTH_USER, data=payload)
        assert response.status_code == 401
        assert response.json()['message'] == ErrorMessage.NOT_AUTHORIZED
