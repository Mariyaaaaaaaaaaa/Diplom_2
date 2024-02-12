import allure
import pytest

from http import HTTPStatus

from data import MessageText, UserData, GenerateUser
from helpers import BaseMethods, CheckMethods
from urls import Urls

from conftest import *


@allure.feature("Проверка изменения пользователя")
class TestChangeUserData:

    @allure.title("Проверка успешного изменения данных пользователя")
    @allure.description("Запросы авторизованного пользователя на изменения данных возвращает ответ с кодом 200"
                        "и текстом ответа 'True'")
    @pytest.mark.parametrize('key_field, new_data', [("name", UserData.NEW_NAME),
                                                     ("password", UserData.NEW_PASSWORD),
                                                     ("email", UserData.NEW_EMAIL)],
                             ids=["change_name", "change_password", "change_email"])
    def test_change_user_data_success(self, create_user_and_del, key_field, new_data):
        payload_data = {key_field: new_data}
        response = BaseMethods.patch_request(Urls.USER_DELETE_CHANGE_INFO, payload_data,
                                             create_user_and_del[1].json()['accessToken'], )
        CheckMethods.check_status_code(response, HTTPStatus.OK)
        CheckMethods.check_message_json(response, MessageText.SUCCESS_KEY, MessageText.SUCCESS_OPERATION)

    @allure.title("Параметризированная проверка получения ошибки изменения данных неавторизованного пользователя")
    @allure.description("Запросы неавторизованного пользователя на изменения данных возвращает ошибку с кодом 401"
                        "и текстом ответа 'You should be authorised'")
    @pytest.mark.parametrize('key_field, new_data', [("name", UserData.NEW_NAME),
                                                     ("password", UserData.NEW_PASSWORD),
                                                     ("email", UserData.NEW_EMAIL)],
                             ids=["change_name", "change_password", "change_email"])
    def test_change_user_data_not_authorized(self, create_user_and_del, key_field, new_data):
        payload_data = {key_field: new_data}
        response = BaseMethods.patch_request(Urls.USER_DELETE_CHANGE_INFO, payload_data)
        CheckMethods.check_status_code(response, HTTPStatus.UNAUTHORIZED)
        CheckMethods.check_message_json(response, MessageText.MESSAGE_KEY, MessageText.NOT_AUTHORIZED)
