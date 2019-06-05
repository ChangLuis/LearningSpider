# First try.
# using the url https://movies.yahoo.com.tw/movie_comingsoon.html?page=1 to fetch the films'title,'address and 'released time.

import requests
from bs4 import BeautifulSoup as BS
from datetime import datetime

def get_page_films():
    res = requests.get("https://movies.yahoo.com.tw/movie_comingsoon.html?page=1")
    res = BS(res.text,"lxml")
    films = res.select(".release_list .release_info")
    list_films = []
    for film in films:
        dict_film = {}
        titles = film.select(".release_movie_name a")
        dict_film["film_chinese_title"] = titles[0].text.strip()
        dict_film["film_eng_title"] = titles[1].text.strip()
        dict_film["film_address"] = titles[0]["href"]

        time = film.select(".release_movie_time")[0].text
        dt = datetime.strptime(time,"上映日期 ： %Y-%m-%d")
        dict_film["dt_formate"] = dt.strftime("%Y-%m-%d")
        dict_film["content"] = film.select(".release_text span")[0].text.strip()
        list_films.append(dict_film)
    print(list_films)
