import allure

import helpers
from data import ErrorMessage


@allure.story('Проверка получения списка заказов пользователя')
class TestReceiveUserOrders:

    @allure.title('Получение списка заказов пользователя')
    def test_receive_user_orders_autorized(self, user):
        response = helpers.get_order_list(user["json"]["accessToken"])
        assert response.status_code == 200
        assert len(response.json()) > 0

    @allure.title('Получение списка заказов неавторизованным пользователем')
    def test_receive_user_orders_not_autorized(self):
        response = helpers.get_order_list()
        assert response.status_code == 401
        assert response.json()['message'] == ErrorMessage.NOT_AUTHORIZED