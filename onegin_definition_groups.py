
# Тест проверяет возможность создания группы регламентов

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
# Тест 1 "Создание группы регламентов"
def test_1_create_definition_group(browser, help):

    # заходим в главное меню регламенты - группы регаламентов
    href = '[href="#/definition_groups"]'
    help.definition(browser, href)

    # нажимаем кнопку Добавить
    xpath = '//button[text()="Добавить"]'
    help.f_xpath(browser, xpath)

    # заполняем поле Наименование
    text = "Тестовая группа регламентов"
    selector = '#name'
    help.past_text(browser, selector, text)

    # заполняем поле Примечание
    text = "Примечания для тестовой группы регламентов"
    selector = '#comment'
    help.past_text( browser, selector, text)

    # нажимаем кнопку Сохранить
    xpath = '//*[text()="Сохранить"]'
    help.f_xpath(browser, xpath)

    # Проверяем наличие тестовой группы регламентов
    xpath = '//*[text() = "ТЕСТОВАЯ ГРУППА РЕГЛАМЕНТОВ"]'
    assert help.check_exists_by_xpath(browser, xpath), "Тестовая группа регламентов не создана"



#@pytest.mark.skip()
# Тест 2 "Изменение группы регламентов"
def test_2_change_definition_group(browser, help):

    # заходим в главное меню регламенты - группы регаламентов
    href = '[href="#/definition_groups"]'
    help.definition(browser, href)

    # Ищем строку ТЕСТОВАЯ ГРУППА РЕГЛАМЕНТОВ
    xpath = '//*[text()="ТЕСТОВАЯ ГРУППА РЕГЛАМЕНТОВ"]'
    help.f_xpath(browser, xpath)

    # изменяем поле Наименование
    text = "Измененная тестовая группа регламентов"
    selector = '#name'
    help.past_text(browser, selector, text)

    # изменяем поле Примечание
    text = "Примечания для тестовой группы регламентов изменено"
    selector = '#comment'
    help.past_text(browser, selector, text)

    # нажимаем кнопку Сохранить
    xpath = '//*[text()="Сохранить"]'
    help.f_xpath(browser, xpath)

    # Проверяем наличие измененной тестовой группы регламентов
    xpath = '//*[text() = "ИЗМЕНЕННАЯ ТЕСТОВАЯ ГРУППА РЕГЛАМЕНТОВ"]'
    assert help.check_exists_by_xpath(browser, xpath), "Тестовая группа регламентов не изменена"


#@pytest.mark.skip()
# Тест 3 "Удаление группы регламентов"
def test_3_del_definition_group(browser, help):
    # заходим в главное меню регламенты - группы регаламентов
    href = '[href="#/definition_groups"]'
    help.definition(browser, href)

    # Ищем строку ИЗМЕНЕННАЯ ТЕСТОВАЯ ГРУППА РЕГЛАМЕНТОВ
    line_definition = browser.find_elements_by_css_selector('[class="text-pointer"]')
    deleg_definition = browser.find_element_by_xpath('//b[text()="ИЗМЕНЕННАЯ ТЕСТОВАЯ ГРУППА РЕГЛАМЕНТОВ"]') # ИЗМЕНЕННАЯ ТЕСТОВАЯ ГРУППА РЕГЛАМЕНТОВ"]')
    deleg_definition.click()
    i = 0
    while line_definition[i] != deleg_definition:
        i += 1
        time.sleep(2)
        # browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # удаляем группу регламентов
    selector = '[class="remove-icon text-black"]'
    help.f_selectors(browser, selector, i)

    # подтвердить удаление
    alert = WDW(browser, 10).until(EC.alert_is_present())
    alert.accept()
    time.sleep(1)
    # Проверяем отсутствие измененной тестовой группы регламентов
    xpath = '//*[text() = "ИЗМЕНЕННАЯ ТЕСТОВАЯ ГРУППА РЕГЛАМЕНТОВ"]'
    assert help.check_no_exists_by_xpath(browser, xpath), "Тестовая группа регламентов не удалена"






