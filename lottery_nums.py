import requests
from bs4 import BeautifulSoup as BS

params = {"p1":"108001","p2":"108134","l":"0","type":"5"}
res = requests.post("http://www.9800.com.tw/trend.asp",data = params)
lottery_page = BS(res.text,"html.parser")
lottery_info = lottery_page.select("tbody")[4].select("td")
for i in range(len(lottery_info)):
    if lottery_info[i].text.replace("-","").isdigit():
        print(lottery_info[i].text)

# I just suffered from an issue.
# When I was spiding the lottery web,the fetched text was not correct.
# Then,about two hours later,I finally found the solution.
# It's the lxml problem.You need use html.parser to decoding the page.