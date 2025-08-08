from selenium.webdriver.common.by import By

class NPPageLocators:
    TTN_input = (By.XPATH, "//input[contains(@class, 'track__form-group-input')]")
    btn_track = (By.ID, "np-number-input-desktop-btn-search-en")
    status_text = (By.CSS_SELECTOR, "div.header__status-text")
