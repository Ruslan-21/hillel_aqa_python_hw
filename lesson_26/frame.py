from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

try:
    driver.get("http://localhost:8000/dz.html")
    time.sleep(2)

    def verify_frame(frame_id, input_id, secret_frame):
        driver.switch_to.frame(driver.find_element(By.ID, frame_id))
        input_elem = driver.find_element(By.ID, input_id)
        input_elem.clear()
        input_elem.send_keys(secret_frame)
        button = driver.find_element(By.TAG_NAME, "button")
        button.click()
        time.sleep(2)
        alert = driver.switch_to.alert
        alert_text = alert.text
        alert.accept()
        driver.switch_to.default_content()
        return alert_text

    success = "Верифікація пройшла успішно!"

    alert1 = verify_frame("frame1", "input1", "Frame1_Secret")
    alert2 = verify_frame("frame2", "input2", "Frame2_Secret")

    assert alert1 == success, "Frame1: Введено неправильний текст!"
    assert alert2 == success, "Frame2: Введено неправильний текст!"

    print("Верифікація пройшла успішно!")

finally:
 driver.quit()
