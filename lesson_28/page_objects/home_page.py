from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from lesson_28.locators.home_page_locators import HomePageLocators

class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def registration(self):
        self.wait.until(EC.element_to_be_clickable(HomePageLocators.sing_in_btn)).click()
        self.wait.until(EC.element_to_be_clickable(HomePageLocators. registration_btn)).click()