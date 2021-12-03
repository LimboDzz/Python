import requests
from bs4 import BeautifulSoup
import json
import pandas as pd

url="https://www.accommodationforstudents.com/london?page=1"

def get(url):
    res=requests.get(url)
    document=BeautifulSoup(res.content,"html.parser")
    script=document.find("script",id="__NEXT_DATA__").text
    return json.loads(script) 

def parse(data,result):
    lis=data["props"]["pageProps"]["viewModel"]["areasToShowInAreaLinksSection"]
    for li in lis:
        i={
            "name":li["name"],
            "location":li["location"],
            "propertyCount":li["propertyCount"],
            "linkPath":li["linkPath"]
        }
        result.append(i)

data=get(url)
result=[]
data=parse(data,result)
df=pd.DataFrame(result)
df.to_csv("accommodation.csv")