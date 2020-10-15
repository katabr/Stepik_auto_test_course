
# Тест проверяет возможность создания новой папки


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import unittest
import sys
import time

class PythonOrgSearch(unittest.TestCase):



    def setUp(self):
        #self.driver = webdriver.Remote(desired_capabilities={
           # "browserName": "firefox",
           # "urlName": "MAC",
        #})

        class ParamTest(unittest.TestCase):
            capabilities = None

        self.driver = webdriver.Remote(desired_capabilities=self.capabilities)



        #self.driver = webdriver.Firefox()

        # открываем браузер
        browser = self.driver
        browser.get("http://192.168.16.66:8090/axel_web/#/requests.html")

        # аутентификация

        login = browser.find_element_by_css_selector('[type="text"]')
        login.send_keys("vasiliev_nv")

        button_enter = browser.find_element_by_css_selector('[type="submit"]')
        button_enter.click()







    def test_1_add_folder(self):

            # заходим во вкладку "Папки"
            browser = self.driver
            link_folders = browser.find_element_by_css_selector('nav>div>ul>li')

            link_folders.click()


            # выбираем папку Избранное

            folder_favourites = browser.find_elements_by_css_selector('[class="group"]')
            folder_favourites[1].click()


            # выбираем кнопку Добавить
            add_data = browser.find_elements_by_css_selector('[type="button"]')
            add_data[2].click()


            # открываем выпадающий список типов объектов
            elem_kind = browser.find_element_by_css_selector('#kind')
            elem_kind.click()
            # добавляем запись

            # выбираем объект Папка
            add_data = browser.find_elements_by_css_selector('[value="F"]')
            add_data[0].click()
            # добавляем запись


            # Открывается карточка добавления нового объекта

            # вводим Название папки
            folder_name = browser.find_element_by_css_selector('#name')
            folder_name.click()
            folder_name_text = "_ 000_Новая тестовая папка"
            folder_name.clear()
            folder_name.send_keys(folder_name_text)

            # выбираем типы содержимого папки (Папка и Документ)
            content_of_folder1 = browser.find_element_by_css_selector('#F')
            content_of_folder1.click()
            content_of_folder2 = browser.find_element_by_css_selector('#D')
            content_of_folder2.click()

            # Сохраняем
            save_folder = browser.find_element_by_css_selector('[class="btn float-left save-icon text-white btn-secondary btn-sm"]')
            save_folder.click()

            # Удаляем созданную папку

            # Сортируем по названию
            #sort_folder = browser.find_elements_by_css_selector('[role="columnheader"]')
            #sort_folder[2].click()

            #Выбираем последнюю созданну папку
            choose1_folder = browser.find_elements_by_css_selector('[aria-colindex="3"]')
            actionChains = ActionChains(browser)
            actionChains.context_click(choose1_folder[-1]).perform()
            #choose1_folder[-1].context_click()
            time.sleep(2)

             #Нажимаем кнопку Удалить
            del_folder = browser.find_elements_by_css_selector('div>ul>li>span')
            del_folder[5].click()
            time.sleep(2)

           # Подтверждаем удаление
            del_folder_yes = browser.find_element_by_css_selector('footer>div>button')
            del_folder_yes.click()





    def tearDown (self):

        time.sleep(2)
        # закрываем браузер
        self.driver.quit()

if __name__ == "__main__":
    Param_Test.capabilities = {
        "browserName": sys.argv[1],
        #"urlName": sys.argv[2],
    }
    unittest.main()