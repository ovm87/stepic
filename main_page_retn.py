from .base_page import BasePage
from selenium.webdriver.common.by import By
from .login_page import LoginPage
from .locators import MainPageLocators
import time 

class MainPage(BasePage):

    # def __init__(self, inputPass, password)
    #     self.inputPass = inputPass
    #     self.password = password
    # Заходим по логину и паролю
    def go_to_login_page(self):
        self.input_send_keys(*MainPageLocators.LOGIN_LINK)
        self.input_send_keys(*MainPageLocators.PASSWORD)
        self.clic_button(*MainPageLocators.BUTTON_LOGIN)
        return LoginPage(browser=self.browser, url=self.browser.current_url)
    # Нажимаем на кнопку создать сервер
    def create_vds(self): 
        self.clic_button_lite(*MainPageLocators.BUTTON_CREATE_VDS)
        return LoginPage(browser=self.browser, url=self.browser.current_url)
    # Задаем параметры VDS  
 
    def parametri_VDS_S_C8_L150(self):
        # ДАТА ЦЕНТР 
        #выбор дата центра Saint Petersburg, superdc
        if self.browser.find_element_by_css_selector('.main__flex .block.block--width270.block--advanced:nth-child(1) .block__content .block__text') != "Saint Petersburg, superdc":
            self.browser.find_element_by_css_selector('.main__flex .block.block--width270.block--advanced:nth-child(1)').click()
        else:
            self.browser.find_element_by_css_selector('.main__flex .block.block--width270.block--advanced:nth-child(2)').click()
        print("Выбрали дата центр Saint Petersburg, superdc")
        self.clic_button_lite(*MainPageLocators.BUTTON_OS_CENTOS)
        print("Выбрали ОС")
        self.clic_button_lite(*MainPageLocators.BUTTON_TARIF_3)
        print("Выбрали Тариф")
        self.input_send_keys(*MainPageLocators.NAME_VDS_S_C8_L150)
        print("Назвали VDS")
        self.clic_button_lite(*MainPageLocators.BUTTON_PAY)
        time.sleep(2)
        print("Нажали кнопку оплатить")
        self.clic_button_lite(*MainPageLocators.BUTTON_PAY_FURTHER)
        time.sleep(1)
        print("Нажали кнопку Далее")
        time.sleep(1)
        self.clic_button_lite(*MainPageLocators.BUTTON_PAY_BALANS)
        print("Выбрали баланс для оплаты")
        time.sleep(1)
        self.clic_button_lite(*MainPageLocators.BUTTON_PAY_FURTHER)
        time.sleep(1)
        self.clic_button_lite(*MainPageLocators.BUTTON_PAY_FURTHER)

    def parametri_VDS_S_U16_ML200(self):
        # ДАТА ЦЕНТР         #выбор дата центра Saint Petersburg, superdc
        if self.browser.find_element_by_css_selector('.main__flex .block.block--width270.block--advanced:nth-child(1) .block__content .block__text') != "Saint Petersburg, superdc":
            self.browser.find_element_by_css_selector('.main__flex .block.block--width270.block--advanced:nth-child(1)').click()
        else:
            self.browser.find_element_by_css_selector('.main__flex .block.block--width270.block--advanced:nth-child(2)').click()
        print("Выбрали дата центр Saint Petersburg, superdc")
        self.clic_button_lite(*MainPageLocators.BUTTON_OS_UBUNTU)
        self.clic_button_lite(*MainPageLocators.BUTTON_OS_UBUNTU_16_4)
        print("Выбрали ОС")
        self.clic_button_lite(*MainPageLocators.BUTTON_TARIF_4)
        print("Выбрали Тариф")
        self.input_send_keys(*MainPageLocators.NAME_VDS_S_U16_ML200)
        print("Назвали VDS")
        self.clic_button_lite(*MainPageLocators.BUTTON_PAY)
        time.sleep(2)
        print("Нажали кнопку оплатить")
        self.clic_button_lite(*MainPageLocators.BUTTON_PAY_FURTHER)
        time.sleep(1)
        print("Нажали кнопку Далее")
        time.sleep(1)
        self.clic_button_lite(*MainPageLocators.BUTTON_PAY_BALANS)
        print("Выбрали баланс для оплаты")
        time.sleep(1)
        self.clic_button_lite(*MainPageLocators.BUTTON_PAY_FURTHER)
        time.sleep(1)
        self.clic_button_lite(*MainPageLocators.BUTTON_PAY_FURTHER)


    def parametri_VDS_S_U20_ML50(self):
        # ДАТА ЦЕНТР         #выбор дата центра Saint Petersburg, superdc
        if self.browser.find_element_by_css_selector('.main__flex .block.block--width270.block--advanced:nth-child(1) .block__content .block__text') != "Saint Petersburg, superdc":
            self.browser.find_element_by_css_selector('.main__flex .block.block--width270.block--advanced:nth-child(1)').click()
        else:
            self.browser.find_element_by_css_selector('.main__flex .block.block--width270.block--advanced:nth-child(2)').click()
        print("Выбрали дата центр Saint Petersburg, superdc")
        #self.clic_button_lite(*MainPageLocators.BUTTON_OS_UBUNTU)
        print("Выбрали ОС")
        self.clic_button_lite(*MainPageLocators.BUTTON_TARIF_1)
        print("Выбрали Тариф")
        self.input_send_keys(*MainPageLocators.NAME_VDS_S_U20_ML50)
        print("Назвали VDS")
        self.clic_button_lite(*MainPageLocators.BUTTON_PAY)
        time.sleep(2)
        print("Нажали кнопку оплатить")
        self.clic_button_lite(*MainPageLocators.BUTTON_PAY_FURTHER)
        time.sleep(1)
        print("Нажали кнопку Далее")
        time.sleep(1)
        self.clic_button_lite(*MainPageLocators.BUTTON_PAY_BALANS)
        print("Выбрали баланс для оплаты")
        time.sleep(1)
        self.clic_button_lite(*MainPageLocators.BUTTON_PAY_FURTHER)
        time.sleep(1)
        self.clic_button_lite(*MainPageLocators.BUTTON_PAY_FURTHER)

    def parametri_VDS_S_D11_ML100(self):
        # ДАТА ЦЕНТР         #выбор дата центра Saint Petersburg, superdc
        if self.browser.find_element_by_css_selector('.main__flex .block.block--width270.block--advanced:nth-child(1) .block__content .block__text') != "Saint Petersburg, superdc":
            self.browser.find_element_by_css_selector('.main__flex .block.block--width270.block--advanced:nth-child(1)').click()
        else:
            self.browser.find_element_by_css_selector('.main__flex .block.block--width270.block--advanced:nth-child(2)').click()
        print("Выбрали дата центр Saint Petersburg, superdc")
        #self.clic_button_lite(*MainPageLocators.BUTTON_OS_DEBIAN)
        print("Выбрали ОС")
        # не нажимаем кнопку выбора тарифа т.к. от выбран по умолчанию
        self.clic_button_lite(*MainPageLocators.BUTTON_TARIF_5)
        print("Выбрали Тариф")
        self.input_send_keys(*MainPageLocators.NAME_VDS_S_D11_ML100)
        print("Назвали VDS")
        self.clic_button_lite(*MainPageLocators.BUTTON_PAY)
        time.sleep(2)
        print("Нажали кнопку оплатить")
        self.clic_button_lite(*MainPageLocators.BUTTON_PAY_FURTHER)
        time.sleep(1)
        print("Нажали кнопку Далее")
        time.sleep(1)
        self.clic_button_lite(*MainPageLocators.BUTTON_PAY_BALANS)
        print("Выбрали баланс для оплаты")
        time.sleep(1)
        self.clic_button_lite(*MainPageLocators.BUTTON_PAY_FURTHER)
        time.sleep(1)
        self.clic_button_lite(*MainPageLocators.BUTTON_PAY_FURTHER)

    def parametri_VDS_S_D9_ML350(self):
        # ДАТА ЦЕНТР         #выбор дата центра Saint Petersburg, superdc
        if self.browser.find_element_by_css_selector('.main__flex .block.block--width270.block--advanced:nth-child(1) .block__content .block__text') != "Saint Petersburg, superdc":
            self.browser.find_element_by_css_selector('.main__flex .block.block--width270.block--advanced:nth-child(1)').click()
        else:
            self.browser.find_element_by_css_selector('.main__flex .block.block--width270.block--advanced:nth-child(2)').click()
        print("Выбрали дата центр Saint Petersburg, superdc")
        self.clic_button_lite(*MainPageLocators.BUTTON_OS_DEBIAN)
        self.clic_button_lite(*MainPageLocators.BUTTON_OS_DEBIAN_9)
        print("Выбрали ОС")
        #self.clic_button_lite(*MainPageLocators.BUTTON_TARIF_2)
        print("Выбрали Тариф")
        self.input_send_keys(*MainPageLocators.NAME_VDS_S_D9_ML350)
        print("Назвали VDS")
        self.clic_button_lite(*MainPageLocators.BUTTON_PAY)
        time.sleep(2)
        print("Нажали кнопку оплатить")
        self.clic_button_lite(*MainPageLocators.BUTTON_PAY_FURTHER)
        time.sleep(1)
        print("Нажали кнопку Далее")
        time.sleep(1)
        self.clic_button_lite(*MainPageLocators.BUTTON_PAY_BALANS)
        print("Выбрали баланс для оплаты")
        time.sleep(1)
        self.clic_button_lite(*MainPageLocators.BUTTON_PAY_FURTHER)
        time.sleep(1)
        self.clic_button_lite(*MainPageLocators.BUTTON_PAY_FURTHER)

    # def delete_vds(self):
    #     n=1
    #     for i in range(n):
    #         pass
    #найти кебаб меню
            
    #Нажать кнопку удалить
           
    #Подтвердить удаление
            
    
#elements=browser.find_elements_by_css_selector('.vds-item_container__39URw')

  

# def should_be_login_link(self):
#         assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"