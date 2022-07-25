# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

link = "https://www.citilink.ru"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    button = browser.find_element(By.CSS_SELECTOR, ".HeaderMenu__button_basket > div:nth-child(2)")
    button.click()
    time.sleep(10)
    button = browser.find_element(By.CSS_SELECTOR, ".Basket__basket-empty-button")
    button.click()
    time.sleep(10)
finally:
    # закрываем браузер после всех манипуляций
    browser.quit()
