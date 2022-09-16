import time
from .main_page_retn import MainPage
# from Selenium import webdriver
# from .login_page import LoginPage


def test_go_in_Stage_VDS_C8(browser):
    link = "https://app.stage.medialand.pro/vds"
    page = MainPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()                      # открываем страницу
    page.go_to_login_page()          # выполняем метод страницы — переходим на страницу логина, вводим логин и пароль и осуществляем вход.
    page.create_vds() # Нажимаем на кнопку создать сервер
    page.parametri_VDS_S_C8_L150()  # Создаем сервер с заданными параметрами
    time.sleep(1) # Даем загрузиться странице
   

def test_go_in_Stage_VDS_U16(browser):
    link = "https://app.stage.medialand.pro/vds"
    page = MainPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()                      # открываем страницу
    page.go_to_login_page()          # выполняем метод страницы — переходим на страницу логина, вводим логин и пароль и осуществляем вход.
    page.create_vds() # Нажимаем на кнопку создать сервер
    page.parametri_VDS_S_U16_ML200()# Создаем сервер с заданными параметрами
    time.sleep(1) # Даем загрузиться странице
   
def test_go_in_Stage_VDS_U20(browser):
    link = "https://app.stage.medialand.pro/vds"
    page = MainPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()                      # открываем страницу
    page.go_to_login_page()          # выполняем метод страницы — переходим на страницу логина, вводим логин и пароль и осуществляем вход.
    page.create_vds() # Нажимаем на кнопку создать сервер
    page.parametri_VDS_S_U20_ML50() # Создаем сервер с заданными параметрами
    time.sleep(1) # Даем загрузиться странице

def test_go_in_Stage_VDS_D11(browser):
    link = "https://app.stage.medialand.pro/vds"
    page = MainPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()                      # открываем страницу
    page.go_to_login_page()          # выполняем метод страницы — переходим на страницу логина, вводим логин и пароль и осуществляем вход.
    page.create_vds() # Нажимаем на кнопку создать сервер
    page.parametri_VDS_S_D11_ML100() # Создаем сервер с заданными параметрами
    time.sleep(1) # Даем загрузиться странице
# @pytest.mark.skip
def test_go_in_Stage_VDS_D9(browser):
    link = "https://app.stage.medialand.pro/vds"
    page = MainPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()                      # открываем страницу
    page.go_to_login_page()          # выполняем метод страницы — переходим на страницу логина, вводим логин и пароль и осуществляем вход.
    page.create_vds() # Нажимаем на кнопку создать сервер
    page.parametri_VDS_S_D9_ML350() # Создаем сервер с заданными параметрами
    time.sleep(1) # Даем загрузиться странице