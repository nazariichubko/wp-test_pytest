import csv
import datetime
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from src.Classes.fake_data import FakeData as fd
import requests

driver = webdriver.Chrome(r"C:\Users\nazar\git\wp-test_pytest\src\webdriver_chrome_exe\chromedriver.exe")
time_now  = datetime.datetime.now().strftime('%m_%d_%Y_%H_%M_%S')

def test_open_calendar_page():
    """Checkin if calendar page is reachable and opening."""
    driver.get('http://localhost/wp-test/calendar/test-calendar/')
    assert driver.current_url == r'http://localhost/wp-test/calendar/test-calendar/'

    if driver.current_url == r'http://localhost/wp-test/calendar/test-calendar/':
        with open('test_results.csv', 'a', newline='') as csv_file:
            writer = csv.writer((csv_file))
            writer.writerow([time_now, 'test_id_1', 'Calendar page is opened.', 'PASSED'])
    else:
        with open('test_results.csv', 'a', newline='') as csv_file:
            writer = csv.writer((csv_file))
            writer.writerow([time_now, 'Calendar page is NOT opened', 'Failed'])


def test_current_date():
    """Checking the current day value on calendar page"""
    driver.get('http://localhost/wp-test/calendar/test-calendar/')
    driver.implicitly_wait(5)
    today_date = driver.find_element(By.XPATH, "//td[contains(@class, 'simcal-today')]")
    print(today_date.text)
    assert today_date.is_displayed() == True

    if today_date.is_displayed() == True:
        with open('test_results.csv', 'a', newline='') as csv_file:
            writer = csv.writer((csv_file))
            writer.writerow([time_now,'test_id_2', 'Today date displayed correctly', 'PASSED'])
    else:
        with open('test_results.csv', 'a', newline='') as csv_file:
            writer = csv.writer((csv_file))
            writer.writerow([time_now, 'Today data is not displayed', 'Failed'])



def test_add_comment():
    """Adding comment to the test website"""
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

    if comment_displayed.is_displayed() == True:
        with open('test_results.csv', 'a', newline='') as csv_file:
            writer = csv.writer((csv_file))
            writer.writerow([time_now,'test_id_3', 'Comment has been added', 'PASSED'])
    else:
        with open('test_results.csv', 'a', newline='') as csv_file:
            writer = csv.writer((csv_file))
            writer.writerow([time_now, 'Comment has NOT been added', 'Failed'])

    driver.quit()





