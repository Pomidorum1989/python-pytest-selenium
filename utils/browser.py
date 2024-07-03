import threading
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.edge.options import Options as EdgeOptions
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager


class BrowserFactory:
    _local = threading.local()

    @staticmethod
    def get_driver(browser_name):
        if not hasattr(BrowserFactory._local, 'driver'):
            if browser_name.lower() == 'chrome':
                BrowserFactory._local.driver = BrowserFactory._get_chrome_driver()
            elif browser_name.lower() == 'firefox':
                BrowserFactory._local.driver = BrowserFactory._get_firefox_driver()
            elif browser_name.lower() == 'edge':
                BrowserFactory._local.driver = BrowserFactory._get_edge_driver()
            else:
                raise ValueError(f"Unsupported browser: {browser_name}")
        return BrowserFactory._local.driver

    @staticmethod
    def _get_chrome_driver():
        chrome_options = ChromeOptions()
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--window-size=1920,1080")
        chrome_options.add_argument("--incognito")
        chrome_options.add_argument("--start-maximized")
        chrome_options.add_argument("--disable-extensions")
        chrome_options.add_argument("--disable-infobars")
        chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
        service = ChromeService(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=chrome_options)
        driver.maximize_window()
        return driver

    @staticmethod
    def _get_firefox_driver():
        firefox_options = FirefoxOptions()
        firefox_options.add_argument("--disable-gpu")
        firefox_options.add_argument("--width=1920")
        firefox_options.add_argument("--height=1080")
        firefox_options.add_argument("--incognito")
        firefox_options.add_argument("--start-maximized")
        firefox_options.add_argument("--disable-extensions")
        firefox_options.add_argument("--disable-infobars")
        service = FirefoxService(GeckoDriverManager().install())
        driver = webdriver.Firefox(service=service, options=firefox_options)
        driver.maximize_window()
        return driver

    @staticmethod
    def _get_edge_driver():
        edge_options = EdgeOptions()
        edge_options.add_argument("--disable-gpu")
        edge_options.add_argument("--window-size=1920,1080")
        edge_options.add_argument("--inprivate")
        edge_options.add_argument("--start-maximized")
        edge_options.add_argument("--disable-extensions")
        edge_options.add_argument("--disable-infobars")
        service = EdgeService(EdgeChromiumDriverManager().install())
        driver = webdriver.Edge(service=service, options=edge_options)
        driver.maximize_window()
        return driver
