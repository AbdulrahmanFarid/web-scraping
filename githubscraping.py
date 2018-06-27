import requests
from bs4 import BeautifulSoup
import re
import pandas as pd
import xlsxwriter

session = requests.Session()

url = 'https://github.com/{}'
userName = 'Macuyiko'

#visit the login page

r = session.get(url.format('login'))

html_soup = BeautifulSoup(r.text, 'html.parser')

form = html_soup.find('form')
my_data = {}
#Get out the hidden form element
for inp in form.select('input[type="hidden"]'):
   my_data[inp['name']] = inp['value']

my_data.update({'login':'your_email@example.com', 'password': 'your passwd'})

headers = []
languages = []
stars = []

if input('do you want to login: ') is 'y':
    r = session.post(url.format('session'), data = my_data)
    r = session.get(url.format(userName), params = ({'tab': 'repositories'}))
    html_soup = BeautifulSoup(r.text, 'html.parser')
    e_mail = html_soup.find('a', class_ = "u-email").text
    for total in html_soup.find_all('li', itemtype = "http://schema.org/Code"):
        a_headers = total.find('a', itemprop="name codeRepository")
        header = a_headers.get_text(strip = True) if a_headers else 'no header'
        headers.append(header)
        item = total.find('div', class_ = 'f6 text-gray mt-2')
        span_language = item.find('span', itemprop="programmingLanguage")
        language = span_language.get_text(strip = True) if span_language else 'unknown language'
        languages.append(language)
        a_star = item.find('a', href= re.compile('\/stargazers'))
        star = a_star.get_text(strip = True) if a_star else 'No Stars'
        stars.append(star)

    df = pd.DataFrame({'headers': headers,
                       'languages': languages,
                       'stars': stars})
    writer = pd.ExcelWriter('abdo.xlsx', engine = 'xlsxwriter')
    df.to_excel(writer, index = False, startrow = 1)

    workbook = writer.book
    worksheet = writer.sheets['Sheet1']
    length = len(stars)
    worksheet.merge_range('A1:C1', e_mail)
    worksheet.set_column('A2:A%s' %length, 30)
    worksheet.set_column('B2:B%s' %length, 15)
