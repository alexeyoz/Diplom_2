import allure
import pytest
import helpers
from data import ErrorMessage


@allure.story('Проверка авторизации пользователя')
class TestLoginUser:
    @allure.title('Авторизация под существующим пользователем')
    def test_can_login_user(self, user):
        response = helpers.login_user(user["email"], user["password"])
        assert response.status_code == 200
        assert response.json()['success']

    @allure.title('Авторизация с неверным логином и паролем')
    @pytest.mark.parametrize('email, password', [['', 'password'], ['email', '']])
    def test_login_user_not_enough_data(self, email, password):
        response = helpers.login_user(email, password)

        assert response.status_code == 401
        assert response.json()['message'] == ErrorMessage.INCORRECT_LOGIN_PASSWORD
