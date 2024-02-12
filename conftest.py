import pytest
from urls import Urls
from data import Order, GenerateUser
from helpers import BaseMethods


@pytest.fixture
def create_user_and_del():
    user_data = GenerateUser.creat_user()
    response = BaseMethods.post_request(Urls.USER_CREATE, user_data)
    yield user_data, response
    BaseMethods.del_request(Urls.USER_DELETE_CHANGE_INFO,
                            response.json()['accessToken'])


@pytest.fixture
def create_order(create_user_and_del):
    order_payment = {"ingredients": Order.INGREDIENTS}
    response = BaseMethods.post_request(Urls.ORDER, order_payment,
                                        create_user_and_del[1].json()['accessToken'])
    return response
