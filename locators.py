from decimal import Clamped
from selenium.webdriver.common.by import By


class MainPageLocators():
    URL_STAGE_VDS="https://app.stage.medialand.pro/vds"
    URL_PROD_VDS= "https://app.sshvps.ru/vds"

    LOGIN_LINK = (By.NAME, "email","mvmppk181@gmail.com")
    LOGIN_LINK_NEW = (By.NAME, "email","mvmppk181+1@gmail.com")
    PASSWORD_PROD=(By.NAME, "password",'BAPBs2xhs')
    PASSWORD = (By.NAME, "password",'123456')
    
    BUTTON_LOGIN= (By.CLASS_NAME, "button.button--full")
    BUTTON_CREATE_VDS = (By.CLASS_NAME,"title.title--with_button .title__button")

    BUTTON_OS_CENTOS=(By.CSS_SELECTOR, ".layout-container .layout-container_internal .block.block--width270.block--advanced.block--os:nth-child(3) .modal__item .css-qeye73")
    BUTTON_OS_CENTOS_7=(By.CSS_SELECTOR, ".layout-container .layout-container_internal .block.block--width270.block--advanced.block--os:nth-child(3) .modal__item .css-16v8dco-menu .css-1bsn2c5-option")
    
    BUTTON_OS_UBUNTU=(By.CSS_SELECTOR, ".layout-container .layout-container_internal .block.block--width270.block--advanced.block--os:nth-child(2) .modal__item .css-qeye73")
    BUTTON_OS_UBUNTU_18_4=(By.CSS_SELECTOR, '.layout-container .layout-container_internal .block.block--width270.block--advanced.block--os:nth-child(2) .modal__item .css-16v8dco-menu .css-1bsn2c5-option:nth-child(2)')
    BUTTON_OS_UBUNTU_16_4=(By.CSS_SELECTOR, '.layout-container .layout-container_internal .block.block--width270.block--advanced.block--os:nth-child(2) .modal__item .css-16v8dco-menu .css-1bsn2c5-option:nth-child(3)')
    
    BUTTON_OS_DEBIAN=(By.CSS_SELECTOR, ".layout-container .layout-container_internal .block.block--width270.block--advanced.block--os:nth-child(1) .modal__item .css-qeye73")
    BUTTON_OS_DEBIAN_10=(By.CSS_SELECTOR, '.layout-container .layout-container_internal .block.block--width270.block--advanced.block--os:nth-child(1) .modal__item .css-16v8dco-menu .css-1bsn2c5-option:nth-child(2)')
    BUTTON_OS_DEBIAN_9=(By.CSS_SELECTOR, '.layout-container .layout-container_internal .block.block--width270.block--advanced.block--os:nth-child(1) .modal__item .css-16v8dco-menu .css-1bsn2c5-option:nth-child(3)')
    
    
    # Кнопки выбора тарифа (2-50  3-100  4-150  5-200 6-350) 
    BUTTON_TARIF_1 = (By.CSS_SELECTOR, ".table.table--tariffs .table--tariffs__item:nth-child(2)")
    BUTTON_TARIF_1_LABLE = (By.CSS_SELECTOR, ".table.table--tariffs .table--tariffs__item:nth-child(2) .item__available") 

    BUTTON_TARIF_2 = (By.CSS_SELECTOR, ".table.table--tariffs .table--tariffs__item:nth-child(3)")
    BUTTON_TARIF_2_LABLE = (By.CSS_SELECTOR, ".table.table--tariffs .table--tariffs__item:nth-child(3) .item__available") 

    BUTTON_TARIF_3 = (By.CSS_SELECTOR, ".table.table--tariffs .table--tariffs__item:nth-child(4)")
    BUTTON_TARIF_3_LABLE = (By.CSS_SELECTOR, ".table.table--tariffs .table--tariffs__item:nth-child(4) .item__available") 

    BUTTON_TARIF_4 = (By.CSS_SELECTOR, ".table.table--tariffs .table--tariffs__item:nth-child(5)")
    BUTTON_TARIF_4_LABLE = (By.CSS_SELECTOR, ".table.table--tariffs .table--tariffs__item:nth-child(5) .item__available") 

    BUTTON_TARIF_5 = (By.CSS_SELECTOR, ".table.table--tariffs .table--tariffs__item:nth-child(6)")
    BUTTON_TARIF_5_LABLE = (By.CSS_SELECTOR, ".table.table--tariffs .table--tariffs__item:nth-child(6) .item__available") 

    # имена для тарифов VDS
    NAME_VDS_S_C8_L150 = (By.CSS_SELECTOR, ".servers > div:nth-child(1) > input", "S-C8-ML150")
    NAME_VDS_S_C7_L50 = (By.CSS_SELECTOR, ".servers > div:nth-child(1) > input", "S-C7-ML50")
    NAME_VDS_S_U16_ML200 = (By.CSS_SELECTOR, ".servers > div:nth-child(1) > input", "S-U16-ML200")
    NAME_VDS_S_U18_ML200 = (By.CSS_SELECTOR, ".servers > div:nth-child(1) > input", "S-U18-ML200")
    NAME_VDS_S_U20_ML50 = (By.CSS_SELECTOR, ".servers > div:nth-child(1) > input", "S-U20-ML50")
    NAME_VDS_S_D11_ML100 = (By.CSS_SELECTOR, ".servers > div:nth-child(1) > input", "S-D11-ML100")
    NAME_VDS_S_D9_ML350 = (By.CSS_SELECTOR, ".servers > div:nth-child(1) > input", "S-D9-ML350")
    NAME_VDS_S_D10_ML350 = (By.CSS_SELECTOR, ".servers > div:nth-child(1) > input", "S-D10-ML350")

    NAME_VDS_S_C8 = (By.CSS_SELECTOR, ".servers > div:nth-child(1) > input", "S-C8")
    NAME_VDS_S_C7 = (By.CSS_SELECTOR, ".servers > div:nth-child(1) > input", "S-C7")
    NAME_VDS_S_U16 = (By.CSS_SELECTOR, ".servers > div:nth-child(1) > input", "S-U16")
    NAME_VDS_S_U18 = (By.CSS_SELECTOR, ".servers > div:nth-child(1) > input", "S-U18")
    NAME_VDS_S_U20 = (By.CSS_SELECTOR, ".servers > div:nth-child(1) > input", "S-U20")
    NAME_VDS_S_D11 = (By.CSS_SELECTOR, ".servers > div:nth-child(1) > input", "S-D11")
    NAME_VDS_S_D9 = (By.CSS_SELECTOR, ".servers > div:nth-child(1) > input", "S-D9")
    NAME_VDS_S_D10 = (By.CSS_SELECTOR, ".servers > div:nth-child(1) > input", "S-D10")


    BUTTON_PAY= (By.CLASS_NAME, "button.servers-create-cofirmation_button__2gwuz")
    BUTTON_PAY_FURTHER = (By.CSS_SELECTOR, ".modal__content .modal__buttons .button.button--small")

    BUTTON_PAY_BALANS = (By.CSS_SELECTOR, ".modal__content .modal__payment-methods .deal__block .deal__item:nth-child(1)")
    BUTTON_PAY_BALANS_PAY = (By.CSS_SELECTOR,".modal__content .button.button.modal__payment-button")
class LoginPageLocators():
    pass    
