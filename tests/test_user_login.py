import pytest
import allure

from data import MessageText, UserData
from http import HTTPStatus

from urls import Urls
from helpers import BaseMethods, CheckMethods
from conftest import *



@allure.feature("Проверка входа в систему")
class TestLoginUser:

    @allure.title("Проверка успешного входа в систему")
    @allure.description("Запрос на авторизацию с корректными email и паролем возвращает код ответа 200"
                        "и текст ответа 'True'")
    def test_user_login_success(self, create_user_and_del):
        user_data = {"email": create_user_and_del[0]["email"],
                     "password": create_user_and_del[0]["password"]}
        response = BaseMethods.post_request(Urls.USER_LOGIN, user_data)
        CheckMethods.check_status_code(response, HTTPStatus.OK)
        CheckMethods.check_message_json(response, MessageText.SUCCESS_KEY, MessageText.SUCCESS_OPERATION)

    @allure.title("Параметризированная проверка невозможности авторизации пользователя с некорректным логином/паролем")
    @allure.description("Запросы с корректным email и некорректным паролем,"
                        "некорректным email и корректным паролем, возвращают ошибку с кодом 401 и текстом ответа "
                        "'email or password are incorrect'")
    @pytest.mark.parametrize("email, password", [(UserData.EMAIL, UserData.ERROR_PASSWORD),
                                                 (UserData.ERROR_EMAIL, UserData.PASSWORD)],
                             ids=['ERROR_PASSWORD', 'ERROR_EMAIL'])
    def test_authorized_error_data(self, email, password):
        user_data = {"email": email,
                     "password": password}
        response = BaseMethods.post_request(Urls.USER_LOGIN, user_data)
        CheckMethods.check_status_code(response, HTTPStatus.UNAUTHORIZED)
        CheckMethods.check_message_json(response, MessageText.MESSAGE_KEY, MessageText.INVALID_DATA)
