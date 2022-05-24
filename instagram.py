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
    # options.add_argument("--log-level=3")
    options.add_experimental_option("detach", True)
    options.add_argument("--user-data-dir=C:\\Users\\amand\\OneDrive\\Desktop\\Things For Work\\Make My Job Easier\\UserData")
    options.page_load_strategy = 'normal'
    browser = webdriver.Chrome(options=options)

    browser.get("https://www.instagram.com")

    potentialAccounts = {}
    return browser



accountName = "TVJ"
browser = set_up_page(accountName)
