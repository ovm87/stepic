from selenium.common.exceptions import NoSuchElementException


class BasePage():
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    # Метод открытия браузера
    def open(self):
        self.browser.get(self.url)

    #Метод ввода данных в поле
    def input_send_keys(self, how1, what1, text1):
        self.browser.find_element(how1, what1).send_keys(text1)
        pass

    #Метод нажатия кнопки
    def clic_button(self, how2, what2):
        button = self.browser.find_element(how2, what2)
        self.browser.execute_script("return arguments[0].scrollIntoView(true);", button) #Сначала проскроллим чтоб бала видна кнопка
        button.click()
        pass
    def clic_button_lite(self, how2, what2):
        self.browser.find_element(how2, what2).click()
    
    # Перехват исключения
    def is_element_present(self, how3, what3):
        try:
            self.browser.find_element(how3, what3)
        except NoSuchElementException:
            return False
        return True
