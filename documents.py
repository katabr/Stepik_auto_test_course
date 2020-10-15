
# Тест проверяет возможность создания:
# тест1 -  новых реквизитов электронных документов
# тест2 -  новых типов карточек электронных документов
# тест3 -  видов документов


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.common.exceptions import NoSuchElementException
import time





def test_1_add_requisit_of_doc(browser):

            browser.implicitly_wait(5)


            # заходим во вкладку "Документы"

            link_documents = browser.find_elements_by_css_selector('nav>div>ul>li>a>span')

            link_documents[1].click()


            # выбираем  строку Реквизиты документов
            open_vew_of_doc = browser.find_element_by_css_selector('[href="#/doc_requisites"]')

            open_vew_of_doc.click()


            # открываем форму (кнопка Добавить)
            add_data = browser.find_elements_by_css_selector('[type="button"]')
            add_data[1].click()
            # добавляем запись



            # вводим код реквизита
            kod_req_doc = browser.find_element_by_css_selector('#code')
            kod_req_doc.click()
            kod_req_doc_text = "Код реквизита документа"
            kod_req_doc.clear()
            kod_req_doc.send_keys(kod_req_doc_text)

            # вводим Название документа
            name_req_doc = browser.find_element_by_css_selector('#name')
            name_req_doc.click()
            name_req_doc_text = "Название реквизита документа"
            name_req_doc.clear()
            name_req_doc.send_keys(name_req_doc_text)

            # поле Сохранять
            save_req = browser.find_element_by_css_selector('#stored')
            save_req.click()

            save_req1 = browser.find_elements_by_css_selector('[value="true"]')

            save_req1[0].click()

            # поле Тип
            type_req = browser.find_element_by_css_selector('#type')
            type_req.click()

            type_req1 = browser.find_elements_by_css_selector('[value="Ц"]')

            type_req1[0].click()

            # поле Представление реквизита
            type_req_feild = browser.find_element_by_css_selector('#formatter')
            type_req_feild.click()

            type_req_feild1 = browser.find_element_by_css_selector('[value="number"]')

            type_req_feild1.click()



            # Сохраняем
            save_req_doc = browser.find_elements_by_css_selector('[type="submit"]')
            save_req_doc[0].click()



            # проверяем верность записи в журнале
            # проверяем поле КОД
            #kod_req_ver = browser.find_elements_by_css_selector('[aria-colindex="2"]')
            #kod_req_ver_е = kod_req_ver[-1].text
            #assert kod_req_ver_е == kod_req_doc_text, "Incorrect value"
            #print("Expected value Код", kod_req_doc_text, ", actual value Код", kod_req_ver_е, ".")
            time.sleep(1)
            # Переходим на последнюю страницу
            # next_page = browser.find_elements_by_css_selector('body>div>div>div>div>div>div>div>div>div>ul>li>span')
            next_page = browser.find_elements_by_css_selector('[role="presentation"]')
            next_page[-1].click()

            # Удалаяем запись
            del_req = browser.find_elements_by_css_selector('tbody>tr>td>button')
            del_req[-1].click()

            # Удалаяем запись
            del_req = browser.find_elements_by_css_selector('footer>div>button')
            del_req[-2].click()


