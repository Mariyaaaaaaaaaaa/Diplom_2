import allure
import pytest

from http import HTTPStatus

from data import MessageText, GenerateUser
from helpers import BaseMethods, CheckMethods
from urls import Urls

from conftest import *


@allure.feature("Проверка создания заказа")
class TestOrderCreate:

    @allure.title("Параметризированная проверка создания заказа авторизированных пользователей")
    @allure.description("Запросы авторизованного пользователя с ингредиентами и без ингредиентов возвращают "
                        "ответ с кодом 200/400 и текстом ответа 'True'/'False'")
    @pytest.mark.parametrize('ingredients, status_code, text_answer',
                             [(Order.INGREDIENTS, HTTPStatus.OK, MessageText.SUCCESS_OPERATION),
                              (Order.INGREDIENTS_EMPTY, HTTPStatus.BAD_REQUEST, MessageText.FALSE_OPERATION)],
                             ids=["with_ingredients", "without_ingredients"])
    def test_create_order_exist_user(self, create_user_and_del, ingredients, status_code, text_answer):
        order_payment = {"ingredients": ingredients}
        response = BaseMethods.post_request(Urls.ORDER, order_payment,
                                            create_user_and_del[1].json()['accessToken'])
        CheckMethods.check_status_code(response, status_code)
        CheckMethods.check_message_json(response, MessageText.SUCCESS_KEY, text_answer)

    @allure.title("Параметризированная проверка создания заказа неавторизированного пользователя с ингредиентами и "
                  "без ингредиентов")
    @allure.description("Запросы неавторизованного пользователя c ингредиентами и без ингредиентов, "
                        "возвращают ответ с кодом 200/400 и текстом ответа 'True'/'False'")
    @pytest.mark.parametrize('ingredients, status_code, text_answer',
                             [(Order.INGREDIENTS, HTTPStatus.OK, MessageText.SUCCESS_OPERATION),
                              (Order.INGREDIENTS_EMPTY, HTTPStatus.BAD_REQUEST, MessageText.FALSE_OPERATION)],
                             ids=["with_ingredients", "without_ingredients"])
    def test_create_order_unauthorized_no_ingredients(self, ingredients, status_code, text_answer):
        order_payment = {"ingredients": ingredients}
        response = BaseMethods.post_request(Urls.ORDER, order_payment)
        CheckMethods.check_status_code(response, status_code)
        CheckMethods.check_message_json(response, MessageText.SUCCESS_KEY, text_answer)

    @allure.title("Проверка создания заказа авторизированного пользователя с неправильным ингредиентом")
    @allure.description("Запрос с авторизацией с несуществующим ингредиентом, возвращает ошибку "
                        "с кодом 500 и текстом ответа 'Internal Server Error'")
    def test_create_order_authorized_ingredients_error(self, create_user_and_del):
        order_payment = {"ingredients": Order.INGREDIENTS_ERROR}
        response = BaseMethods.post_request(Urls.ORDER, order_payment,
                                            create_user_and_del[1].json()['accessToken'])
        CheckMethods.check_status_code(response, HTTPStatus.INTERNAL_SERVER_ERROR)
        CheckMethods.check_message_text(response, MessageText.SERVER_ERROR)

    @allure.title("Проверка создания заказа для неавторизированного пользователя с неправильным игредиентом")
    @allure.description("Запрос неавторизованного пользователя с несуществующим ингредиентом возвращает ошибку "
                        "с кодом 500 и текстом ответа 'Internal Server Error'")
    def test_create_order_unauthorized_ingredients_error(self):
        order_payment = {"ingredients": Order.INGREDIENTS_ERROR}
        response = BaseMethods.post_request(Urls.ORDER, order_payment)
        CheckMethods.check_status_code(response, HTTPStatus.INTERNAL_SERVER_ERROR)
        CheckMethods.check_message_text(response, MessageText.SERVER_ERROR)
