from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import requests
import pickle


def set_up_page(accountName):
    options = Options()
    # options.add_argument("--headless")
    options.add_argument("--log-level=3")
    options.add_experimental_option("detach", True)
    browser = webdriver.Chrome(options=options)

    # pickle.dump( browser.get_cookies() , open("cookies.pkl","wb"))

    browser.get("https://www.instagram.com")
    sign_in_username = browser.find_element_by_name("username")
    sign_in_username.send_keys("")
    sign_in_password = browser.find_element_by_name("password")
    sign_in_password.send_keys("")
    sign_in_password.send_keys(Keys.RETURN)

    # save_details = browser.find_element_by_xpath("""//*[@id="react-root"]/section/main/div/div/div/section/div/button""")
    try:
        element = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((browser.find_element_by_xpath("""//*[@id="react-root"]/section/main/div/div/div/section/div/button""")))
    )
    finally:
        browser.quit()
    # save_details.click()

    # save_details = browser.find_element_by_xpath("""//*[@id="react-root"]/section/main/div/div/div/section/div/button""")

    potentialAccounts = {}
    return browser



accountName = "TVJ"
browser = set_up_page(accountName)


# def save_cookies(browser):
#     cookies = pickle.load(open("cookies.pkl", "rb"))
#for cookie in cookies:
    # browser.add_cookie(cookie)