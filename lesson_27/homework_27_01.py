import pytest
from selenium import webdriver
from page_np import NPTrackingPage

@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@pytest.mark.parametrize("ttn_number, expected_status", [
    ("59001424801175", "Отримана"),
])
def test_nova_poshta_tracking(driver, ttn_number, expected_status):
    page = NPTrackingPage(driver)
    page.open_page()
    actual_status = page.track_parcel(ttn_number)
    assert actual_status.startswith(expected_status), f"Статус '{actual_status}' не починається з '{expected_status}'"
