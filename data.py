from dataclasses import dataclass
from faker import Faker


class GenerateUser:
    @staticmethod
    def creat_user():
        fake = Faker()
        user = {"email": fake.email(),
                "password": fake.password(),
                "name": fake.user_name()}
        return user


@dataclass
class UserData:
    EMAIL: str = "shcherbakova_sun999@yandex.ru"
    PASSWORD: str = "2421484"
    ERROR_EMAIL: str = "kjvknkskf_999@yandex.ru"
    ERROR_PASSWORD: str = "edwf43df"
    NAME: str = "tim"
    NEW_NAME: str = GenerateUser.creat_user()["name"]
    NEW_EMAIL: str = GenerateUser.creat_user()["email"]
    NEW_PASSWORD: str = GenerateUser.creat_user()["password"]


class MessageText:
    SUCCESS_OPERATION = True
    FALSE_OPERATION = False
    SUCCESS_KEY = 'success'
    MESSAGE_KEY = 'message'
    USER_NAME_KEY = []
    SERVER_ERROR = "Internal Server Error"
    NOT_AUTHORIZED = "You should be authorised"
    USER_ALREADY_EXISTS = 'User already exists'
    INVALID_DATA = "email or password are incorrect"
    REQUIRED_FIELD = "Email, password and name are required fields"


class Order:
    INGREDIENTS = ["61c0c5a71d1f82001bdaaa70", "61c0c5a71d1f82001bdaaa71"]
    INGREDIENTS_ERROR = ["89bffh124lw3efj"]
    INGREDIENTS_EMPTY = ""
