#i made this script on search word book but i don't think it will give the same
#output for other things as watches(because here there isno't writer for example
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import re
import pandas as pd
import xlsxwriter

def search(var):
    base_url = 'https://www.amazon.com'
    session = requests.Session()
    req = session.headers.update({'User-Agent': 'Mozilla/5.0 ',
                                    'Referer': "https://www.amazon.com/"})
    req = session.get(base_url)
    #here we search for all Departement
    #for speed please select a certain Departement
    parameters = {
    'url': 'search-alias%3Daps',
    'field-keywords': var
    }
    new_url = urljoin(base_url, '/s/ref=nb_sb_noss?')
    html_content = session.get(new_url, params = parameters)
    return html_content


#here you should have something to do but i don't so i will get
#the name of book, writer, stars for the book,
#how many person gave stars and href of the picture of book
titles = []
writers = []
stars = []
numb_person = []
href_pictures = []

def parse_content(lis):
    for element in lis:
        html_soup = BeautifulSoup(element.text, 'html.parser')
        for html in html_soup.find_all('div', class_ = "a-fixed-left-grid-col a-col-right"):
            if html.select('h3.a-size-small.s-inline.a-text-normal'):
                obj1 = html.select('h2.a-size-medium.s-inline.s-access-title.a-text-normal')
                title = obj1[0].text if obj1 else None
                titles.append(title)
                obj2 = html.select('span.a-size-small.a-color-secondary a')
                writer = obj2[0].text if obj2 else None
                writers.append(writer)
                obj3 = html.select('i.a-icon.a-icon-star span.a-icon-alt')
                star = obj3[0].text if obj3 else None
                star = re.match('\d((\.\d)?)', star).group(0)
                stars.append(star)
                obj4 = html.find('a',href = re.compile('book#customerReviews$'))
                person = obj4.text if obj4 else None
                numb_person.append(person)
                obj5 = html.find_previous('img', width = '218', height = '218')
                href_picture = obj5['src'] if obj5 else None
                href_pictures.append(href_picture)


def find_elements(lis):
    html_content_list = []
    try:
        if type(lis) is list:
            for element in lis:
                var2 = search(element)
                html_content_list.append(var2)
        else:
            raise TypeError

    except TypeError:
        print('please send for function find_elements list')

    if html_content_list is None:
        print('sorry we did not find any thing with your list')
    else:
        parse_content(html_content_list)



find_elements(['book'])

df = pd.DataFrame({'titles': titles,
                   'writers': writers,
                   'stars': stars,
                   'numb_person': numb_person,
                   'href_pictures': href_pictures})

writer = pd.ExcelWriter('amazonscraping.xlsx', engine = 'xlsxwriter')
df.to_excel(writer, index = False)
#writer.save()

#workbook = writer.book
worksheet = writer.sheets['Sheet1']
length = len(titles)
worksheet.set_column('A1:A%i' %length, 50)
worksheet.set_column('B1:B%i' %length, 50)
worksheet.set_column('E1:E%i' %length, 100)
writer.save()

#as note here i search with all departement but if you try to test the same
#name on amazon search it will automatically move you for example to
#books or Alxa skills so if you want to compare result of script with the
#result of browser add in search function this line and take its output and add
#it to your browser output  "html_content.request.url"
