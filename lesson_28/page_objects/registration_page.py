from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from lesson_28.locators.registration_page_locators import RegistrationPageLocators

class RegistrationPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def registration_form(self, name, last_name, email, password):
        self.driver.find_element(*RegistrationPageLocators.name).send_keys(name)
        self.driver.find_element(*RegistrationPageLocators.last_name).send_keys(last_name)
        self.driver.find_element(*RegistrationPageLocators.email).send_keys(email)
        self.driver.find_element(*RegistrationPageLocators.password).send_keys(password)
        self.driver.find_element(*RegistrationPageLocators.password_confirm).send_keys(password)

    def submit(self):
        self.wait.until(EC.element_to_be_clickable(RegistrationPageLocators.btn_register)).click()