import pytest
import requests
from random import randrange
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import pendulum
from src.generators.player_localizations import PlayerLocalization
from src.Classes.fake_data import FakeData as fd
from selenium.webdriver.support import expected_conditions as EC


random_id = randrange(1, 999, 1)
current_time = pendulum.now().to_formatted_date_string()


def test_localhost_website():
    response = requests.get("http://localhost/wp-test/")
    print(response)
    assert response.status_code == 200

def test_post_json_test():
    data = dict(id= random_id, name='testpython', lastname= 'testpython2')
    response = requests.post('http://localhost:3000/users', data)
    print(response.text)
    assert response.status_code == 201

def test_data_from_nodejs_database():
    response = requests.get("http://localhost:3000/users")
    print(response.text)
    assert response.status_code == 200


def test_navigate_to_homepage():
    path = r"C:\Users\nazar\git\wp-test_pytest\src\webdriver_chrome_exe\chromedriver.exe"
    driver = webdriver.Chrome(path)
    driver.implicitly_wait(5)
    driver.get("http://localhost/wp-test/")
    assert driver.find_element(By.ID, 'page-header-cover').is_displayed() == True
    # if driver.find_element(By.ID, 'page-header-cover').is_displayed():
    #     print("Element is displayed")
    # else:
    #     print("Element not found")

def test_navigate_to_calendar_page():
    response = requests.get("http://localhost/wp-test/calendar/test-calendar/")
    print(response)
    assert response.status_code == 200

def test_search():
    screenshot_name = randrange(1, 100, 5)
    path = r"C:\Users\nazar\git\wp-test_pytest\src\webdriver_chrome_exe\chromedriver.exe"
    driver = webdriver.Chrome(path)
    driver.implicitly_wait(5)
    driver.get("http://localhost/wp-test/")
    driver.find_element(By.ID, "wp-block-search__input-1").send_keys('test')
    driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
    assert driver.find_element(By.XPATH, "//article[@id]").is_displayed()
    driver.save_screenshot(f"{screenshot_name}.png")


@pytest.mark.parametrize("statuses", [
    "active", "inactive"
])
def test_bulder_feature(get_user_data_generated, statuses):
    generated_data =get_user_data_generated.update_inner_value(['localize'], PlayerLocalization("es_ES").set_number(15).build()).build()
    response = requests.post('http://localhost:3000/users', generated_data)
    print(response.text)
    assert response.status_code == 200 or 201

def test_contact_form():
    screenshot_name = randrange(1, 100, 5)
    path = r"C:\Users\nazar\git\wp-test_pytest\src\webdriver_chrome_exe\chromedriver.exe"
    driver = webdriver.Chrome(path)
    driver.implicitly_wait(5)
    driver.get("http://localhost/wp-test/site/")
    driver.find_element(By.ID, "field_dp46a_first").send_keys(fd.first_name)
    driver.find_element(By.ID, "field_dp46a_last").send_keys(fd.last_name)
    driver.find_element(By.ID, "field_j3yjg").send_keys(fd.email)
    driver.find_element(By.ID, "field_qbnam").send_keys(fd.phone_number)
    driver.find_element(By.ID, "field_uot6f").send_keys(fd.random_text)
    driver.find_element(By.XPATH, "//button[text() = 'Submit']").click()
    assert WebDriverWait(driver,30).until(
            EC.text_to_be_present_in_element(
                (By.ID, 'frm_form_2_container'),  # Element filtaration
                    'Your responses were successfully submitted. Thank you!'  # Expected text
                )
            )
    driver.save_screenshot(rf"C:\Users\nazar\git\wp-test_pytest\src\screenshots\test_contact_form\test_contact_form {current_time}.png")




