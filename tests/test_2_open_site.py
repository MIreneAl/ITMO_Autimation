import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://demoqa.com/")
time.sleep(5)

# поиск элемента

icon = driver.find_element(By.CSS_SELECTOR, 'header > a > img')

if icon is None:
    print('Элемент не найден')
else:
    print('Элемент найден')


footer = driver.find_element(By.CSS_SELECTOR, 'footer > span')

if footer is None:
    print('Элемент не найден')
else:
    print('Элемент найден')

buttons = driver.find_element(By.CSS_SELECTOR, 'div > div > div.home-body > div > div')

if buttons is None:
    print('Элемент не найден')
else:
    print('Элемент найден')
