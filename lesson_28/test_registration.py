from selenium import webdriver
from lesson_28.page_objects.home_page import HomePage
from lesson_28.page_objects.registration_page import RegistrationPage
import pytest
import time

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get("https://guest:welcome2qauto@qauto2.forstudy.space/")
    yield driver
    driver.quit()

def test_user_registration(driver):
    home_page = HomePage(driver)
    registration_page = RegistrationPage(driver)

    home_page.registration()

    email = f"testuser_{int(time.time())}@example.com"
    registration_page.registration_form(
        name="Test",
        last_name="User",
        email=email,
        password="Password123"
    )
    registration_page.submit()

    assert driver.title == "Hillel Qauto"
