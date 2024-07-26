import selenium
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

user = input("Enter your email or phone number: ")
Pass = input("Enter your password: ")

browser_option = Options()
browser_option.add_experimental_option('detach', True)

browser = selenium.webdriver.Chrome(browser_option)

browser.get("https://www.facebook.com")
browser.maximize_window()

email = browser.find_element(By.ID, "email")
email.send_keys(user)

password = browser.find_element(By.ID, "pass")
password.send_keys(Pass)

login = browser.find_element(By.NAME, "login")
login.click()

while True:
    browser.execute_script("window.scrollBy(0,1)", "")
