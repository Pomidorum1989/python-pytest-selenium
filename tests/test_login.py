from datetime import datetime

import pytest

from pages.login_page import LoginPage
from pages.product_page import ProductPage
from utils.browser import BrowserFactory
from utils.config import Config
from utils.logger import test_logger

test_data = [
    ("standard_user", "secret_sauce"),
    ("locked_out_user", "secret_sauce"),
    ("problem_user", "secret_sauce"),
    ("performance_glitch_user", "secret_sauce"),
    ("error_user", "secret_sauce"),
    ("visual_user", "secret_sauce")
]


@pytest.fixture(params=test_data, scope='function')
def user_credentials(request):
    return request.param


@pytest.fixture(scope='function')
def setup_driver(request):
    driver = BrowserFactory.get_driver("chrome")
    driver.get(Config.BASE_URL)
    yield driver
    driver.quit()
    del BrowserFactory._local.driver  # Ensure the driver is removed from thread-local storage


def test_login(setup_driver, user_credentials):
    driver = setup_driver
    login_page = LoginPage(driver)
    username, password = user_credentials
    assert login_page.is_title_visible(), "Login title is not visible"
    login_page.enter_username(username)
    login_page.enter_password(password)
    login_page.take_screen_shot('login_' + username)
    login_page.click_login()
    assert not login_page.is_user_blocked(username), f"User is blocked with login {username}"
    product_page = ProductPage(driver)
    title = product_page.get_product_title_name()
    assert title == "Products", f"Incorrect page title value. Expected 'Products', got '{title}'"
    info = {
        'productNames': product_page.get_product_names(),
        'title': title,
        'username': username,
        'password': password
    }
    test_logger.info(info)
    product_page.click_menu_btn()
    product_page.click_log_out_btn()
    login_page.clear_username()
    login_page.clear_password()


if __name__ == "__main__":
    args = [
        "tests/",  # Directory where your tests are located
        "-v",  # Verbose mode
        "--html=reports/test_report.html",  # HTML report file location
        "--self-contained-html",  # Embed CSS and JavaScript in HTML
        "--maxfail=2",  # Limit displayed failures to 2
        "-n", "6",  # Run tests in parallel with 4 workers
        "--quiet"  # Suppress console output
    ]
    pytest.main(args)
