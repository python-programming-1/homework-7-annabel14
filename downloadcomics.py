import os
import pprint
import requests
from bs4 import BeautifulSoup

starting_url = 'https://www.gocomics.com/pearlsbeforeswine/2019/08/21'
i = 0
while i < 10: #for 10 comics
    res = requests.get(starting_url) #pulls html
    res.raise_for_status() #checks this url is ok
    all_html = BeautifulSoup(res.text,"html.parser")
    image_html = all_html.select("picture.item-comic-image")
    image_url = image_html[0].contents[0].attrs['src']

    image_res = requests.get(image_url)
    image_res.raise_for_status()

    base = os.path.basename(image_url) + '.png'

    image_file = open(base,'wb')
    for chunk in image_res.iter_content(100000):
        image_file.write(chunk)

    prev_link_html = all_html.select("nav.gc-calendar-nav")
    prev_link = 'https://www.gocomics.com' + prev_link_html[0].contents[1].contents[3].attrs['href']
    starting_url = prev_link
    i += 1
