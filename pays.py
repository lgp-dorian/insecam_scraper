from bs4 import BeautifulSoup as bs4
import requests
import re
import yarl 
import geoip2.database
import csv

reader = geoip2.database.Reader('./GeoLite2-City.mmdb')

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/109.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Accept-Language': 'fr,fr-FR;q=0.8,en-US;q=0.5,en;q=0.3',
    # 'Accept-Encoding': 'gzip, deflate',
    'Referer': 'http://insecam.org/en/bycountry/FR/',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
}

pays_code = 'FR'

response = requests.get('http://insecam.org/en/bycountry/' + pays_code, headers=headers)
soup = bs4(response.text, features="lxml")
navbar = soup.findAll("nav", {"class": "navigation"})[0].find_all("ul", {"class": "pagination"})[0]

max_page = navbar.prettify().split('\n')[2]

max_page = re.findall(r'\d+', max_page)[0]

f = open('urls_'+ pays_code +'.csv', 'a')
writer = csv.writer(f)


for b in range(1, int(max_page) + 1):
    response = requests.get('http://insecam.org/en/bycountry/'+ pays_code +'/?page=' + str(b), headers=headers)
    soup = bs4(response.text, features="lxml")
    images = soup.findAll('img')
    for image in images:
        if "yandex.ru" in image['src']:
            pass
        elif "data:image/gif;base64" in image['src']:
            pass
        else:
            host = yarl.URL(image['src']).host
            response = reader.city(host)
            lat = response.location.latitude
            lon = response.location.longitude
            print(host)
            print(image['src'])
            writer.writerow([image['src'], host, lat, lon])
    print(b)

f.close()