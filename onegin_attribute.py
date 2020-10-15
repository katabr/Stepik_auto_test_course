
# Тест проверяет возможность создания, редактирования и удаления атрибута регламента в списке атрибутов


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import unittest
import time

#class TestRegulations(unittest.TestCase):


    #def setUp(self):
        #self.driver = webdriver.Firefox()

        # открываем браузер
        #browser = self.driver


#driver.get("http://localhost:8080/#/")
        #browser.get("http://localhost:8090/axel_web/#/definitions")
        #time.sleep(5)

        # вводим логин
        #time.sleep(1)
       # login = browser.find_element_by_css_selector('[type="text"]')
        #login.send_keys("test")
        #time.sleep(1)
        #button_enter = browser.find_element_by_css_selector('[type="submit"]')
        #button_enter.click()
        #time.sleep(1)




    # Тест 1 "Создание атрибута в таблице атрибутов"
def test_1_create_attribute(browser):
        # заходим в главное меню
        browser.implicitly_wait(5)
        # заходим в главное меню
        link_MainMenu = browser.find_element_by_xpath('//span[text()="Регламенты"]')
        link_MainMenu.click()

        browser.implicitly_wait(5)
        # выбираем Регламенты
        definitions = browser.find_element_by_css_selector('[href="#/definitions"]')
        definitions.click()

        # в списке регламентов выбираем последнюю строку, Наименование
        last_definition = browser.find_elements_by_css_selector('tr>td>b')
        last_definition[-1].click()
        time.sleep(1)
        browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)
        # выбираем кнопку Атрибуты
        attribute_button = browser.find_element_by_css_selector('[class="btn float-left settings-icon text-black btn-secondary btn-sm"]')
        attribute_button.click()
        time.sleep(1)

        # выбираем кнопку Добавить
        add_attribute = browser.find_element_by_xpath('//button[text()="Добавить"]')
        add_attribute.click()
        time.sleep(1)

        # вводим Код
        attribute_code = browser.find_element_by_css_selector('#code')
        attribute_code.click()
        attribute_code_text = "0_Тестовый код"
        attribute_code.clear()
        attribute_code.send_keys(attribute_code_text)

        # вводим Наименование
        attribute_name = browser.find_element_by_css_selector('#name')
        attribute_name.click()
        attribute_name_text = "0_Тестовый атрибут"
        attribute_name.clear()
        attribute_name.send_keys(attribute_name_text)

        # выбираем Тип
        attribute_type = browser.find_element_by_css_selector('#type')
        attribute_type.click()
        attribute_type_choice = browser.find_element_by_css_selector('[value="С"]')
        attribute_type_choice.click()


        # Сохраняем
        save_definition_group = browser.find_element_by_css_selector('[class="btn float-left  save-icon text-black btn-secondary btn-sm"]')
        save_definition_group.click()
        browser.implicitly_wait(5)

        # Тест 2 "Изменение атрибута в таблице атрибутов"
def test_2_change_attribute(browser):
            #browser = self.driver

            # заходим в главное меню
            browser.implicitly_wait(5)
            # заходим в главное меню
            link_MainMenu = browser.find_element_by_xpath('//span[text()="Регламенты"]')
            link_MainMenu.click()

            browser.implicitly_wait(5)
            # выбираем Регламенты
            definitions = browser.find_element_by_css_selector('[href="#/definitions"]')
            definitions.click()

            # в списке регламентов выбираем последнюю строку, Наименование
            last_definition = browser.find_elements_by_css_selector('tr>td>b')
            last_definition[-1].click()

            # выбираем кнопку Атрибуты
            attribute_button = browser.find_element_by_css_selector(
                '[class="btn float-left settings-icon text-black btn-secondary btn-sm"]')
            attribute_button.click()


            # в списке атрибутов выбираем последнюю строку, Карточка
            last_attribute = browser.find_elements_by_css_selector('[class="btn card-icon text-black btn-secondary btn-sm"]')
            last_attribute[-1].click()



            # изменяем Наименование
            attribute_name = browser.find_element_by_css_selector('#name')
            attribute_name.click()
            attribute_name_text = "0_Тестовый атрибут изменен"
            attribute_name.clear()
            attribute_name.send_keys(attribute_name_text)



            # Сохраняем изменения
            save_definition_group = browser.find_element_by_css_selector(
                '[class="btn float-left  save-icon text-black btn-secondary btn-sm"]')
            save_definition_group.click()
            browser.implicitly_wait(5)

    # Тест 3 "Удаление атрибута в таблице атрибутов"

def test_3_delete_attribute(browser):
        #browser = self.driver

        browser.implicitly_wait(5)
        # заходим в главное меню
        link_MainMenu = browser.find_element_by_xpath('//span[text()="Регламенты"]')
        link_MainMenu.click()

        browser.implicitly_wait(5)

        # выбираем Регламенты
        definitions = browser.find_element_by_css_selector('[href="#/definitions"]')
        definitions.click()


        # в списке регламентов выбираем последнюю строку, Наименование
        last_definition = browser.find_elements_by_css_selector('tr>td>b')
        last_definition[-1].click()


        # выбираем кнопку Атрибуты
        attribute_button = browser.find_element_by_css_selector(
            '[class="btn float-left settings-icon text-black btn-secondary btn-sm"]')
        attribute_button.click()


        # в списке атрибутов выбираем последнюю строку, кнопку Удалить
        last_attribute_del = browser.find_elements_by_css_selector(
            '[class="btn remove-icon text-black btn-secondary btn-sm"]')
        last_attribute_del[-1].click()



        # подтверждаем удаление
        confirm = browser.switch_to.alert
        confirm.accept()
        browser.implicitly_wait(5)


    #def tearDown (self):

        #time.sleep(2)
        # закрываем браузер
        #self.driver.quit()

