import os
import sys

import pytest

from saucedemo.PageObject.homepage import  HomePage
from saucedemo.PageObject.logIn_page import LoginPage
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))


def test_e2e(driver):
    login = LoginPage(driver)
    homepage = HomePage(driver)

    login.enter_username("standard_user")
    login.enter_password("secret_sauce")
    login.click_login()
    homepage.sort_products("lohi")
    homepage.get_items("inventory_item")

