import selenium
import pytest
from selenium import webdriver
from selene.api import *


@pytest.fixture(autouse=True)
def driver_setup(request):
    selected_browser = request.config.getoption('--browser')
    print("___Selected browser is " + selected_browser)
    if selected_browser is 'chrome':
        config.browser_name = 'chrome'
    else:
        raise Exception("Incorrect browser name")


def pytest_addoption(parser):
    parser.addoption('--browser', action='store', default='chrome', help='Select browser to run test')
