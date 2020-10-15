
# Тест проверяет возможность создания делегата и его запуска для тестового регламента
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as WDW
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import pytest
import time
import math

DEF_NAME = "РЕГЛАМЕНТ ДЛЯ СОЗДАНИЯ ДЕЛЕГАТОВ"
DELEGAT_NAME = "Стартовый делегат"


#@pytest.mark.skip()
def test_1_create_definition(browser, help):

    # заходим в главное меню регламенты - регаламенты
    href = '[href="#/definitions"]'
    help.definition(browser, href)

    # нажимаем кнопку Добавить
    xpath = '//*[text()="Добавить "]'
    help.f_xpath(browser, xpath )

    # заполняем поле Код
    text = "РД"
    selector = '#code_a'
    help.past_text( browser, selector, text)

    # заполняем поле Наименование
    text = "Регламент для создания делегатов"
    selector = '#name_a'
    help.past_text( browser, selector, text)

    # выбираем Группу
    selector = '#group_a'
    help.f_selectors(browser, selector)
    selector = 'div>select>option'
    help.f_selectors( browser, selector)

    # выбираем Состояние "Открытый"
    selector = '#state_a'
    help.f_selectors(browser, selector)
    selector = '[value="О"]'
    help.f_selectors( browser, selector)

    # вводим Описание
    text = "Регламент для создания делегатов"
    selector = '#description_a'
    help.past_text(browser, selector, text)

    # нажимаем кнопку Сохранить
    xpath = '//button[text()="Сохранить"]'
    help.f_xpath(browser, xpath )

    # Проверяем наличие нового регламена
    xpath = '//*[text() = "РЕГЛАМЕНТ ДЛЯ СОЗДАНИЯ ДЕЛЕГАТОВ"]'
    assert help.check_exists_by_xpath(browser, xpath), "Регламент для создания делегатов не создан"

#@pytest.mark.skip()
# Тест 2 "Добавление нового делегата
def test_2_create_delegation(browser, help):

    # заходим в главное меню регламенты - регаламенты
    href = '[href="#/definitions"]'
    help.definition(browser, href)

    # Выбираем строку Регламента для создания делегатов
    xpath = '//b[text()="РЕГЛАМЕНТ ДЛЯ СОЗДАНИЯ ДЕЛЕГАТОВ"]'
    help.f_xpath(browser, xpath)
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # выбираем кнопку Делегаты
    xpath = '//*[text()="Делегаты "]'
    help.f_xpath(browser, xpath )
    #browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    browser.execute_script("window.scrollBy(0,-250)", "")

    # нажимаем кнопку Добавить
    xpath = '//button[text()="Добавить "]'
    help.f_xpath(browser, xpath )
    #selector = 'class = add-icon.text-black'
    #help.f_selectors(browser, selector)


    # заполняем поле Название
    text = "Стартовый делегат"
    selector = '#name'
    help.past_text( browser, selector, text)
    time.sleep(1)
    # выбираем Тип "Делегат выполнения"
    selector = '#type'
    help.f_selectors(browser, selector)
    selector = '[value="E"]'
    help.f_selectors( browser, selector)


    # выбираем Вид "Скрипт"
    selector = '#kind'
    help.f_selectors(browser, selector)
    selector = '[value="Q"]'
    help.f_selectors( browser, selector)

    # Вводим текст скрипта
    text = "print('Скрипт делегата выполнен')"
    selector = '#configuration'
    help.past_text( browser, selector, text)

    # нажимаем кнопку Сохранить
    xpath = '//*[text()="Сохранить"]'
    help.f_xpath(browser, xpath )
    time.sleep(1)
    # Проверяем наличие нового делегата в списке
    xpath = '//*[text() = "Стартовый делегат"]'
    assert help.check_exists_by_xpath(browser, xpath), "Делегат для Регламента не создан"


