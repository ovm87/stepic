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
        # return LoginPage(browser=self.browser, url=self.browser.current_url)
   
    # Нажимаем на кнопку создать сервер
    def create_vds(self): 
        self.clic_button_lite(*MainPageLocators.BUTTON_CREATE_VDS)
        #return LoginPage(browser=self.browser, url=self.browser.current_url)
    
    # Выбор дата центра 
    def data_center_superdc(self):
        if self.browser.find_element_by_css_selector('.main__flex .block.block--width270.block--advanced:nth-child(1) .block__content .block__text') == "Saint Petersburg, superdc":
            self.browser.find_element_by_css_selector('.main__flex .block.block--width270.block--advanced:nth-child(1)').click()
        else:
            self.browser.find_element_by_css_selector('.main__flex .block.block--width270.block--advanced:nth-child(2)').click()
        print("Выбрали дата центр Saint Petersburg, superdc")

    def data_center_retn(self):
        if self.browser.find_element_by_css_selector('.main__flex .block.block--width270.block--advanced:nth-child(1) .block__content .block__text') != "Saint Petersburg, superdc":
            self.browser.find_element_by_css_selector('.main__flex .block.block--width270.block--advanced:nth-child(1)').click()
        else:
            self.browser.find_element_by_css_selector('.main__flex .block.block--width270.block--advanced:nth-child(2)').click()
        print("Выбрали дата центр Saint Petersburg, retn")

    def data_center_xelent(self):
        if self.browser.find_element_by_css_selector('.main__flex .block.block--width270.block--advanced:nth-child(1) .block__content .block__text') == "Saint Petersburg, Xelent":
            self.browser.find_element_by_css_selector('.main__flex .block.block--width270.block--advanced:nth-child(1)').click()
        else:
            self.browser.find_element_by_css_selector('.main__flex .block.block--width270.block--advanced:nth-child(2)').click()
        print("Выбрали дата центр Saint Petersburg, superdc")

    def data_center_volume_solutions(self):
        if self.browser.find_element_by_css_selector('.main__flex .block.block--width270.block--advanced:nth-child(1) .block__content .block__text') != "Saint Petersburg, Xelent":
            self.browser.find_element_by_css_selector('.main__flex .block.block--width270.block--advanced:nth-child(1)').click()
        else:
            self.browser.find_element_by_css_selector('.main__flex .block.block--width270.block--advanced:nth-child(2)').click()
        print("Выбрали дата центр Saint Petersburg, retn")   
        # Тарифы 
    def tarif_1(self):
        self.clic_button_lite(*MainPageLocators.BUTTON_TARIF_1)
    def tarif_2(self):
        self.clic_button_lite(*MainPageLocators.BUTTON_TARIF_2)
    def tarif_3(self):
        self.clic_button_lite(*MainPageLocators.BUTTON_TARIF_3)      
    def tarif_4(self):
        self.clic_button_lite(*MainPageLocators.BUTTON_TARIF_4)
    def tarif_5(self):
        self.clic_button_lite(*MainPageLocators.BUTTON_TARIF_5) 
       
       # OS
    def os_mm(self, mm):
        if mm==1:
            # Ubuntu 20
            self.clic_button_lite(*MainPageLocators.BUTTON_OS_UBUNTU)
            self.input_send_keys(*MainPageLocators.NAME_VDS_S_U20)
            print("Назвали VDS")
            print("Выбрали ОС")
        if mm==2: # Ubuntu 18
            self.clic_button_lite(*MainPageLocators.BUTTON_OS_UBUNTU)
            self.clic_button_lite(*MainPageLocators.BUTTON_OS_UBUNTU_18_4)
            self.input_send_keys(*MainPageLocators.NAME_VDS_S_U18)
            print("Назвали VDS")
            print("Выбрали ОС")

        if mm==3: # Ubuntu 16
           self.clic_button_lite(*MainPageLocators.BUTTON_OS_UBUNTU)
           self.clic_button_lite(*MainPageLocators.BUTTON_OS_UBUNTU_16_4)
           self.input_send_keys(*MainPageLocators.NAME_VDS_S_U16)
           print("Назвали VDS")

        if mm==4: # Debian 11
           self.clic_button_lite(*MainPageLocators.BUTTON_OS_DEBIAN)
           print("Выбрали ОС")
           self.input_send_keys(*MainPageLocators.NAME_VDS_S_D11)
           print("Назвали VDS")

        if mm==5: # Debian 10
           self.clic_button_lite(*MainPageLocators.BUTTON_OS_DEBIAN)
           self.clic_button_lite(*MainPageLocators.BUTTON_OS_DEBIAN_10)        
           print("Выбрали ОС")
           self.input_send_keys(*MainPageLocators.NAME_VDS_S_D10)
           print("Назвали VDS")

        if mm==6: # Debian 9
           self.clic_button_lite(*MainPageLocators.BUTTON_OS_DEBIAN)
           self.clic_button_lite(*MainPageLocators.BUTTON_OS_DEBIAN_9)        
           print("Выбрали ОС")
           self.input_send_keys(*MainPageLocators.NAME_VDS_S_D11)
           print("Назвали VDS")

        if mm==7: # Centos 8
           self.clic_button_lite(*MainPageLocators.BUTTON_OS_CENTOS)
           print("Выбрали ОС")
           self.input_send_keys(*MainPageLocators.NAME_VDS_S_C8)
           print("Назвали VDS") 

        if mm==8: # Centos 7
           self.clic_button_lite(*MainPageLocators.BUTTON_OS_CENTOS)
           self.clic_button_lite(*MainPageLocators.BUTTON_OS_CENTOS_7)        
           print("Выбрали ОС")
           self.input_send_keys(*MainPageLocators.NAME_VDS_S_C7)
           print("Назвали VDS")

    def pay_vds(self):
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

    def tarif_ff(self, ff):
        if ff==1:
            self.clic_button_lite(*MainPageLocators.BUTTON_TARIF_1)
        if ff==2:
            self.clic_button_lite(*MainPageLocators.BUTTON_TARIF_2) 
        if ff==3:
            self.clic_button_lite(*MainPageLocators.BUTTON_TARIF_3)
        if ff==4:
            self.clic_button_lite(*MainPageLocators.BUTTON_TARIF_4)
        if ff==5:
            self.clic_button_lite(*MainPageLocators.BUTTON_TARIF_5)                     

    

                    
