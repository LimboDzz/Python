import requests
from bs4 import BeautifulSoup
import pandas
baseurl="https://www.thewhiskyexchange.com"
url="https://www.thewhiskyexchange.com/c/35/japanese-whisky"
headers={
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36"
}
def get(url,headers):
    data=[]

    res=requests.get(url,headers=headers)
    document=BeautifulSoup(res.content,"html.parser")
    links=document.find_all("a",class_="product-card",href=True)
    for link in links:
        href=baseurl+link["href"]
        dataInside=getInside(href, headers)
        data.append(dataInside)
    return data


def getInside(url,headers):
    res=requests.get(url,headers=headers)
    print(res.status_code)
    document=BeautifulSoup(res.content,"html.parser")
    header=document.find("header", class_="product-main__header")
    name=header.find("h1", class_="product-main__name").text
    lis=header.find("ul").find_all("li")
    flavour=lis[0].text
    bottling="No bottling info."
    if(len(lis)>1):
        bottling=lis[1].text
    percent=header.find("p",class_="product-main__data").text
    review=header.find("div",class_="product-main__attraction").find("span", class_=False)
    if(review):
        review=review.text
    else:
        review="No reviews."
    return {
        "name":name.strip(),
        "flavour":flavour.strip(),
        "percent":percent.strip(),
        "review":review.strip(),
    }

df=pandas.DataFrame(get(url,headers))
df.to_csv("whisky.csv")