import requests
from bs4 import BeautifulSoup

def tenki_jp():
    base_url = "https://tenki.jp/forecast/5/24/5210/21201/"
    ret = requests.get(base_url)
    soup =  BeautifulSoup(ret.content, "lxml")

    week = soup.find("section",{'class':'forecast-point-week-wrap'})
    print (soup.find("h3",{'class':"bottom-style date-set"}).text)
    for i in range(len(week)):
        tmp = week.find_all("td",{'class':'cityday'})[i].text.split()
        print (tmp[0],tmp[1])
        print ("最高",week.find_all("p",{'class':'high-temp'})[i].text)
        print ("最低",week.find_all("p",{'class':'low-temp'})[i].text)
        print ("降水確率",week.find_all("p",{'class':'precip'})[i].text)

def yahoo_tenki():
    base_url = "https://weather.yahoo.co.jp/weather/jp/21/5210.html#week"
    ret = requests.get(base_url)
    soup =  BeautifulSoup(ret.content, "lxml")
    week = soup.find_all('tr',{'align':'center'})
    num = len(week[0].find_all("small"))
    for i in range(1,num):
        print(week[0].find_all("small")[i].text)
        print(week[1].find_all("small")[i].text)
        temp = week[2].find_all("small")[i]
        print ("最高",temp.find('font',{'color':"#ff3300"}).text)
        print ("最低",temp.find('font',{'color':"#0066ff"}).text)
        print ("降水確率",week[3].find_all("small")[i].text)
        
if __name__ == "__main__":
    tenki_jp()
    # yahoo_tenki()