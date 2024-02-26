import allure

import helpers
from data import Ingredients, ErrorMessage


@allure.story('Проверка создания заказа')
class TestCreatingOrder:

    @allure.title('Создание заказа')
    def test_creating_order_autorized(self, user):
        response = helpers.creating_order(Ingredients.INGREDIENTS, user["json"]["accessToken"])
        assert response.status_code == 200

    @allure.title('Создание заказа неавторизованным пользователем')
    def test_creating_order_not_autorized(self):
        response = helpers.creating_order(Ingredients.INGREDIENTS)
        assert response.status_code == 200

    @allure.title('Создание заказа без ингредиентов')
    def test_creating_order_not_ingredients(self):
        response = helpers.creating_order('')
        assert response.status_code == 400
        assert response.json()['message'] == ErrorMessage.INGREDIENTS_NOT_PROVIDED

    @allure.title('Создание заказа с некорректными ингредиентами')
    def test_creating_order_incorrect_ingredients(self):
        response = helpers.creating_order('60d3463f7034a000269f45e7')
        assert response.status_code == 400
        assert response.json()['message'] == ErrorMessage.INGREDIENTS_PROVIDED_INCORRECT