import os

import pytest
from dotenv import load_dotenv
from selene.support.shared import browser

from framework.demoqa import DemoQaWithEnv

load_dotenv()


def pytest_addoption(parser):
    parser.addoption("--env", action='store', default="prod")


@pytest.fixture(scope='session')
def env(request):
    return request.config.getoption("--env")


@pytest.fixture(scope='session')
def demowebshop(env):
    return DemoQaWithEnv(env)


@pytest.fixture(scope='session')
def cookie(demowebshop):
    response = demowebshop.login(os.getenv("LOGIN"), os.getenv("PASSWORD"))
    authorization_cookie = response.cookies.get("NOPCOMMERCE.AUTH")
    return authorization_cookie


@pytest.fixture(scope='function')
def app(demowebshop, cookie):
    browser.config.base_url = demowebshop.demoqa.url
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    browser.open("Themes/DefaultClean/Content/images/logo.png")
    browser.driver.add_cookie({"name": "NOPCOMMERCE.AUTH", "value": cookie})
    yield browser
    browser.quit()


@pytest.fixture(scope='session')
def reqres(env):
    return DemoQaWithEnv(env).reqres
