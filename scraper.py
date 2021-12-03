import requests
from bs4 import BeautifulSoup
import pandas
# import time
def getUrls():
    res=requests.get("https://sh.fang.ke.com/loupan/pg1/",headers={
        "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36 OPR/26.0.1656.60",
    })
    document=BeautifulSoup(res.content,"html.parser")
    links=document.find("div",class_="fc-main clear").find_all("a",href=True)
    urls=[]
    for link in links:
        urls.append({
            "name":link.text,
            "url":"https:"+link["href"]
        })
    return urls

def scrape(url,geolocation,data):
    # request
    res=requests.get(url,headers={
        "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36 OPR/26.0.1656.60",
    })
    # err
    if(res.status_code!=200):
        print(f"ErrorCode: {res.status_code}")
        return
    # 200
    document=BeautifulSoup(res.content,"html.parser")
    wrappers=document.find_all("div",class_="resblock-desc-wrapper")
    for wrapper in wrappers:
        name=wrapper.find("a",class_="name").text
        location=wrapper.find("a",class_="resblock-location").text.strip()
        price=wrapper.find("span",class_="number").text
        entry={
            "地区":geolocation,
            "楼盘":name,
            "地址":location,
            "元/㎡(均价)":price,
        }
        data.append(entry)

def log(data):
    df=pandas.DataFrame(data)
    df.to_excel("贝壳.xlsx")

urls=getUrls()
data=[]
for url in urls:
    for i in range(1,3):
        scrape(url["url"]+f"/pg{i}",url["name"],data)
        print("Done with "+url["name"]+f" - {i}")
log(data)