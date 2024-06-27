import logging

from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from utils.logger import test_logger


class ProductPage(BasePage):
    PRODUCT_TITLE = (By.XPATH, "//span[@data-test='title']")
    PRODUCT_NAMES = (By.XPATH, "//div[@data-test= 'inventory-item-name']")
    MENU_BTN = (By.XPATH, "//div[@class= 'bm-burger-button']/button")
    LOG_OUT_BTN = (By.XPATH, "//a[@data-test = 'logout-sidebar-link']")

    def get_product_title_name(self):
        return self.get_text(self.PRODUCT_TITLE)

    def get_product_names(self):
        product_names = self.find_elements(self.PRODUCT_NAMES)
        product_names_text = []
        for product in product_names:
            text = self.get_text_web_element(product)
            test_logger.info(text)
            product_names_text.append(text)
        return product_names_text

    def click_menu_btn(self):
        test_logger.info("Clicked menu button")
        return self.click(self.MENU_BTN)

    def click_log_out_btn(self):
        test_logger.info("Clicked log out button")
        return self.click(self.LOG_OUT_BTN)
