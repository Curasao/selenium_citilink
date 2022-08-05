import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

link = "https://www.citilink.ru"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    button = browser.find_element(By.CSS_SELECTOR, ".MainHeader__search-open")
    button.click()
    time.sleep(10)
    search = browser.find_element(By.TAG_NAME,"input")

    # search request for citilink
    search.send_keys('Смартфон')
    search.send_keys(Keys.RETURN)


    time.sleep(10)
finally:
    # закрываем браузер после всех манипуляций
    browser.quit()
