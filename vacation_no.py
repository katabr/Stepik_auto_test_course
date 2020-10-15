
# Тест проверяет адекватность формирования диаграммы Ганта


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


FILLING_OF_APPLICATION = 60
CONSIDERATION_OF_APPLICATION = 120
NOTIFICATION_OF_RESULTS = 180



#@pytest.fixture(scope = "function")
def login_task_vacation_no( browser, help):
    # выбираем Регламенты - Задачи
     href = '[href="#/instances"]'
     help.definition(browser, href)
     time.sleep(1)
     # Открываем карточку задачи Тестовый отпуск
     xpath1 = '//b[text()="Тестовый отпуск - нет"]'
     help.f_xpath(browser, xpath1)
     test_vacation = browser.find_element_by_xpath(xpath1)
     ActionChains(browser).move_to_element(test_vacation).double_click().perform()
     time.sleep(1)
     # Выбираем вкладку Аналитика
     xpath = '//a[text()="Аналитика"]'
     help.f_xpath(browser, xpath)






@pytest.mark.skip()
# Тест 1 "Прохождение бизнес-процесса Полноценный отпуск - ответ отрицательный"
def test_1_vacation_no(browser, help):
    #WDW = WebDriverWait(browser, 15)
    #browser = self.driver

    def prep_definition_no(n, m, l, k):
    # выбираем Регламенты - Регламенты
        href = '[href="#/definitions"]'
        help.definition(browser, href)
        time.sleep(1)
    # выбираем строку Регламента ОТПУСК
        line_definition = browser.find_elements_by_css_selector('tr>td>b')
        definition_vacation = browser.find_element_by_xpath('//*[text()="ОТПУСК"]')
        time.sleep(1)
        i = 0
        while line_definition [i] != definition_vacation:
            i+=1
            browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        time.sleep(1)
    # запускаем процесс ОТПУСК
        selector = '[class="start-icon text-black"]'
        help.f_selectors( browser, selector, i)
        time.sleep(1)


    # 1 заполняем поля формы стартового узла
        browser.implicitly_wait(5)
    # Поле Название процесса
        selector = '#processInstanceSubject'
        text = "Тестовый отпуск - нет"
        help.past_text(browser, selector, text)
        time.sleep(1)
    # Поле Важность
        selector = '#processInstanceImportance'
        help.f_selectors(browser, selector)
        time.sleep(1)
    # важность Высокая
        selector = '[value="H"]'
        help.f_selectors(browser, selector)
        time.sleep(1)
    #  Заполняем поля участников процесса (vasiliev_nv)
        for k in range(3):
            selector = '[class="choose-icon"]'
            help.f_selectors(browser, selector, k)
            xpath = '//td[text()="vasiliev_nv"]'
            help.f_xpath(browser, xpath)
        time.sleep(1)
    # нажимаем кнопку Подтвердить
        xpath = '//button[text()="Подтвердить"]'
        help.f_xpath(browser, xpath)
        time.sleep(1)
    # проверяем, что процесс запущен, нажимаем ОК
        time.sleep(3)
    #browser.implicitly_wait(10)
        alert = browser.switch_to.alert
        alert.accept()
        time.sleep(1)

