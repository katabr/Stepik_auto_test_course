
# Тест проверяет возможность создания, изменения, удаления новой папки


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.common.exceptions import NoSuchElementException
import time







def test_1_add_folder(browser):

            # заходим во вкладку "Папки"

            browser.implicitly_wait(5)

            link_folders = browser.find_element_by_css_selector('[href="#/folders"]')
            link_folders.click()


            # выбираем папку Личная папка

            folder_favourites = browser.find_element_by_xpath('//span[text()="Исходящие"]')
            folder_favourites.click()


           # Проверяем наличие тестовой папки
            #element = browser.find_element_by_xpath('//td[text()="Новая тестовая папка"]')
            from selenium.common.exceptions import NoSuchElementException
            def check_exists_by_xpath(xpath):
                try:
                    browser.find_element_by_xpath(xpath)
                except NoSuchElementException:
                    return False
                return True

            #self.assertTrue(check_exists_by_xpath('//td[text()="Новая тестовая папка"]'))

            # Если есть, удаляем ее
            if check_exists_by_xpath('//td[text()="Папка тест 1"]')== True:

                    element = browser.find_element_by_xpath('//td[text()="Папка тест 1"]')
                    element.click()
                    actionChains = ActionChains(browser)
                    actionChains.double_click(element).perform()

                    button_del = browser.find_element_by_xpath('//button[text()="Удалить"]')
                    button_del.click()
                    # Подтверждаем удаление
                    del_folder_yes = browser.find_element_by_css_selector('footer>div>button')
                    del_folder_yes.click()

                    folder_journals= browser.find_element_by_css_selector('[href="#/journals"]')
                    folder_journals.click()
                    time.sleep(1)


            if check_exists_by_xpath('//td[text()="Папка тест 2"]')== True:

                    element = browser.find_element_by_xpath('//td[text()="Папка тест 2"]')
                    element.click()
                    actionChains = ActionChains(browser)
                    actionChains.double_click(element).perform()

                    button_del = browser.find_element_by_xpath('//button[text()="Удалить"]')
                    button_del.click()
                    # Подтверждаем удаление
                    del_folder_yes = browser.find_element_by_css_selector('footer>div>button')
                    del_folder_yes.click()

                    folder_journals = browser.find_element_css_selector('[href="#/journals"]')
                    folder_journals.click()
                    time.sleep(1)


            # заходим во вкладку "Папки"
            # browser = link.driver
            link_folders = browser.find_element_by_css_selector('[href="#/folders"]')
            link_folders.click()
            browser.implicitly_wait(5)

            # выбираем папку Избранное

            folder_favourites_1 = browser.find_element_by_xpath('//span[text()="Исходящие"]')
            folder_favourites_1.click()
            browser.implicitly_wait(5)

            # выбираем кнопку Добавить
            button_add = browser.find_element_by_xpath('//button[text()="Добавить"]')
            button_add.click()


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
            folder_name_text = "Папка тест 1"
            folder_name.clear()
            folder_name.send_keys(folder_name_text)

            # Выбираем типы содержимого папки (Папка и Документ)
            content_of_folder1 = browser.find_element_by_css_selector('#F')
            content_of_folder1.click()
            content_of_folder2 = browser.find_element_by_css_selector('#D')
            content_of_folder2.click()

            # Сохраняем
            save_folder = browser.find_element_by_xpath('//button[text()="Сохранить"]')
            save_folder.click()

            # Проверяем наличие тестовой папки

            if check_exists_by_xpath('//td[text()="Папка тест 1"]') == True:
                print("Тестовая папка создана")
            else: print("Тестовая папка не создана")
            time.sleep(1)


            # Изменяем тестовую папку

            folder_journals = browser.find_element_by_css_selector('[href="#/journals"]')
            folder_journals.click()
            time.sleep(1)
            # заходим во вкладку "Папки"
            # browser = link.driver
            link_folders = browser.find_element_by_css_selector('[href="#/folders"]')
            link_folders.click()
            browser.implicitly_wait(5)

            # выбираем папку Исходящие

            folder_favourites_1 = browser.find_element_by_xpath('//span[text()="Исходящие"]')
            folder_favourites_1.click()
            browser.implicitly_wait(5)


            test_folder = browser.find_element_by_xpath('//td[text()="Папка тест 1"]')
            test_folder.click()
            actionChains = ActionChains(browser)
            actionChains.double_click(test_folder).perform()


            # Открываем карточку объекта
            #test_folder.doubleclick()
            change_folder = browser.find_element_by_xpath('//button[text()="Карточка"]')
            change_folder.click()

            folder_name_new = browser.find_element_by_css_selector('#name')
            folder_name_new.click()
            folder_name_new_text = "Папка тест 2"
            folder_name_new.clear()
            folder_name_new.send_keys(folder_name_new_text)

            # Сохраняем
            save_folder = browser.find_element_by_xpath('//button[text()="Сохранить"]')
            save_folder.click()



            # Проверяем наличие измененной тестовой папки

            if check_exists_by_xpath('//td[text()="Папка тест 2"]') == True:
                print("Тестовая папка изменена")
            else:
                print("Тестовая папка не изменена")


            # Удаляем созданную папку

            folder_journals = browser.find_element_by_css_selector('[href="#/journals"]')
            folder_journals.click()
            time.sleep(1)
            # заходим во вкладку "Папки"
            # browser = link.driver
            link_folders = browser.find_element_by_css_selector('[href="#/folders"]')
            link_folders.click()
            browser.implicitly_wait(5)

            # выбираем папку Исходящие

            folder_favourites_1 = browser.find_element_by_xpath('//span[text()="Исходящие"]')
            folder_favourites_1.click()
            browser.implicitly_wait(5)

            # выбираем измененную тестовую папку

            test_folder = browser.find_element_by_xpath('//td[text()="Папка тест 2"]')
            test_folder.click()
            actionChains = ActionChains(browser)
            actionChains.double_click(test_folder).perform()

            button_del = browser.find_element_by_xpath('//button[text()="Удалить"]')
            button_del.click()
            # Подтверждаем удаление
            del_folder_yes = browser.find_element_by_css_selector('footer>div>button')
            del_folder_yes.click()


          # Проверяем отсутствие измененной тестовой папки

            if check_exists_by_xpath('//td[text()="Папка тест 2"]') == True:
                print("Тестовая папка не удалена")
            else:
                print("Тестовая папка удалена")





