import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager

# Запуск драйвера Firefox
driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

# URL сайта
url = 'https://divan.ru/'
driver.get(url)

# Подождите загрузки страницы
time.sleep(5)

# Пример парсинга: находим элементы с информацией о диванах
# Измените селекторы в зависимости от структуры сайта
# Например, если диваны находятся в блоке с классом 'product-card'
divan_elements = driver.find_elements(By.CSS_SELECTOR, '.product-card')  # замените на актуальный CSS селектор

data = []

for divan in divan_elements:
    try:
        title = divan.find_element(By.CSS_SELECTOR, '.product-title').text  # замените на актуальный CSS селектор
        price = divan.find_element(By.CSS_SELECTOR, '.product-price').text  # замените на актуальный CSS селектор
        data.append({'Title': title, 'Price': price})
    except Exception as e:
        print(f"Ошибка при извлечении данных: {e}")

# Закрываем драйвер
driver.quit()

# Сохраняем данные в CSV файл
df = pd.DataFrame(data)
df.to_csv('divans.csv', index=False, encoding='utf-8-sig')

print("Данные успешно сохранены в divans.csv")