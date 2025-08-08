from selenium.webdriver.common.by import By

class HomePageLocators:
    sing_in_btn = (By.XPATH, "//button[contains(@class, 'header_signin') and text()='Sign In']")
    registration_btn = (By.XPATH, "//button[@type='button' and contains(@class, 'btn-link') and text()='Registration']")