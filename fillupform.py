from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get('https://www.phptravels.net/login')
# подождем полную загрузку страницы
WebDriverWait(driver, 3).until(EC.text_to_be_present_in_element(
    (By.XPATH, '//*[@id="fadein"]/div[1]/div/div[2]/div[1]/div/h5'), 'Login'
))
# уберем сообщение о куки
try:
    cookieButton = driver.find_element(By.CLASS_NAME, 'cc-dismiss')
    cookieButton.click()
except Exception:
    print('No cookie =(')
# находим поля логин и пароль по name
login = driver.find_element(By.NAME, 'email')
password = driver.find_element(By.NAME, 'password')
# заполняем поля формы
login.send_keys('user@phptravels.com')
password.send_keys('demouser')
