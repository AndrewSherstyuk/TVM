import selenium
import pytest
from selenium import webdriver
from selene.api import *
from allure_commons._allure import attach
from allure_commons.types import AttachmentType

import os
from pathlib import Path
import shutil
import subprocess
import time


@pytest.fixture(autouse=True)
def driver_setup(request):
    selected_browser = request.config.getoption('--browser')
    print("Selected browser is " + selected_browser)
    if selected_browser is 'chrome':
        config.browser_name = 'chrome'
    else:
        raise Exception("Incorrect browser name")
    config.timeout = 10


def pytest_addoption(parser):
    parser.addoption('--browser', action='store', default='chrome', help='Select browser to run test')

def pytest_exception_interact(node, call, report):
    from selene.browser import driver
    try:
        attach(
            driver().get_screenshot_as_png(),
            name="Screenshot",
            attachment_type=AttachmentType.PNG)
    except:
        pass
    browser.quit_driver()


""" session fixture. Prepares data for report generating at the end of session. """
@pytest.fixture(scope="session", autouse=True)
def report(request):
    brws = request.config.getoption('--browser')

    def prepare_report():
        print("\n")
        print("___PREPARING REPORT STARTED____")
        try:
            os.remove("./allure-results/environment.txt")
        except:
            pass

        try:
            os.remove("./allure-results/environment.properties")
        except:
            pass

        f = open("./allure-results/environment.txt", "w+")
        f.write("browser=" + brws + "\r\n")
        f.close()
        os.rename("./allure-results/environment.txt", "./allure-results/environment.properties")

        history = Path("./allure-report/history")
        if history.exists():
            if Path("./allure-results/history").exists():
                shutil.rmtree("./allure-results/history")
            shutil.copytree("./allure-report/history", "./allure-results/history")
        print("___REPORT DATA PREPARED___")

    request.addfinalizer(prepare_report)



