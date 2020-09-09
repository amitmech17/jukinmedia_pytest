import pytest
from base.webdriverfactory import WebDriverFactory
from pages.loginpage.login_page import LoginPage
import time


# @pytest.yield_fixture()
# #@pytest.fixture()
# def setUp():
#     print("Running method level setUp")
#     yield
#     print("Running method level tearDown")


@pytest.yield_fixture(scope="function")
#@pytest.fixture(scope="class")
def oneTimeSetUp(request, browser,url):
    print("Running one time setUp")
    wdf = WebDriverFactory(browser)
    driver = wdf.getWebDriverInstance()
    driver.get(url)
    time.sleep(1)
    if request.cls is not None:
        request.cls.driver = driver
    yield driver
    driver.quit()
    print("Running one time tearDown")


def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--osType", help="Type of operating system")
    # parser.addoption("--email")
    # parser.addoption("--password")
    parser.addoption("--url")


@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")

@pytest.fixture(scope="session")
def osType(request):
    return request.config.getoption("--osType")

# @pytest.fixture(scope="session")
# def email(request):
#     return request.config.getoption("--email")
#
# @pytest.fixture(scope="session")
# def password(request):
#     return request.config.getoption("--password")

@pytest.fixture(scope="session")
def url(request):
    return request.config.getoption("--url")