import time
from .main_page import MainPage
from .locators import MainPageLocators
from .login_page import LoginPage
from selenium import webdriver
from datetime import datetime

link = MainPageLocators.URL_PROD_VDS
def test_go_in_Stage_VDS_D9_350_VS(browser):
    page = MainPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()                      # открываем страницу
    page.go_to_login_page_prod()          # выполняем метод страницы — переходим на страницу логина, вводим логин и пароль и осуществляем вход.
    page.create_vds() # Нажимаем на кнопку создать сервер
    # page.data_center_volume_solutions() #выбираем дата центр
    # page.parametri_VDS_S_D9_ML350() # Создаем сервер с заданными параметрами
    # page.pay_vds()
    # logs.write("S_D9_ML350 создана")
    time.sleep(10) # Даем загрузиться странице
     
     ####
    assert page.is_element_present(*MainPageLocators.BUTTON_TARIF_1_LABLE), "Тариф не доступен для покупки" 
    # Все что после ассерта не выполняется,если не найден элемент - тест падает и выдает ошибку
    print(page.browser.find_element_by_css_selector(".table.table--tariffs .table--tariffs__item:nth-child(2) .item__available").text)
    
    txt = page.browser.find_element(*MainPageLocators.BUTTON_TARIF_1_LABLE).text
    ch=int(txt[-2: ])
    if ch >7:
        print(ch)
    else:
        print("0000")
    ######
    time.sleep(10) # Даем загрузиться странице 
    

    