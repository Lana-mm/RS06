import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager

driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

url = 'https://divan.ru/'
driver.get(url)

time.sleep(2)


divan_elements = driver.find_elements(By.CSS_SELECTOR, 'lylNH')

data = []

for divan in divan_elements:
    try:
        title = divan.find_element(By.CSS_SELECTOR, 'ui-GPFV8 qUioe ProductName ActiveProduct').text
        price = divan.find_element(By.CSS_SELECTOR, 'ui-LD-ZU KIkOH').text
        data.append({'Title': title, 'Price': price})
    except Exception as e:
        print(f"Ошибка при извлечении данных: {e}")

driver.quit()

df = pd.DataFrame(data)
df.to_csv('divans.csv', index=False, encoding='utf-8-sig')

print("Данные успешно сохранены в divans.csv")