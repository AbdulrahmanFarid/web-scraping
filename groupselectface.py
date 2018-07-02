from selenium import webdriver
from urllib.parse import urljoin


class Facebook():
    url = 'https://www.facebook.com/login'

    def __init__(self, username, passwd, group):
        self.username = username
        self.passwd = passwd
        self.group = group
        self.driver = webdriver.Chrome()
        self.log_in()
        self.search()
#        self.driver.quit()

    def log_in(self):
        self.driver.implicitly_wait(8)
        self.driver.get(self.url)
        self.driver.find_element_by_id('email').send_keys(self.username)
        self.driver.find_element_by_id('pass').send_keys(self.passwd)
        self.driver.find_element_by_tag_name('form').submit()
        new_url = urljoin(self.url, 'groups')
        self.driver.get(new_url)

    def search(self):
        self.a_group = self.driver.find_element_by_class_name('_266w')
        self.a_group1 = self.a_group.find_element_by_tag_name('a')
        self.a_group2 = self.a_group1.get_attribute('href')
        self.link = urljoin(self.url, self.a_group2)
        self.driver.get(self.link)

obj = Facebook('user_name', 'passwd',
'Science & Free courses')
