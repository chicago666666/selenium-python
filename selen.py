from selenium import webdriver
# Позволяет использовать "By" для поиска элемента сайта по типу
# By.XPATH на пример
from selenium.webdriver.common.by import By
# Позволяет ждать определенного события по времени - чтобы продолжить выполнение программы
from selenium.webdriver.support.ui import WebDriverWait
# Ожидаемый результат - набор методов (условий) для перехвата событий, который можно передавать
# WebDriverWait для ожидания именно этих событий, установленный промежуток времени - чтобы продолжить
# выполнение программы.
from selenium.webdriver.support import expected_conditions as EC



driver = webdriver.Chrome()
driver.get("https://www.w3schools.com/js/js_intro.asp")
my_element = driver.find_element(By.XPATH, '//*[@id="main"]/div[2]/a[2]')
WebDriverWait(driver, 6).until(EC.text_to_be_present_in_element(
    (By.XPATH, '//*[@id="footer"]/div[5]/div[4]/div/a[13]'), 'Get Certified »'
))
print(f"{my_element.text}")
my_element.click()
my_element = driver.find_element(By.XPATH, '//*[@id="main"]/div[3]/p/a')
print(f"{my_element.text}")
my_element.click()
