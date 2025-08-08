from selenium.webdriver.common.by import By

class RegistrationPageLocators:
    name = (By.ID, "signupName")
    last_name = (By.ID, "signupLastName")
    email = (By.ID, "signupEmail")
    password = (By.ID, "signupPassword")
    password_confirm = (By.ID, "signupRepeatPassword")
    btn_register = (By.XPATH, "//button[text()='Register']")