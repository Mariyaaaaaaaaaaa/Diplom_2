import allure
import pytest

from http import HTTPStatus

from data import MessageText, GenerateUser
from helpers import BaseMethods, CheckMethods
from urls import Urls

from conftest import *


@allure.feature("Проверка создания пользователя")
class TestCreateUser:

    @allure.title("Проверка успешного создания пользователя")
    @allure.description("Запрос создания нового пользователя с валидными данными (наличие email/пароля/имени) "
                        "возвращает успешный код ответа 200 и текста ответа True")
    def test_user_create_success(self):
        response = BaseMethods.post_request(Urls.USER_CREATE,
                                            GenerateUser.creat_user())
        CheckMethods.check_status_code(response, HTTPStatus.OK)
        CheckMethods.check_message_json(response, MessageText.SUCCESS_KEY, MessageText.SUCCESS_OPERATION)

    @allure.title("Проверка невозможности создания пользователя с существующим логином")
    @allure.description("Запрос на создание пользователя, который уже существует в системе, возвращает ошибку "
                        "с кодом 403 и текстом ответа 'User already exists'")
    def test_create_user_existed_login(self, create_user_and_del):
        response = BaseMethods.post_request(Urls.USER_CREATE,
                                            create_user_and_del[0])
        CheckMethods.check_status_code(response, HTTPStatus.FORBIDDEN)
        CheckMethods.check_message_json(response, MessageText.MESSAGE_KEY, MessageText.USER_ALREADY_EXISTS)

    @allure.title("Параметризированная проверка невозможности создания пользователя без заполнения обязательного поля "
                  "email/пароль/имя")
    @allure.description("Запрос создания нового пользователя с невалидными данными (без email/пароля/имени), "
                        "возвращает ошибку с кодом 403 и текстом ответа 'Email, password and name are required fields'")
    @pytest.mark.parametrize('email, password, name',
                             [(GenerateUser.creat_user()['email'], GenerateUser.creat_user()['password'],
                               None),
                              (GenerateUser.creat_user()['email'], None, GenerateUser.creat_user()['name']),
                              (None, GenerateUser.creat_user()['password'],
                               GenerateUser.creat_user()['name'])],
                             ids=['without_email', 'without_password', 'without_name'])
    def test_create_user_without_required_field(self, email, password, name):
        payload_user_data = {"email": email,
                             "password": password,
                             "name": name}
        response = BaseMethods.post_request(Urls.USER_CREATE, payload_user_data)
        CheckMethods.check_status_code(response, HTTPStatus.FORBIDDEN)
        CheckMethods.check_message_json(response, MessageText.MESSAGE_KEY, MessageText.REQUIRED_FIELD)
