import requests
import os
from bs4 import BeautifulSoup
from urllib.parse import urljoin

url = 'http://books.toscrape.com/'
r = requests.get(url)
html_soup = BeautifulSoup(r.text, 'html.parser')

title = []
image = []
price = []
avail = []
rating = []

#you can use os.path.exists if you don't care about is it file or dict
if os.path.isdir('images') is False:
     os.mkdir('images')

for element in html_soup.find_all('article', class_ = 'product_pod'):
    image_e = element.find('img', class_ = 'thumbnail')
    img_src = image_e['src'] if image_e else None
    img_alt = image_e['alt'] if image_e else None
    if img_src:
        img_url = urljoin(url, img_src)
        img_src = requests.get(img_url, stream = True)
        with open('images/' + img_alt + '.jpg', 'wb') as file:
            for byte_chunk in img_src.iter_content(chunk_size = 4096):
                file.write(byte_chunk)
        image.append('image exist')
    else:
        image.append(img_alt)

    h3_title = element.find('h3').get_text(strip = True) if element.find('h3') else None
    title.append(h3_title)
    p_price = element.find('p', class_ = 'price_color').text
    p_price = p_price.replace('Â', '')
    price.append(p_price)
    p_avail = element.find('p', class_ = 'instock availability').get_text(strip = True)
    avail.append(p_avail)
    star_rating = element.find('p', class_ = 'star-rating')['class']
    stars = star_rating[1].replace('star-rating', '').strip()
    rating.append(stars)

