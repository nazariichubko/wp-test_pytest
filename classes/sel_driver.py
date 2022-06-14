from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains




class DriverClass(webdriver.Chrome):
    def __init__(self, driver_path=r"c:\Users\nazar\git\wp-test_pytest\src\webdriver_chrome_exe", teardown=False):
        self.driver_path = driver_path
        self.teardown = teardown
        os.environ['PATH'] += self.driver_path
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        super(DriverClass, self).__init__(options=options)
        self.implicitly_wait(5)
        self.maximize_window()