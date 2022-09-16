import time
from .main_page_40_VDS import MainPage
from .locators import MainPageLocators
# from Selenium import webdriver
from .login_page import LoginPage

# link = MainPageLocators.URL_STAGE_VDS
link = MainPageLocators.URL_STAGE_VDS


def test_tarif_ml50(browser):
    page = MainPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()                      # открываем страницу
    page.go_to_login_page()          # выполняем метод страницы — переходим на страницу логина, вводим логин и пароль и осуществляем вход.
    page.create_vds()                # Нажимаем на кнопку создать сервер
 
    m=9
    ff=1
    for mm in range(3,m):
        page.data_center_retn()
        time.sleep(2)
        page.tarif_ff(ff)
        time.sleep(2)
        page.os_mm(mm)
        time.sleep(2)
        page.pay_vds()
        time.sleep(10)
        if mm==m-1:
            break
        page.create_vds()         

def test_tarif_ml100(browser):
    page = MainPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()                      # открываем страницу
    page.go_to_login_page()          # выполняем метод страницы — переходим на страницу логина, вводим логин и пароль и осуществляем вход.
    page.create_vds()
    m=9
    ff=2
    for mm in range(3,m):
        page.data_center_retn()
        time.sleep(2)
        page.tarif_ff(ff)
        time.sleep(2)
        page.os_mm(mm)
        time.sleep(2)
        page.pay_vds()
        time.sleep(10)
        if mm==m-1:
            break
        page.create_vds()

def test_tarif_ml150(browser):
    page = MainPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()                      # открываем страницу
    page.go_to_login_page()          # выполняем метод страницы — переходим на страницу логина, вводим логин и пароль и осуществляем вход.
    page.create_vds()
    m=9
    ff=3
    for mm in range(3,m):
        page.data_center_retn()
        time.sleep(2)
        page.tarif_ff(ff)
        time.sleep(2)
        page.os_mm(mm)
        time.sleep(2)
        page.pay_vds()
        time.sleep(10)
        if mm==m-1:
            break
        page.create_vds()

def test_tarif_ml200(browser):
    page = MainPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()                      # открываем страницу
    page.go_to_login_page()          # выполняем метод страницы — переходим на страницу логина, вводим логин и пароль и осуществляем вход.
    page.create_vds()
    m=9
    ff=4
    for mm in range(3,m):
        page.data_center_retn()
        time.sleep(2)
        page.tarif_ff(ff)
        time.sleep(2)
        page.os_mm(mm)
        time.sleep(2)
        page.pay_vds()
        time.sleep(10)
        if mm==m-1:
            break
        page.create_vds()  

def test_tarif_ml350(browser):
    page = MainPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()                      # открываем страницу
    page.go_to_login_page()          # выполняем метод страницы — переходим на страницу логина, вводим логин и пароль и осуществляем вход.
    page.create_vds()
    m=9
    ff=5
    for mm in range(3,m):
        page.data_center_retn()
        time.sleep(2)
        page.tarif_ff(ff)
        time.sleep(2)
        page.os_mm(mm)
        time.sleep(2)
        page.pay_vds()
        time.sleep(10)
        if mm==m-1:
            break
        page.create_vds() 
