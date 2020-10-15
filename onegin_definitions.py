
# Тест проверяет возможность создания, изменения, удаления регламента

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as WDW
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import pytest
import time

#@pytest.mark.skip()
# Тест 1 "Создание нового регламента"
def test_1_create_definition(browser, help):

# Создаем тестовую группу регламентов
    # заходим в главное меню регламенты - группы регаламентов
    href = '[href="#/definition_groups"]'
    help.definition(browser, href)

    # нажимаем кнопку Добавить
    xpath = '//button[text()="Добавить"]'
    help.f_xpath(browser, xpath)

    # заполняем поле Наименование
    text = "Группа для проверки регламентов"
    selector = '#name'
    help.past_text(browser, selector, text)

    # заполняем поле Примечание
    text = "Примечания для тестовой группы регламентов"
    selector = '#comment'
    help.past_text(browser, selector, text)

    # нажимаем кнопку Сохранить
    xpath = '//*[text()="Сохранить"]'
    help.f_xpath(browser, xpath)

# Добавляем новый регламент
    # заходим в главное меню регламенты - регламенты
    href = '[href="#/definitions"]'
    help.definition(browser, href)

    # нажимаем кнопку Добавить
    xpath = '//*[text()="Добавить "]'
    help.f_xpath(browser, xpath)

    # заполняем поле Код
    text = "НТР"
    selector = '#code_a'
    help.past_text(browser, selector, text)

    # заполняем поле Наименование
    text = "Новый тестовый регламент"
    selector = '#name_a'
    help.past_text(browser, selector, text)

    # выбираем Группу регламентов
    selector = '#group_a'
    help.f_selectors(browser, selector)
    xpath = '//option[text()=" Группа для проверки регламентов "]'
    help.f_xpath(browser, xpath)

    # выбираем Состояние регламентов
    selector = '#state_a'
    help.f_selectors(browser, selector)
    selector = '[value="З"]'
    help.f_selectors(browser, selector)

    # заполняем поле Описание
    text = "Описание для тестового регламента"
    selector = '#description_a'
    help.past_text(browser, selector, text)

    # нажимаем кнопку Сохранить
    xpath = '//*[text()="Сохранить"]'
    help.f_xpath(browser, xpath)


    # Проверяем наличие тестового регламента
    xpath = '//*[text() = "НОВЫЙ ТЕСТОВЫЙ РЕГЛАМЕНТ"]'
    #element = WDW(browser, 10).until(EC.element_to_be_clickable((By.ID, xpath)))
    #element.click()
    assert help.check_exists_by_xpath(browser, xpath), "Новый тестовый регламент не создан"


#@pytest.mark.skip()
# Тест 2 "Смена названия и состояния регламента"
def test_2_change_state_of_definition(browser, help):

    # заходим в главное меню регламенты - регламенты
    href = '[href="#/definitions"]'
    help.definition(browser, href)

    # ищем строку  Новый тестовый регламент
    xpath = '//b[text()="НОВЫЙ ТЕСТОВЫЙ РЕГЛАМЕНТ"]'
    help.f_xpath(browser, xpath)

    # изменяем Состояние регламентов
    selector = '#state'
    help.f_selectors(browser, selector)
    selector = '[value="О"]'
    help.f_selectors(browser, selector)

    # заполняем поле Наименование
    text = "Измененный новый тестовый регламент"
    selector = '#name'
    help.past_text(browser, selector, text)

    # нажимаем кнопку Сохранить изменения
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    xpath = '//*[text()="Сохранить изменения "]'
    help.f_xpath(browser, xpath)

    # Проверяем наличие тестового регламента
    xpath = '//*[text() = "ИЗМЕНЕННЫЙ НОВЫЙ ТЕСТОВЫЙ РЕГЛАМЕНТ"]'
    assert help.check_exists_by_xpath(browser, xpath), "Новый тестовый регламент не изменен"


#@pytest.mark.skip()
# Тест 3 "Удаление регламента"
def test_3_del_definition_group(browser, help):

    # заходим в главное меню регламенты - регламенты
    href = '[href="#/definitions"]'
    help.definition(browser, href)

    # Ищем строку Измененный новый тестовый регламент
    line_definition = browser.find_elements_by_css_selector('[class="text-pointer"]')
    deleg_definition = browser.find_element_by_xpath('//b[text()="ИЗМЕНЕННЫЙ НОВЫЙ ТЕСТОВЫЙ РЕГЛАМЕНТ"]')
    deleg_definition.click()
    i = 0
    while line_definition[i] != deleg_definition:
        i += 1
        # browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # нажимаем кнопку Удалить
    selector = '[class="remove-icon text-black"]'
    help.f_selectors(browser, selector, i)

    # подтвердить удаление
    alert = WDW(browser, 10).until(EC.alert_is_present())
    alert.accept()

    # Проверяем отсутствие тестового регламента
    xpath = '//b[text() = "ИЗМЕНЕННЫЙ НОВЫЙ ТЕСТОВЫЙ РЕГЛАМЕНТ"]'
    time.sleep(1)
    assert help.check_no_exists_by_xpath(browser, xpath), "Новый тестовый регламент не удален"

    # заходим в главное меню регламенты - группы регаламентов
    href = '[href="#/definition_groups"]'
    help.definition(browser, href)

    # Ищем строку Группа для проверки регламентов
    line_definition = browser.find_elements_by_css_selector('[class="text-pointer"]')
    deleg_definition = browser.find_element_by_xpath('//b[text()="ГРУППА ДЛЯ ПРОВЕРКИ РЕГЛАМЕНТОВ"]')
    deleg_definition.click()
    i = 0
    while line_definition[i] != deleg_definition:
        i += 1
        # browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # удаляем группу регламентов
    selector = '[class="remove-icon text-black"]'
    help.f_selectors(browser, selector, i)

    # подтвердить удаление
    alert = WDW(browser, 10).until(EC.alert_is_present())
    alert.accept()

    # Проверяем отсутствие измененной тестовой группы регламентов
    xpath = '//*[text() = "ИЗМЕНЕННЫЙ НОВЫЙ ТЕСТОВЫЙ РЕГЛАМЕНТ"]'
    time.sleep(1)
    assert help.check_no_exists_by_xpath(browser, xpath), "Группа для проверки регламентов не удалена"

    print("Тестовые данные удалены")



