import requests
from bs4 import BeautifulSoup

def get_stockPrice():
    base_url = "https://tenki.jp/forecast/5/24/5210/21201/"
    ret = requests.get(base_url)
    soup =  BeautifulSoup(ret.content, "lxml")
    today = soup.find("section", {'class':'today-weather'}).text
    tommorow = soup.find("section", {'class':'tomorrow-weather'}).text
    print (tommorow)
    week = soup.find("section",{'class':'forecast-point-week-wrap'})
    print (len(week))
    for i in range(len(week)):
        print (week.find_all("td",{'class':'cityday'})[i].text)
        print ("最高",week.find_all("p",{'class':'high-temp'})[i].text,)
        print ("最低",week.find_all("p",{'class':'low-temp'})[i].text,)
        print ("降水確率",week.find_all("p",{'class':'precip'})[i].text,)
        
if __name__ == "__main__":
    get_stockPrice()