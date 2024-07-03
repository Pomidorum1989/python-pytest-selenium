import os

import pytest
from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utils.logger import test_logger


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def find_element(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def find_elements(self, locator):
        return self.wait.until(EC.visibility_of_all_elements_located(locator))

    def click(self, locator):
        self.find_element(locator).click()

    def enter_text(self, locator, text):
        self.find_element(locator).send_keys(text)

    def clear_text(self, locator):
        self.find_element(locator).clear()

    def get_text(self, arg):
        return self.find_element(arg).text

    def get_text_web_element(self, arg):
        if isinstance(arg, WebElement):
            return arg.text

    def is_visible(self, locator):
        return self.find_element(locator).is_displayed()

    def is_element_not_displayed(self, locator):
        try:
            WebDriverWait(self.driver, 10).until_not(EC.visibility_of_element_located(locator))
            return True
        except (TimeoutException, NoSuchElementException):
            return False

    def take_screen_shot(self, file_name):
        screenshot_path = os.path.join(os.getcwd(), "screenshots")
        os.makedirs(screenshot_path, exist_ok=True)
        screenshot_file = os.path.join(screenshot_path, f"{file_name}.png")
        self.driver.save_screenshot(screenshot_file)
        test_logger.info("Screenshot was taken %s", file_name)