# Ожидание задания Подача заявления
        time.sleep(n)

    # выбираем Регламенты - Задания
        href = '[href="#/nodes"]'
        help.definition(browser, href)
        time.sleep(3)
   # исполняем задание Подача заявления
        xpath = '//*[text() = "Тестовый отпуск - нет - Подача заявления"]'
        help.done(browser, xpath)
        time.sleep(1)


    # 2 заполняем поля формы исполнения Подача заявления
        browser.implicitly_wait(5)
    # Поле Заявление
        selector = '[type="text"]'
        text = "Текст тестового заявления"
        help.past_text(browser, selector, text)
        time.sleep(1)
    # Поле Дата1
        selector_data1 = ' div>input '
        data1 = browser.find_elements_by_css_selector(selector_data1)
        time.sleep(1)
        data1[1].click
        action = ActionChains(browser)
        action.send_keys(Keys.TAB).send_keys(11).send_keys(12).send_keys(2020).send_keys(Keys.TAB).send_keys(22).send_keys(12).send_keys(Keys.TAB).send_keys(15).send_keys(12).send_keys(2020).send_keys(Keys.TAB).send_keys(17).send_keys(30).perform()
        time.sleep(1)
    # нажимаем кнопку Подтвердить
        xpath = '//button[text()="Подтвердить"]'
        help.f_xpath(browser, xpath)
        time.sleep(1)

    # проверяем, что процесс запущен, нажимаем ОК
        time.sleep(3)
        browser.implicitly_wait(10)
        alert = browser.switch_to.alert
        alert.accept()
        time.sleep(1)

    # Ожидание задания Контроль
        time.sleep(m)

    # исполняем задание Контроль
        xpath = '//*[text() = "Тестовый отпуск - нет - Подача заявления"]'
        help.done(browser, xpath)

    #browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    # нажимаем кнопку Подтвердить
        xpath = '//button[text()="Снять с контроля"]'
        help.f_xpath(browser, xpath)


    # проверяем, что процесс запущен, нажимаем ОК
        time.sleep(3)
        browser.implicitly_wait(10)
        alert = browser.switch_to.alert
        alert.accept()
        time.sleep(1)

    # Ожидание задания Рассмотрение заявления
        time.sleep(l)

    # исполняем задание Рассмотрение заявления
        xpath = '//*[text() = "Тестовый отпуск - нет - Рассмотрение заявления"]'
        help.done(browser, xpath)
        time.sleep(1)
    # заполняем поле отпустить Да
        selector = '[value="Н"]'
        help.f_selectors(browser, selector)
        time.sleep(1)
    # заполняем поле Резолюция
        selector = '[type="text"]'
        text = "Не отпустить"
        help.past_text(browser, selector, text, i=2)
        time.sleep(1)
    # нажимаем кнопку Подтвердить
        xpath = '//button[text()="Подтвердить"]'
        help.f_xpath(browser, xpath)

        time.sleep(3)
    # проверяем, что процесс запущен, нажимаем ОК
        browser.implicitly_wait(10)
        alert = browser.switch_to.alert
        alert.accept()
        time.sleep(1)

    # Ожидание задания Уведомление о результате
        time.sleep(k)

    # исполняем задание Уведомление о результате
        xpath = '//*[text() = "Тестовый отпуск - нет - Уведомление о результате"]'
        help.done(browser, xpath)
        time.sleep(1)
    # нажимаем кнопку Подтвердить
        xpath = '//button[text()="Подтвердить"]'
        help.f_xpath(browser, xpath)
        time.sleep(1)

    # проверяем, что процесс запущен, нажимаем ОК
        time.sleep(3)
        browser.implicitly_wait(10)
        alert = browser.switch_to.alert
        alert.accept()
        time.sleep(1)

    # запускаем процесс прохождения регламента Отпуск


    prep_definition_no(1, FILLING_OF_APPLICATION, CONSIDERATION_OF_APPLICATION, NOTIFICATION_OF_RESULTS)
    xpath = '//*[text_contain() = "Тестовый отпуск - нет"]'
    assert help.check_no_exists_by_xpath(browser, xpath) , "Регламент - Отпуск ответ отрицательный- не выполнен"




# Тест 2-6 "Проверка наличия элементов диаграммы Ганта в списке для бизнес-процесса Полноценный отпуск - ответ отрицательный"

#@pytest.mark.skip()
class TestPresenceTreeTaskNo():
    @pytest.mark.skip()
    def test_2_tree_filing_of_applicaton_no(self, browser,help):

        login_task_vacation_no(browser, help)
        xpath = '//div[text()="Подача заявления"]'
        assert help.check_exists_by_xpath(browser,xpath), "Задача - Подача заявления - не найдена"

    @pytest.mark.skip()
    def test_3_tree_consideration_of_applicaton_no(self, browser, help):

        login_task_vacation_no(browser, help)
        xpath = '//div[text()="Рассмотрение заявления"]'
        assert help.check_exists_by_xpath(browser, xpath), "Задача - Рассмотрение заявления - не найдена"
        time.sleep(1)

    @pytest.mark.skip()
    def test_4_tree_accrual_of_vacation_pay_no(self, browser, help):
        xpath = '//div[text()="Начисление отпускных"]'
        assert help.check_no_exists_by_xpath(browser, xpath), "Задачи - Начисление отпускных - не должно быть"
        time.sleep(1)

    @pytest.mark.skip()
    def test_5_tree_preparation_of_documents_no(self, browser, help):
        xpath = '//div[text()="Подготовка документов"]'
        assert help.check_no_exists_by_xpath(browser, xpath), "Задачи - Подготовка документов - не должно быть"
        time.sleep(1)

    @pytest.mark.skip()
    def test_6_tree_notification_of_results_no(self, browser, help):

        login_task_vacation_no(browser, help)
        xpath = '//div[text()="Уведомление о результате"]'
        assert help.check_exists_by_xpath(browser, xpath), "Задача - Уведомление о результате - не найдена"
        time.sleep(1)



