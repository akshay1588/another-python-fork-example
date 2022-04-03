from counter_page import CounterPage

'''def test_counter_starts_at_one(page):
	page.goto('https://counter.onlineclock.net/')

	assert page.locator('#counter').text_content() == "1"

def test_counter_counts_up_once_on_click(page):
	page.goto('https://counter.onlineclock.net/')
	page.locator('text="Count Up"').click()
	assert page.locator('#counter').text_content() == "2"

def test_counter_counts_up_twice_on_double_click(page):
	page.goto('https://counter.onlineclock.net/')
	page.locator('text="Count Up"').dblclick()
	assert page.locator('#counter').text_content() == "3"

def test_counter_counts_down_once_on_click(page):
	page.goto('https://counter.onlineclock.net/')
	page.locator('text="Count Down"').click()
	assert page.locator('#counter').text_content() == "0"

def test_counter_counts_down_twice_on_double_click(page): #UI Testing
	page.goto('https://counter.onlineclock.net/')
	page.locator('text="Count Down"').dblclick()
	assert page.locator('#counter').text_content() == "-1"'''

def test_counter_starts_at_one(page):
	counter=CounterPage(page)
	counter.visit()

	assert counter.get_current_value()=='1'
	page.wait_for_timeout(1500)

def test_find_count_down(page):
	counter=CounterPage(page)
	counter.visit()
	a=counter.get_count_down_button()
	print(a.inner_text())
	print(a.text_content())

def test_find_count_up(page):
	counter=CounterPage(page)
	counter.visit()
	counter.get_count_up_button()

def test_press_count_down(page):
	counter=CounterPage(page)
	counter.visit()
	counter.count_down()
	assert counter.get_current_value()=='0'


def test_press_count_up(page):
	counter=CounterPage(page)
	counter.visit()
	counter.count_up()
	assert counter.get_current_value()=='2'