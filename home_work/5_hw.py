import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")
time.sleep(5)


name = driver.find_element(By.CSS_SELECTOR, '#user-name')
passw = driver.find_element(By.CSS_SELECTOR, '#password')
submit = driver.find_element(By.CSS_SELECTOR, '#login-button')


if name is None or passw is None or submit is None:
    print('Элементы не найдены')
else:
    print('Элементы найдены')