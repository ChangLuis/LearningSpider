# First try.
# using the url https://movies.yahoo.com.tw/movie_comingsoon.html?page=1 to fetch the films'title,'address and 'released time.

import requests
from bs4 import BeautifulSoup as BS
from datetime import datetime

res = requests.get("https://movies.yahoo.com.tw/movie_comingsoon.html?page=1")
res = BS(res.text,"lxml")
films = res.select(".release_list .release_info")

for film in films:
    titles = film.select(".release_movie_name a")
    film_chinese_title = titles[0].text.strip()
    film_eng_title = titles[1].text.strip()
    film_address = titles[0]["href"]

    time = film.select(".release_movie_time")[0].text
    dt = datetime.strptime(time,"上映日期 ： %Y-%m-%d")
    dt_formate = dt.strftime("%Y-%m-%d")
    print(f"{film_chinese_title}, {film_eng_title}, {dt_formate}")
    print(film_address,"\n")

