import requests
from bs4 import BeautifulSoup as BS

params = {"p1":"108001","p2":"108136","l":"0","type":"5"}
res = requests.post("http://www.9800.com.tw/trend.asp",data = params)
lottery_page = BS(res.text,"html.parser")
lottery_info = lottery_page.select("tbody")[4].select("td")

data = []
for i in range(len(lottery_info)):
    if lottery_info[i].text.replace("-","").isdigit():
        data.append(lottery_info[i].text)

lottery_infos = []
count = 1        
for i in range(0,len(data),7):
        lottery_infos.append(
                {"id":count,"period":int(data[i]),"period_date":data[i+1],
                "num1":data[i+2],"num2":data[i+3],"num3":data[i+4],"num4":data[i+5],"num5":data[i+6]
                })
        count +=1





# I just suffered from an issue.
# When I was spiding the lottery web,the fetched text was not correct.
# Then,about two hours later,I finally found the solution.
# It's the lxml problem.You need use html.parser to decoding the page.