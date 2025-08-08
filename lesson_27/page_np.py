from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators_np import NPPageLocators

class NPTrackingPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://tracking.novaposhta.ua/#/uk"
        self.input_locator = NPPageLocators.TTN_input
        self.button_locator = NPPageLocators.btn_track
        self.result_locator = NPPageLocators.status_text

    def open_page(self):
        self.driver.get(self.url)

    def track_parcel(self, ttn_number):

        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.input_locator))
        input_elem = self.driver.find_element(*self.input_locator)
        input_elem.clear()
        input_elem.send_keys(ttn_number)

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.button_locator)
        )
        button = self.driver.find_element(*self.button_locator)
        button.click()


        status_elem = WebDriverWait(self.driver, 15).until(
            EC.visibility_of_element_located(self.result_locator)
        )
        return status_elem.text
