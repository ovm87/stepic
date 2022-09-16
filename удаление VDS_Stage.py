#импорт библиотек
#Обязательная часть Начало

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time 
#запускаем нужную страницу ссылка в зависимости от того куда идем.
link = "https://app.stage.medialand.pro/vds"
browser = webdriver.Chrome()
browser.get(link)
#ВВести логин и пароль
input1 = browser.find_element_by_name("email")
input1.send_keys("mvmppk181+1@gmail.com")
input2 = browser.find_element_by_name("password")
input2.send_keys("123456")


  # Нажать кнопку Сначала проскроллим чтоб бала видна
button = browser.find_element_by_class_name("button.button--full")
browser.execute_script("return arguments[0].scrollIntoView(true);", button)
button.click()
#Обязательная часть Конец
time.sleep(3)


n=8 # Задаем количество удаляемых машин параметром  n

for i in range(n):
    #найти кебаб меню
    button1 = WebDriverWait(browser,5).until(EC.element_to_be_clickable((By.CLASS_NAME,"vds-item_more_button__1xtM9 .more")))
    button1 = browser.find_element_by_class_name("vds-item_more_button__1xtM9 .more")
    button1.click()
    #Нажать кнопку удалить
    button2 = browser.find_element_by_css_selector(".popup-link:nth-child(3)")
    button2.click()
     #Подтвердить удаление
    button5 = WebDriverWait(browser,5).until(EC.element_to_be_clickable((By.CSS_SELECTOR,'.modal__content .modal__buttons .button.button--small')))
    button5=browser.find_element_by_css_selector('.modal__content .modal__buttons .button.button--small')
    button5.click()
    time.sleep(1)
    # button6 = WebDriverWait(browser,5).until(EC.element_to_be_clickable((By.CSS_SELECTOR,'.modal__content .modal__buttons .button.button--small')))
    # button6=browser.find_element_by_css_selector('.modal__buttons .button.button--small')
    # button6.click()
    time.sleep(2)
    # button6=browser.find_element_by_css_selector('.modal__content.modal__vds-delete .modal__buttons .button.button--small')
    # button6.click()
    time.sleep(2)


time.sleep(10)