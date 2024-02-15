import allure
import pytest

from http import HTTPStatus

from data import MessageText
from helpers import BaseMethods, CheckMethods #, GenerateUser
from urls import Urls


@allure.feature("Проверка получения заказа пользователя")
class TestOrderGet:
    @allure.title("Проверка заказа авторизованного пользователя")
    @allure.description("Запрос от существующего пользователя"
                        "статус ответа 200 и текста ответа True")
    def test_get_order_authorized_user(self, create_user_and_del, create_order):
        response = BaseMethods.get_request(Urls.ORDER,
                                              token=create_user_and_del[1].json()['accessToken'])
        CheckMethods.check_status_code(response, HTTPStatus.OK)
        CheckMethods.check_message_json(response, MessageText.SUCCESS_KEY, MessageText.SUCCESS_OPERATION)

    @allure.title("Проверка невозможности сделать заказ неавторизованным пользователем")
    @allure.description("Запрос от неавторизованного пользователя, статус ответа 401 и текста ответа 'You "
                        "should be authorised'")
    def test_get_order_of_unauthorized_user(self, create_user_and_del, create_order):
        response = BaseMethods.get_request(Urls.ORDER)
        CheckMethods.check_status_code(response, HTTPStatus.UNAUTHORIZED)
        CheckMethods.check_message_json(response, MessageText.MESSAGE_KEY, MessageText.NOT_AUTHORIZED)
