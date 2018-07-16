from selenium import webdriver

def find_urls(text):
	url = 'https://www.google.com/'
	driver = webdriver.Chrome()
	driver.implicitly_wait(6)
	driver.get(url)
	i = 0
	driver.find_element_by_name('q').send_keys(text)
	driver.find_element_by_tag_name('form').submit()
	elements = driver.find_elements_by_class_name('bkWMgd')
	for element in elements:
		for a in element.find_elements_by_tag_name('a'):
			print(a.get_attribute('href'))

	input('Press ENTER to exit')
	driver.quit()

find_urls('python')
