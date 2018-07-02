from selenium import webdriver

class Twitter():
    def __init__(self, email, passwd, search_word):
        self.email = email
        self.passwd = passwd
        self.search_word = search_word
        self.driver = webdriver.Chrome()
        self.url = 'https://twitter.com/login'
        self.log_in()
        self.search()

    def log_in(self):
        self.driver.implicitly_wait(10)
        self.driver.get(self.url)
        list1 = self.driver.find_elements_by_css_selector('div.clearfix.field')
        list1[0].find_element_by_tag_name('input').send_keys(self.email)
        list1[1].find_element_by_tag_name('input').send_keys(self.passwd)
        submit = self.driver.find_element_by_css_selector('button.submit.EdgeButton.EdgeButton--primary.EdgeButtom--medium').click()

    def search(self):
        search_input = self.driver.find_element_by_css_selector('input.search-input')
        search_input.send_keys(self.search_word)
        submit2 = self.driver.find_element_by_id('global-nav-search').submit()


obj = Twitter('email', 'passwd', 'searchWord')
