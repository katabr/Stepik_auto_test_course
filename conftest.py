from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as WDW
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import pytest
import unittest
import time
import math


@pytest.fixture()
def browser():
    browser = webdriver.Firefox()
    browser.implicitly_wait(15)

    # открываем браузер
    #ASRS = "http://10.128.20.113:8080/axel_web/#/requests.html"
    #ASRC = "http://10.128.24.113:8080/axel_web/#/requests.html"

    #local = "http://localhost:8090/axel_web/#/requests.html"
    local = "http://localhost:8090/axel_web/#/requests.html"
    browser.get(local)

    # аутентификация
    login = browser.find_element_by_css_selector('#username')
    login.send_keys("vasiliev_nv")

    button_enter = browser.find_element_by_xpath('//button[text()="Войти"]')
    button_enter.click()


    # закрываем браузер
    yield browser
    browser.quit()


#def check_exists_by_xpath_1(xpath):
   #return len(browser.find_elements_by_xpath(xpath)) > 0

#@pytest.fixture
#class FinedFunction():
    # def __init__(self, href, selector, i, xpath,  text, x ):
    #     self.href = href
    #     self.selector = selector
    #     self.i = i
    #     self.xpath = xpath
    #     self.text = text
    #     self.x = x


class Helper:
    @staticmethod
    def check_exists_by_xpath(browser, xpath):
        try:
           browser.find_element_by_xpath(xpath)
        except NoSuchElementException:
            return False
        return True

    @staticmethod
    def check_no_exists_by_xpath(browser, xpath):
        try:
            browser.find_element_by_xpath(xpath)
        except NoSuchElementException:
            return True
        return False

    @staticmethod
    def f_xpath( browser, xpath):
        varxp = browser.find_element_by_xpath(xpath)
        varxp.click()

    @staticmethod
    # добавить текст в поле
    def past_text( browser, selector, text, i=0 ):
        field = browser.find_elements_by_css_selector(selector)
        field[i].click()
        field_text = text
        field[i].clear()
        field[i].send_keys(field_text)

    @staticmethod
    # кликнуть на  i элемент из списка по селектору
    def f_selectors(browser, selector, i=0 ):
        vars = browser.find_elements_by_css_selector(selector)
        vars[i].click()



    @staticmethod
    # исполняем Задание
    def done(browser, xpath):

        def calc(x):
            return int(math.ceil(x / 7))

        line_definition = browser.find_elements_by_css_selector('td.text-left')
        definition_vacation = browser.find_element_by_xpath(xpath)
        l = 0
        while line_definition[l] != definition_vacation:
             l += 1
        #selector = 'button.start-icon.text-black'
        j = calc(l)
        #f_selectors(selector, j)
        vars = browser.find_elements_by_css_selector('button.start-icon.text-black')
        vars[j].click()

    @staticmethod
    # Заходим в один из разделов вкладки Регламенты
    def definition(browser, href):
        # заходим в главное меню Регламенты
        link_MainMenu = browser.find_element_by_xpath('//span[text()="Регламенты"]')
        link_MainMenu.click()
        browser.implicitly_wait(5)

        # выбираем Регламенты
        definitions = browser.find_element_by_css_selector(href)
        definitions.click()
        browser.implicitly_wait(5)

    @staticmethod
    def login_task_vacation_yes(browser, help):
        # выбираем Регламенты - Задачи
        href = '[href="#/instances"]'
        help.definition(browser, href)
        time.sleep(1)
        # Открываем карточку задачи Тестовый отпуск
        xpath = '//b[text()="Тестовый отпуск - да"]'
        help.f_xpath(browser, xpath)
        test_vacation = browser.find_element_by_xpath(xpath)
        ActionChains(browser).move_to_element(test_vacation).double_click().perform()
        time.sleep(1)
        # Выбираем вкладку Аналитика
        xpath = '//a[text()="Аналитика"]'
        help.f_xpath(browser, xpath)

    @staticmethod
    # кликнуть на элемент по селектору
    def f_selector(browser, selector):
        var = browser.find_element_by_css_selector(selector)
        var.click()





@pytest.fixture
def help():
    return Helper

@pytest.fixture
def definition( href, browser):
    # заходим в главное меню Регламенты
    # link_MainMenu = browser.find_element_by_xpath('//span[text()="Регламенты"]')
    # link_MainMenu.click()
    # browser.implicitly_wait(5)
    # выбираем Регламенты
    # definitions = browser.find_element_by_css_selector(href)
    definitions.click()
    browser.implicitly_wait(5)

@pytest.fixture
# кликнуть на элемент по селектору
def f_selector(selector, browser):
    var = browser.find_element_by_css_selector(selector)
    var.click()










#@pytest.fixture
#def definition(browser, href):
    # заходим в главное меню Регламенты
    #link_MainMenu = browser.find_element_by_xpath('//span[text()="Регламенты"]')
    #link_MainMenu.click()
    #browser.implicitly_wait(5)

    # выбираем Регламенты
    #definitions = browser.find_element_by_css_selector(href)
    #definitions.click()
    #browser.implicitly_wait(5)




