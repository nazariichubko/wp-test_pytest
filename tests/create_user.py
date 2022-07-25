import time
import pytest
import requests
import json
from selenium import webdriver
from src.Classes.fake_data import FakeData as fd
from selenium.webdriver.common.by import By

# driver = webdriver.Chrome(executable_path=r'C:\Users\nazar\git\wp-test_pytest\src\webdriver_chrome_exe\chromedriver.exe')
# driver.maximize_window()
#
# NAME = "Ім'я"
password = "Qwerty1!"

# def test_create_tutor():
#     driver.implicitly_wait(5)
#     driver.get("https://dev.teachme.com.ua")
#     driver.find_element(By.XPATH, "//button/i[@class='la la-key']" ).click()
#     driver.find_element(By.XPATH, "//span[@class='checkbox__text text-uppercase' and text() = 'teacher']").click()
#     driver.find_element(By.XPATH, f"//input[@type='text' and @placeholder= 'Name']").send_keys(fd.first_name)
#     driver.find_element(By.XPATH, "//input[@type='text' and @placeholder= 'Surname']").send_keys(fd.last_name)
#     driver.find_element(By.XPATH, "//input[@type='text' and @placeholder= 'Email' and @maxlength = '524288' and @class = 'input-text__input']").send_keys(fd.email)
#     driver.find_element(By.XPATH, "//div/input[@type = 'password' and @placeholder = 'Password' and @class = 'input-text__input input-text__input_icon']").send_keys(password)
#     driver.find_element(By.XPATH, "//input[@type='password' and @placeholder= 'Repeat password' and @maxlength = '524288' and @class = 'class='input-text__input input-text__input_icon']").send_keys(password)
#     driver.find_element(By.XPATH, "//button[text() = 'Register']").click()
#     driver.find_element(By.XPATH, "//button[@class = 'main-header__user']").click()
#     time.sleep(2)
#     driver.find_element(By.XPATH, "//button[@class = 'main-header__user']").click()

def test_create_user_api():
        data = dict(firstname=f"NCTest{fd.first_name}", lastname=f"NCTest{fd.last_name}",
                    email=f"{fd.last_name.lower()}{fd.random_number}@mailinator.com", password=password,role='tutor',
                    password_confirmation=password)
        response = requests.post('https://dev.api.teachme.com.ua/v1/register', data)
        # res = response.json()
        # print(res['data']['token'])
        print(response.status_code)


