from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
from datetime import datetime

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def find(self, locator):
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(locator)
        )
    def click(self, locator):
        self.find(locator).click()

    def type_text(self, locator, text):
        element = self.find(locator)
        element.clear()
        element.send_keys(text)

    def get_text(self, locator):
        return self.find(locator).text
    def take_screenshots(self, name):
        # self.driver.maximize_window()
        # self.driver.save_screenshot(f"reports/{name}.png")
        # print("Screenshot saved:", f"reports/{name}.png")
        now = datetime.now()
        date_folder = now.strftime("%Y%m%d")
        timestamp = now.strftime("%H%M%S")

        folder_path = f"reports/{date_folder}"
        os.makedirs(folder_path, exist_ok=True)

        path = f"{folder_path}/{name}_{timestamp}.png"
        self.driver.save_screenshot(path)
        print("Screenshot saved:", path)


