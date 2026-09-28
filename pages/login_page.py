from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):
    URL = "https://practicetestautomation.com/practice-test-login"

    userName = (By.ID, "username")
    passWord = (By.ID, "password")
    submitButton = (By.ID, "submit")
    message = (By.CSS_SELECTOR, ".post-title")
    logoutButton = (By.XPATH, "//a[text()='Log out']")
    invalid_username_message = (By.XPATH, "//div[@id='error' and text()='Your username is invalid!']")
    invalid_password_message = (By.XPATH, "//div[@id='error' and text()='Your password is invalid!']")

    def open(self):
        self.driver.get(self.URL)
    def enter_username(self, username):
        self.type_text(self.userName, username)
    def enter_password(self, password):
        self.type_text(self.passWord, password)
    def click_submit(self):
        self.click(self.submitButton)
    def get_message(self):
        return self.get_text(self.message)
    def get_invalid_username(self):
        return self.get_text(self.invalid_username_message)
    def get_invalid_password(self):
        return self.get_text(self.invalid_password_message)
    def click_logout(self, logout_button):
        self.click(self.logoutButton, logout_button)

    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_submit()
        if username == "student" and password == "Password123":
            return self.get_message()
        elif username != "student":
            return self.get_invalid_username()
        elif password != "Password123":
            return self.get_invalid_password()  