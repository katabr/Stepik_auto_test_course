
# Тест проверяет возможность добавления, изменения, удаления новой записи в Журнале


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.common.exceptions import NoSuchElementException
import time



def test_add_record_in_logbook(browser):
	browser.implicitly_wait(5)

	browser.implicitly_wait(5)
	from selenium.common.exceptions import NoSuchElementException
	def check_exists_by_xpath(xpath):
		try:
			browser.find_element_by_xpath(xpath)
		except NoSuchElementException:
			return False
		return True


	# заходим во вкладку "Журналы"
	link_logbook = browser.find_element_by_css_selector('[href="#/journals"]')
	link_logbook.click()

	# открываем  Журнал дежурного
	#open_journal = browser.find_element_by_xpath('//td[text()="Журнал дежурного"]')
	#open_journal.click()

	line_definition = browser.find_elements_by_css_selector('tr>td')
	duty_logbook = browser.find_element_by_xpath('//*[text()="Журнал дежурного"]')

	i = 0
	while line_definition[i] != duty_logbook:
		i += 1
		#browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

	# открываем  Журнал дежурного
	#print(i)
	k = int((i-1)/8)
	print(k)

	duty_logbook_go = browser.find_elements_by_xpath('//button[text()="Открыть"]')
	duty_logbook_go[k].click()



	# открываем форму
	#add_data = browser.find_elements_by_css_selector('[type="button"]')
	#add_data[1].click()
	#time.sleep(2)
	#browser.implicitly_wait(10)

	# добавляем запись
	add_button = browser.find_element_by_xpath('//button[text()="Добавить запись"]')
	add_button.click()
	browser.implicitly_wait(10)

	# проверяем наличие старых полей, удаляем
	#old_record = browser.find_elements_by_css_selector('tr>td')
	#old_record_line = browser.find_element_by_xpath('//*[text()="НОВЫЙ КОД"]')

	#i = 0
	#while old_record[i] != old_record_line:
		#i += 1
		#browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
	#print(i)


    # удаляем старую запись
    #print(i)
    #l = int((i-1)/6)

	#button_vacation_go = browser.find_elements_by_css_selector( '[class="btn remove-icon text-black btn-secondary btn-sm"]')
	#button_vacation_go[l].click()


    # Заполняем поле код
	#kod = browser.find_elements_by_css_selector('[class="form-group"]')
	kod = browser.find_elements_by_css_selector('[type="text"]')
	kod[0].click()
	kod0_text = "НОВЫЙ_КОД"
	#kod[0].clear()
	kod[0].send_keys(kod0_text)


	# открываем календарь приема
	data1 = browser.find_elements_by_css_selector('[class="form-control text-break text-wrap bg-transparent h-auto text-muted"]')#fill-rule="evenodd"]')#button>svg>g>path')
	data1[0].click()

	# выбираем дату 1
	day1 = browser.find_elements_by_css_selector('div>span')#[data-date="2014-08-06"]')
	day1[15].click()

	# выбираем время приема
	data1[1].click()
	#time_1 = browser.find_elements_by_xpath('//label[text()="Время"]')
	#time_1[0].click()
	time_now = browser.find_element_by_xpath('//button[text()="Текущее"]')
	time_now.click()

	# открываем календарь передачи
	data1[2].click()

	# выбираем дату 2
	day2 = browser.find_elements_by_css_selector('div>span')
	day2[20].click()

	# выбирает время передачи

	data1[3].click()
	#time_2 = browser.find_element_by_xpath('//label[text()="Время"]')
	#time_2.click()
	time_now = browser.find_element_by_xpath('//button[text()="Текущее"]')
	time_now.click()


	# вводим Содержание задачи

	#kod = browser.find_elements_by_css_selector('[type="text"]')
	kod[1].click()
	kod1_text = "Тестовая задача"
	kod[1].clear()
	kod[1].send_keys(kod1_text)

	kod = browser.find_elements_by_css_selector('[type="text"]')
	kod[2].click()
	kod2_text = "Тестовое примечание"
	kod[2].clear()
	kod[2].send_keys(kod2_text)

	# сохраняем
	save = browser.find_element_by_xpath('//button[text()="Сохранить"]')
	save.click()

	# окно закрывается

	# проверяем верность записи в журнале
	# проверяем поле КОД
	#kod_ver = browser.find_elements_by_css_selector('[aria-colindex="1"]')
	#kod_ver_е = kod_ver[-1].text
	#assert kod_ver_е == kod_text, "Incorrect value"
	#print("Expected value Код", kod_text, ", actual value Код", kod_ver_е, ".")

	# Проверяем наличие записи

	if check_exists_by_xpath('//td[text()="НОВЫЙ_КОД"]') == True:
		print("Тестовая запись создана")
	else:
		print("Тестовая запись не создана")



    # изменяем запись

# ищем строку с названием
	line_definition = browser.find_elements_by_css_selector('tr>td')
	definition_vacation2 = browser.find_element_by_xpath('//*[text()="НОВЫЙ_КОД"]')

	i = 0
	while line_definition[i] != definition_vacation2:
		i += 1
		browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

	# запускаем процесс Полноценный отпуск 2
	button_vacation_go = browser.find_elements_by_css_selector(
		'[class="btn start-icon text-black btn-secondary btn-sm"]')
	button_vacation_go[i].click()







	change_button = browser.find_elements_by_css_selector('table>tbody>tr>td>button')
	change_button[-2].click()

	#изменяем поле записи
	kod = browser.find_elements_by_css_selector('[type="text"]')
	kod[0].click()
	kod_text = "КОД_ИЗМЕНЕН"
	kod[0].clear()
	kod[0].send_keys(kod_text)
	# сохраняем
	save = browser.find_element_by_xpath('//button[text()="Сохранить"]')
	save.click()

	# Проверяем наличие измененной записи

	if check_exists_by_xpath('//td[text()="КОД_ИЗМЕНЕН"]') == True:
		print("Тестовая запись изменена")
	else:
		print("Тестовая запись не изменена")






	# удаляем запись
	delete = browser.find_elements_by_css_selector('table>tbody>tr>td>button')
	delete[-1].click()

	# подтверждаем удаление
	delete_yes = browser.find_elements_by_css_selector('footer>div>button')
	delete_yes[0].click()


	# Проверяем отсутствие измененной записи

	if check_exists_by_xpath('//td[text()="Измененная запись"]') == True:
		print("Тестовая запись не удалена")
	else:
		print("Тестовая запись удалена")
