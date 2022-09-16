import time
from .main_page import MainPage
def test_go_in_Stage_VDS_C8(browser):
    link = "https://app.stage.medialand.pro/vds"
    page = MainPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()                      # открываем страницу
    page.go_to_login_page()          # выполняем метод страницы — переходим на страницу логина, вводим логин и пароль и осуществляем вход.
    page.delite_vds()
    