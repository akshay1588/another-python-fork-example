def test_counter_starts_at_one(page):
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

def test_counter_counts_down_twice_on_double_click(page):
	page.goto('https://counter.onlineclock.net/')
	page.locator('text="Count Down"').dblclick()
	assert page.locator('#counter').text_content() == "-1"
