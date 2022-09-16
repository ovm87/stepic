#импорт библиотек
#Обязательная часть Начало
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


#запускаем нужную страницу ссылка в зависимости от того куда идем.
link = "https://app.sshvps.ru/vds"
browser = webdriver.Chrome()
browser.get(link)

#ВВести логин и пароль
input1 = browser.find_element_by_name("email")
input1.send_keys("mvmppk181@gmail.com")
input2 = browser.find_element_by_name("password")
input2.send_keys("BAPBs2xhs")

logs = open('logsTest.txt', 'a')
logs.write(str(datetime.now())+ '\n')
logs.write("VDS status after buying:"+ '\n')

  # Нажать кнопку Сначала проскроллим чтоб бала видна
button = browser.find_element_by_class_name("button.button--full")
browser.execute_script("return arguments[0].scrollIntoView(true);", button)
button.click()
#Обязательная часть Конец
time.sleep(2)

# кликнуть по вдс
# vds=browser.find_element_by_css_selector(".vds-list_list__2QzXW .vds-item_container__39URw:nth-child(2)").click()

# запросить статус вдс
n=10 # количество проверяемых VDS
for i in range(1,n):
    vds_status = browser.find_element_by_css_selector(
        f".vds-list_list__2QzXW .vds-item_container__39URw:nth-child({i}) .vds-item_label__1zx35"
            ).text
    name_vds=browser.find_element_by_css_selector(
        f".vds-list_list__2QzXW .vds-item_container__39URw:nth-child({i}) .vds-item_name__QP7Br"
            ).text
    about_vds=browser.find_element_by_css_selector(
        f".vds-list_list__2QzXW .vds-item_container__39URw:nth-child({i}) .vds-item_about__qwjus"
            ).text
            
    if vds_status == "Активен":
        print(name_vds,' Параметры :', about_vds, ' - Развернулась')
        logs.write(name_vds + ' Параметры : ' +  about_vds + ' - Развернулась' + '\n')

    else:
        print(name_vds,' Параметры :', about_vds, " - Не развернулась")
        logs.write(name_vds + ' Параметры : ' +  about_vds + ' - Не развернулась' + '\n')
    time.sleep(10)

logs.close()