#@pytest.mark.skip()
# Тест 3 "Выполнение нового делегата напримере стартового узла"
def test_3_done_delegation(browser, help):

    # заходим в главное меню регламенты - регаламенты
    href = '[href="#/definitions"]'
    help.definition(browser, href)

    # Выбираем строку Регламента для создания делегатов
    xpath = '//b[text()="РЕГЛАМЕНТ ДЛЯ СОЗДАНИЯ ДЕЛЕГАТОВ"]'
    help.f_xpath(browser, xpath)
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # нажимаем кнопку Редактор
    xpath = '//*[text()="Редактор "]'
    help.f_xpath(browser, xpath )

    # создаем карточку Стартового узла
    # нажимаем кнопку Карточка
    xpath = '//*[text()="Карточка"]'
    help.f_xpath(browser, xpath)

    # нажимаем кнопку Форма
    browser.execute_script("window.scrollBy(0,-250)", "")
    xpath = '//*[text()="Форма"]'
    help.f_xpath(browser, xpath)

    # добавляем блоки в форму
    j = 0
    while j < 3 :
        # нажимаем кнопку Добавить блок
        xpath = '//*[text()="Добавить блок"]'
        help.f_xpath(browser, xpath)
        j = j+1

    # нажимаем кнопку Сохранить
    xpath = '//*[text()="Сохранить"]'
    help.f_xpath(browser, xpath)

    # подтверждаем сохранение
    #wait = WDW(browser, 10)
    alert = WDW(browser, 10).until(EC.alert_is_present())
    #alert = browser.switch_to.alert
    alert.accept()

    # возвращаемся к редактору регламента
    xpath = '//*[text()="Отмена"]'
    help.f_xpath(browser, xpath)

    # вводим наименование узла Стартовый узел
    browser.execute_script("window.scrollBy(0,-250)", "")
    text = "Стартовый узел"
    selector = '#name'
    help.past_text(browser, selector, text)

    # выбираем Обработчик событий окончания обработки
    selector = '#outDelegation'
    help.f_selectors(browser, selector)

    #list = browser.execute_script(presence_of_element_located(By.xpath('//*[text()= " Стартовый делегат"]')))
    #list[1].click()

    xpath = ('//*[text()= " Стартовый делегат"]')
    help.f_xpath(browser, xpath)
    browser.execute_script("window.scrollBy(0,-250)", "")

    # нажимаем кнопку Сохранить
    xpath = '//*[text()="Сохранить"]'
    help.f_xpath(browser, xpath)

    # нажимаем кнопку К списку регламентов
    xpath = '//button[text()="К списку регламентов"]'
    help.f_xpath(browser, xpath)


    # Ищем строку РЕГЛАМЕНТ ДЛЯ СОЗДАНИЯ ДЕЛЕГАТОВ
    line_definition = browser.find_elements_by_css_selector('[class="text-pointer"]')
    deleg_definition = browser.find_element_by_xpath('//b[text()="РЕГЛАМЕНТ ДЛЯ СОЗДАНИЯ ДЕЛЕГАТОВ"]')
    deleg_definition.click()
    i = 0
    while line_definition[i] != deleg_definition:
        i += 1
        #time.sleep(2)
        # browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # запускаем регламент
    selector = '[class="start-icon text-black"]'
    j = i*2
    help.f_selectors(browser, selector, j)
    #del_definition_group = browser.find_elements_by_css_selector('[class="start-icon text-black"]')
    #del_definition_group[i].click()
    #browser.implicitly_wait(5)

    # заполняем карточку процесса
    # заполняем поле Название процесса
    text = "Тестовый процесс делегата"
    selector = '#processInstanceSubject'
    help.past_text( browser, selector, text)

    # выбираем Тип Важности
    selector = '#processInstanceImportance'
    help.f_selectors(browser, selector)
    selector = '[value="N"]'
    help.f_selectors( browser, selector)

    # нажимаем кнопку Подтвердить
    xpath = '//*[text()="Подтвердить"]'
    help.f_xpath(browser, xpath)

    # подтверждаем форму
    alert = WDW(browser, 10).until(EC.alert_is_present())
    alert.accept()

    # заходим в главное меню регламенты - задачи
    href = '[href="#/instances"]'
    help.definition(browser, href)

    # выбираем задачу "Тестовый процесс делегата"
    xpath = '//*[text()="Тестовый процесс делегата"]'
    help.f_xpath(browser, xpath)

    # Ищем строку Тестовый процесс делегата
    line_definition = browser.find_elements_by_css_selector('[class="text-pointer"]')
    deleg_definition = browser.find_element_by_xpath('//*[text()="Тестовый процесс делегата"]')
    deleg_definition.click()
    i = 0
    while line_definition[i] != deleg_definition:
        i += 1
        browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    print(i)
    time.sleep(1)
    # открываем Журнал
    #browser.execute_script("window.scrollBy(0,-250)", "")
    selector = 'td>button.card-icon.text-black'#>font>font'
    #selector = '[style="vertical-align: inherit;"]'
    help.f_selectors(browser, selector,i)

    #xpath = '//*[text()="Журнал"]' #@and contains(@class, "x-grid3-cell-inner")]'
    #help.f_xpath(browser, xpath)
    time.sleep(1)
    # Проверяем наличие вызова делегата
    xpath = '//*[contains(text(), "Вызов делегата") ]'
    help.f_xpath(browser, xpath)
    assert help.check_exists_by_xpath(browser, xpath), "Делегат для Регламента не вызван"

    # Проверяем отсутствие ошибок вызова делегата
    xpath = '//*[text() = "Ошибка делегата"]'
    assert help.check_no_exists_by_xpath(browser, xpath), "Ошибка делегата"


# удаление тестового регламента
#@pytest.mark.skip()
def test_clean (browser, help):

    # заходим в главное меню регламенты - регаламенты
    href = '[href="#/definitions"]'
    help.definition(browser, href)

    # Выбираем строку Регламента для создания делегатов
    xpath = '//b[text()="РЕГЛАМЕНТ ДЛЯ СОЗДАНИЯ ДЕЛЕГАТОВ"]'
    help.f_xpath(browser, xpath)
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")


    if help.check_no_exists_by_xpath(browser, xpath) == True:
        print("Тестовый делегат не удален")

    # заходим в главное меню регламенты - регаламенты
    href = '[href="#/definitions"]'
    help.definition(browser, href)

    xpath = '//b[text()="РЕГЛАМЕНТ ДЛЯ СОЗДАНИЯ ДЕЛЕГАТОВ"]'
    if help.check_exists_by_xpath(browser, xpath) == True :

        # Ищем строку РЕГЛАМЕНТ ДЛЯ СОЗДАНИЯ ДЕЛЕГАТОВ
        line_definition = browser.find_elements_by_css_selector('[class="text-pointer"]')
        deleg_definition = browser.find_element_by_xpath('//b[text()="РЕГЛАМЕНТ ДЛЯ СОЗДАНИЯ ДЕЛЕГАТОВ"]')
        deleg_definition.click()
        i = 0
        while line_definition[i] != deleg_definition:
            i += 1
            # browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # удаляем регламент
        selector = '[class="remove-icon text-black"]'
        help.f_selectors(browser, selector, i)

        # подтверждаем удаление
        alert = WDW(browser, 10).until(EC.alert_is_present())
        alert.accept()

    if help.check_no_exists_by_xpath(browser, xpath) == True:
        print("Тестовый регламент для делегата не удален")

    print("Тестовые данные удалены")


#test_clean(browser, help)