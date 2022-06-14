import pytest
import requests
from random import randrange
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from src.generators.player_localizations import PlayerLocalization
from src.Classes.fake_data import FakeData as fd
from selenium.webdriver.support import expected_conditions as EC

from xlwt import Workbook


driver = webdriver.Chrome(r"C:\Users\nazar\git\wp-test_pytest\src\webdriver_chrome_exe\chromedriver.exe")
wb = Workbook()
sheet = wb.add_sheet("test_result.csv")

def test_open_calendar_page():
    driver.get('http://localhost/wp-test/calendar/test-calendar/')
    assert driver.current_url == r'http://localhost/wp-test/calendar/test-calendar/'


def test_current_date():
    driver.get('http://localhost/wp-test/calendar/test-calendar/')
    driver.implicitly_wait(5)
    today_date = driver.find_element(By.XPATH, "//td[contains(@class, 'simcal-today')]")
    print(today_date.text)
    assert today_date.is_displayed() == True

    if today_date.is_displayed() == True:
        sheet.write(1, 0, f"Test Passed, Today's date: {today_date.text})")
        wb.save("test_result.csv")


def test_add_comment():
    driver.get('http://localhost/wp-test/2022/05/10/test-post/')
    driver.implicitly_wait(5)
    comment_box = driver.find_element(By.ID, "comment")
    comment_box.click()
    comment_box.send_keys(fd.random_text)
    name_field = driver.find_element(By.ID, "author")
    name_field.click()
    name_field.send_keys(fd.first_name)
    email_field = driver.find_element(By.ID, "email")
    email_field.click()
    email_field.send_keys(fd.email)
    submit_button = driver.find_element(By.ID, "submit")
    submit_button.click()
    comment_displayed = driver.find_element(By.XPATH, "//article[@class = 'comment clearfix']")
    assert comment_displayed.is_displayed() == True

    driver.quit()

