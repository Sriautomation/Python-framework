from selenium import webdriver
from pages.login_page import LoginPage
from test_data import valid_password, valid_username, invalid_password, invalid_username
from selenium.webdriver.chrome.options import Options


def test_valid_login():
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(options=options)

    try:
        login_page = LoginPage(driver)
        login_page.open()
        login_page.login(valid_username, valid_password)
        login_page.take_screenshots("Valid login result")

        message = login_page.get_message()
        assert "Logged In Successfully" in message
        print("Valid login test passed. Message:", message.strip())
    finally:
        driver.quit()


def test_invalid_username():
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(options=options)

    try:
        login_page = LoginPage(driver)
        login_page.open()
        login_page.login(invalid_username, valid_password)
        login_page.take_screenshots("Invalid username")

        message = login_page.get_invalid_username()
        assert "Your username is invalid!" in message
        print("Your error message is", message.strip())
    finally:
        driver.quit()

def test_invalid_password():
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-ssm-usage")
    driver = webdriver.Chrome(options=options)

    try:
        login_page = LoginPage(driver)
        login_page.open()
        login_page.login(valid_username, invalid_password)
        login_page.take_screenshots("Invalid password")

        message = login_page.get_invalid_password()
        assert "Your password is invalid!" in message
        print("Your invalid password error message is ", message.strip())
    finally:
        driver.quit()