def test_2_add_type_of_card_of_doc(browser):
    # заходим во вкладку "Документы"

    link_documents = browser.find_elements_by_css_selector('nav>div>ul>li>a>span')

    link_documents[1].click()

    # выбираем  строку Типы карточек документов
    open_card_of_doc = browser.find_element_by_css_selector('[href="#/doc_types"]')

    open_card_of_doc.click()

    # открываем форму (кнопка Добавить)
    add_data = browser.find_elements_by_css_selector('[type="button"]')
    add_data[1].click()
    # добавляем запись

    # вводим код типа карточки
    kod_card_of_doc = browser.find_element_by_css_selector('#code')
    kod_card_of_doc.click()
    kod_card_of_doc_text = "0Код типа карточки документа"
    kod_card_of_doc.clear()
    kod_card_of_doc.send_keys(kod_card_of_doc_text)

    # вводим Название документа
    name_card_of_doc = browser.find_element_by_css_selector('#name')
    name_card_of_doc.click()
    name_card_of_doc_text = "0Название типа карточки документа"
    name_card_of_doc.clear()
    name_card_of_doc.send_keys(name_card_of_doc_text)

    # Сохраняем
    save_card_of_doc = browser.find_element_by_css_selector('form>div>button')
    save_card_of_doc.click()

    # Подтверждаем сохранение
    save_card_of_doc = browser.find_element_by_css_selector('form>div>button')
    save_card_of_doc.click()

    # Закрываем окно
    close_card_of_doc = browser.find_element_by_css_selector('footer>div>button')
    close_card_of_doc.click()

    # проверяем верность записи в журнале
    # проверяем поле КОД
    kod_req_ver = browser.find_elements_by_css_selector('[aria-colindex="2"]')
    kod_req_ver_е = kod_req_ver[-1].text
    # assert kod_req_ver_е == kod_req_doc_text, "Incorrect value"
    # print("Expected value Код", kod_req_doc_text, ", actual value Код", kod_req_ver_е, ".")

    # Переходим на последнюю страницу
    next_page = browser.find_elements_by_css_selector('body>div>div>div>div>div>div>div>div>div>ul>li')
    next_page[-1].click()

    # Удалаяем запись
    del_req = browser.find_elements_by_css_selector('tbody>tr>td>button')
    del_req[-1].click()

    # подтверждаем удаление
    delete_yes = browser.find_elements_by_css_selector('footer>div>button')
    delete_yes[0].click()



def test_3_add_vew_of_doc(browser):

            # заходим во вкладку "Документы"

            link_documents = browser.find_elements_by_css_selector('nav>div>ul>li>a>span')

            link_documents[1].click()


            # выбираем  строку Виды документов
            open_vew_of_doc = browser.find_element_by_css_selector('[href="#/doc_kinds"]')

            open_vew_of_doc.click()


            # открываем форму (кнопка Добавить)
            add_data = browser.find_elements_by_css_selector('[type="button"]')
            add_data[1].click()
            # добавляем запись



            # вводим код документа
            kod_doc = browser.find_element_by_css_selector('#code')
            kod_doc.click()
            kod_doc_text = "Код документа"
            kod_doc.clear()
            kod_doc.send_keys(kod_doc_text)

            # вводим Название документа
            name_doc = browser.find_element_by_css_selector('#name')
            name_doc.click()
            name_doc_text = "Название документа"
            name_doc.clear()
            name_doc.send_keys(name_doc_text)

            # поле Жизненный цикл
            life_doc = browser.find_element_by_css_selector('#lifeCycleId')
            life_doc.click()

            life_doc = browser.find_elements_by_css_selector('form>div>div>div>select>option')

            life_doc[0].click()
            time.sleep(3)
            # поле Версия жизненного цикла по умодчанию
            life_doc_by_default = browser.find_element_by_css_selector('#defaultVersionLifeStage')
            life_doc_by_default.click()
            time.sleep(3)

            life_doc[3].click()

            time.sleep(3)
            # Сохраняем
            save_doc = browser.find_element_by_css_selector('form>div>button')
            save_doc.click()

            time.sleep(3)

            # проверяем верность записи в журнале
            # проверяем поле КОД
            #kod_ver = browser.find_elements_by_css_selector('[aria-colindex="2"]')
            #kod_ver_е = kod_ver[-1].text
            #assert kod_ver_е == kod_doc_text, "Incorrect value"
            #print("Expected value Код", kod_doc_text, ", actual value Код", kod_ver_е, ".")

            # Переходим на последнюю страницу
            #next_page = browser.find_elements_by_css_selector('body>div>div>div>div>div>div>div>div>div>ul>li>span')
            #next_page = browser.find_elements_by_css_selector('[class="page-link"]')
           # next_page[-1].click()
            #time.sleep(3)
            # Удалаяем запись
            del_req = browser.find_elements_by_css_selector('tbody>tr>td>button')
            del_req[-1].click()
            time.sleep(3)

            # Удалаяем запись
            del_req = browser.find_elements_by_css_selector('footer>div>button')
            del_req[-2].click()