# Тест 5-7 "Проверка наличия графов элементов диаграммы Ганта для бизнес-процесса Полноценный отпуск - ответ отрицательный"

#@pytest.mark.skip()
class TestPresenceLineTaskNo():

    @pytest.mark.skip()
    def test_5_task_filing_of_applicaton_no(self, browser, help):

        login_task_vacation_no(browser, help)
        xpath ='//div[text()="Подача заявления" and contains(@class, "gantt_task_content")]'
        help.f_xpath(browser, xpath)
        assert help.check_exists_by_xpath(browser, xpath), "График для задачи - Подача заявления - не найден"

    @pytest.mark.skip()
    def test_6_task_consideration_of_applicaton(self, browser, help):

        login_task_vacation_no(browser, help)
        xpath = '//div[text()="Рассмотрение заявления" and contains(@class, "gantt_task_content")]'
        assert help.check_exists_by_xpath(browser, xpath), "График для задачи - Рассмотрение заявления - не найден"
        time.sleep(1)

    @pytest.mark.skip()
    def test_7_task_notification_of_results_no(self,browser, help):

        login_task_vacation_no(browser, help)
        xpath = '//div[text()="Уведомление о результате" and contains(@class, "gantt_task_content")]'
        assert help.check_exists_by_xpath(browser, xpath), "График для задачи - Уведомление о результате - не найден"
        time.sleep(1)



# Тест 8-10 "Проверка длительности графов элементов диаграммы Ганта для бизнес-процесса Полноценный отпуск - ответ отрицательный"


#@pytest.mark.skip()
class TestDurationLineTaskNo():

    def test_8_duration_filing_of_applicaton(self, browser, help):
        login_task_vacation_no(browser, help)
        d1 = int(FILLING_OF_APPLICATION/60)
        duration = browser.find_elements_by_css_selector('div.gantt_tree_content')#.text
        duration1 = int(duration[2].text)
        #print(duration[2].text)
        #print(d1)
        assert d1 == duration1 , 'Длительность диаграммы "Подача заявления" не совпадает с ожидаемой длительностью'
        #print(duration)
        #xpath = '//div[text()="Подача заявления"]'
        #help.f_xpath(browser, xpath)
        #assert help.check_exists_by_xpath(browser, xpath), "Задача - Подача заявления - не найдена"

    #@pytest.mark.skip()
    def test_9_duration_consideration_of_applicaton(self, browser, help):
        login_task_vacation_no(browser, help)
        d2 = int(CONSIDERATION_OF_APPLICATION/60)
        duration = browser.find_elements_by_css_selector('div.gantt_tree_content')  # .text
        duration2 = int(duration[5].text)
        #print(duration[2].text)
        #print(d1)
        assert d2 == duration2, 'Длительность диаграммы "Рассмотрение заявления" не совпадает с ожидаемой длительностью'
        #xpath = '//div[text()="Рассмотрение заявления"]'
        #help.f_xpath(xpath)
        #assert help.check_exists_by_xpath(xpath), "Задача - Рассмотрение заявления - не найдена"
        time.sleep(1)

    #@pytest.mark.skip()
    def test_10_duration_notification_of_results(self, browser, help):
        login_task_vacation_no(browser, help)
        d3 = int(NOTIFICATION_OF_RESULTS/60)
        duration = browser.find_elements_by_css_selector('div.gantt_tree_content')  # .text
        duration3 = int(duration[8].text)
        #print(duration[8].text)
        #print(d1)
        assert d3 == duration3, 'Длительность диаграммы "Уведомление о результате" не совпадает с ожидаемой длительностью'
        #xpath = '//div[text()="Уведомление о результате"]'
        #help.f_xpath(browser, xpath)
        #assert help.check_exists_by_xpath(browser, xpath), "Задача - Уведомление о результате - не найдена"
        time.sleep(1)




