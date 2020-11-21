#scraper.py

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from config import User
import time

driver = webdriver.Firefox()
driver.get("http://icloud.com")
user = User()
username = user.username
password = user.password
time.sleep(10)
element = driver.find_element_by_id('account_name_text_field')
element.send_keys(username)
