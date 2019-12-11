import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption('--browser', action='store', default=None,
                     help="Choose browser: Chrome or Firefox")


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser")
    browser = None
    if browser_name == "Chrome":
        print("\nstart chrome browser for test..")
        browser = webdriver.Chrome()
    elif browser_name == "Firefox":
        print("\nstart firefox browser for test..")
        browser = webdriver.Firefox()
    else:
        raise pytest.UsageError("--browser should be chrome or firefox")
    yield browser
    print("\nquit browser..")
    browser.quit()
