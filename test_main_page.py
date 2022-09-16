import time
from .main_page import MainPage
from .locators import MainPageLocators
from .login_page import LoginPage
from selenium import webdriver
from datetime import datetime

logs = open('logsTest.txt', 'a')
logs.write(str(datetime.now())+ '\n')
logs.write("Создание VDS на Stage")

link = MainPageLocators.URL_STAGE_VDS
logs.write("Дата центр: rent")

def test_go_in_Stage_VDS_C8_150(browser):
    page = MainPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()                      # открываем страницузг
    page.go_to_login_page_stage()          # выполняем метод страницы — переходим на страницу логина, вводим логин и пароль и осуществляем вход.
    page.create_vds() # Нажимаем на кнопку создать сервер
    page.data_center_retn() #выбираем дата центр
    page.parametri_VDS_S_C8_ML150()  # Создаем сервер с заданными параметрами
    page.pay_vds()
    logs.write("S_C8_L150 создана")
    time.sleep(1) # Даем загрузиться странице
   

def test_go_in_Stage_VDS_U16_200(browser):
    page = MainPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()                      # открываем страницу
    page.go_to_login_page_stage()          # выполняем метод страницы — переходим на страницу логина, вводим логин и пароль и осуществляем вход.
    page.create_vds() # Нажимаем на кнопку создать сервер
    page.data_center_retn() #выбираем дата центр
    page.parametri_VDS_S_U16_ML200()# Создаем сервер с заданными параметрами
    page.pay_vds()
    logs.write("S_U16_ML200 создана")
    time.sleep(1) # Даем загрузиться странице
   
def test_go_in_Stage_VDS_U20_50(browser):
    page = MainPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()                      # открываем страницу
    page.go_to_login_page_stage()          # выполняем метод страницы — переходим на страницу логина, вводим логин и пароль и осуществляем вход.
    page.create_vds() # Нажимаем на кнопку создать сервер
    page.data_center_retn() #выбираем дата центр
    page.parametri_VDS_S_U20_ML50() # Создаем сервер с заданными параметрами
    page.pay_vds()
    logs.write("S_U20_ML50  создана")
    time.sleep(1) # Даем загрузиться странице

def test_go_in_Stage_VDS_D11_100(browser):
    page = MainPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()                      # открываем страницу
    page.go_to_login_page_stage()          # выполняем метод страницы — переходим на страницу логина, вводим логин и пароль и осуществляем вход.
    page.create_vds() # Нажимаем на кнопку создать сервер
    page.data_center_retn() #выбираем дата центр
    page.parametri_VDS_S_D11_ML100() # Создаем сервер с заданными параметрами
    page.pay_vds()
    logs.write("S_D11_ML100 создана")
    time.sleep(1) # Даем загрузиться странице
# @pytest.mark.skip
def test_go_in_Stage_VDS_D9_350(browser):
    page = MainPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()                      # открываем страницу
    page.go_to_login_page_stage()          # выполняем метод страницы — переходим на страницу логина, вводим логин и пароль и осуществляем вход.
    page.create_vds() # Нажимаем на кнопку создать сервер
    page.data_center_retn() #выбираем дата центр
    page.parametri_VDS_S_D9_ML350() # Создаем сервер с заданными параметрами
    page.pay_vds()
    logs.write("S_D9_ML350 создана")
    time.sleep(1) # Даем загрузиться странице

logs.write("Дата центр: superdc")
    ###################
def test_go_in_Stage_VDS_C8_150_VS(browser):
    page = MainPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()                      # открываем страницу
    page.go_to_login_page_stage()          # выполняем метод страницы — переходим на страницу логина, вводим логин и пароль и осуществляем вход.
    page.create_vds() # Нажимаем на кнопку создать сервер
    page.data_center_superdc() #выбираем дата центр
    page.parametri_VDS_S_C8_L150()  # Создаем сервер с заданными параметрами
    page.pay_vds()
    logs.write("VDS Stage_VDS_C8_15 создана")
    time.sleep(1) # Даем загрузиться странице
   

def test_go_in_Stage_VDS_U16_200_VS(browser):
    page = MainPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()                      # открываем страницу
    page.go_to_login_page_stage()          # выполняем метод страницы — переходим на страницу логина, вводим логин и пароль и осуществляем вход.
    page.create_vds() # Нажимаем на кнопку создать сервер
    page.data_center_superdc() #выбираем дата центр
    page.parametri_VDS_S_U16_ML200()# Создаем сервер с заданными параметрами
    page.pay_vds()
    logs.write("S_U16_ML200 создана")
    time.sleep(1) # Даем загрузиться странице
   
def test_go_in_Stage_VDS_U20_50_VS(browser):
    page = MainPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()                      # открываем страницу
    page.go_to_login_page_stage()          # выполняем метод страницы — переходим на страницу логина, вводим логин и пароль и осуществляем вход.
    page.create_vds() # Нажимаем на кнопку создать сервер
    page.data_center_superdc() #выбираем дата центр
    page.parametri_VDS_S_U20_ML50() # Создаем сервер с заданными параметрами
    page.pay_vds()
    logs.write("S_U20_ML50  создана")
    time.sleep(1) # Даем загрузиться странице

def test_go_in_Stage_VDS_D11_100_VS(browser):
    page = MainPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()                      # открываем страницу
    page.go_to_login_page_stage()          # выполняем метод страницы — переходим на страницу логина, вводим логин и пароль и осуществляем вход.
    page.create_vds() # Нажимаем на кнопку создать сервер
    page.data_center_superdc() #выбираем дата центр
    page.parametri_VDS_S_D11_ML100() # Создаем сервер с заданными параметрами
    page.pay_vds()
    logs.write("S_D11_ML100 создана")
    time.sleep(1) # Даем загрузиться странице
# @pytest.mark.skip
def test_go_in_Stage_VDS_D9_350_VS(browser):
    page = MainPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()                      # открываем страницу
    page.go_to_login_page_stage()          # выполняем метод страницы — переходим на страницу логина, вводим логин и пароль и осуществляем вход.
    page.create_vds() # Нажимаем на кнопку создать сервер
    page.data_center_superdc() #выбираем дата центр
    page.parametri_VDS_S_D9_ML350() # Создаем сервер с заданными параметрами
    page.pay_vds()
    logs.write("S_D9_ML350 создана")
    time.sleep(1) # Даем загрузиться странице

logs.write("Конец записи.")    