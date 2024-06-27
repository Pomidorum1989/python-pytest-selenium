
from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from utils.logger import test_logger


class LoginPage(BasePage):
    USERNAME_FIELD = (By.ID, "user-name")
    PASSWORD_FIELD = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    LOGIN_TITLE = (By.XPATH, "//div[@class = 'login_logo']")
    USER_NAMES = (By.XPATH, "//div[@id = 'login_credentials']")
    PASSWORD_VALUE = (By.XPATH, "//div[@class = 'login_password']")
    ERROR_VALUE = (By.XPATH, "//h3[@data-test = 'error']")

    def enter_username(self, username):
        test_logger.info("Entering username: %s", username)
        self.enter_text(self.USERNAME_FIELD, username)

    def clear_username(self):
        test_logger.info("Cleared username")
        self.clear_text(self.USERNAME_FIELD)

    def enter_password(self, password):
        test_logger.info("Entering password: %s", password)
        self.enter_text(self.PASSWORD_FIELD, password)

    def clear_password(self):
        test_logger.info("Cleared password")
        self.clear_text(self.PASSWORD_FIELD)

    def click_login(self):
        test_logger.info("Clicked login btn")
        self.click(self.LOGIN_BUTTON)

    def is_title_visible(self):
        return self.is_visible(self.LOGIN_TITLE)

    def is_user_blocked(self, user_name):
        is_blocked = self.is_element_not_displayed(self.ERROR_VALUE)
        if not is_blocked:
            self.take_screen_shot(f"User is blocked for login {user_name}")
            test_logger.info("Reason: " + self.get_text(self.ERROR_VALUE))
        return not is_blocked

    def get_usernames(self):
        username = self.get_text(self.USER_NAMES)
        test_logger.info("Current username is %s", username)
        return username

    def get_password(self):
        password = self.get_text(self.PASSWORD_VALUE)
        test_logger.info("Current password is %s", password)
        return password
