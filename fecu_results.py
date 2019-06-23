import requests
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
from bs4 import BeautifulSoup
import os
import time
#this function can't handle javascript
#and as website depend on javascript
#i will write result_javascript() function
def result_website():
    url = 'http://www.results.eng.cu.edu.eg'
    session = requests.Session()
    session.headers.update({'user-agent': 'Mozilla/5.0',
                            'Referer':'https://www.google.com'})
    return session.get(url)

def result_javascript():
    url = 'http://www.results.eng.cu.edu.eg'
    options = Options()
    #the following two line to preven
    #firfox from opening and run it in
    #silent mode
    options.add_argument('-headless')
    driver = Firefox(options = options)
    #here firefox open 
#    driver = Firefox()
    driver.get(url)
    is_result_appeared(driver.page_source)
    driver.quit()
 
def is_result_appeared(session_data):
    html_soup = BeautifulSoup(session_data,
                                'html.parser')
    if(html_soup.find(id = "td3").a):
        #os.system('xmessage -center "Result had appeared" ')
        #here it will give alram continuously
        while(True):
            print('\a\a')
#    else:
#        print('result did not appear yet')

       
   
if __name__ ==  '__main__':
    #is_result_appeared(result_website())
    #while(True):
        result_javascript()
    #    time.sleep(10*60)
