import requests

from bs4 import BeautifulSoup
import pandas as pd

def jls_extract_def(url):
    res=requests.get(url)
    res.encoding="gbk"
    document=BeautifulSoup(res.text,"html.parser")
    table=document.find_all("table",class_="box no_doc")[2]
    data=[]
    for i in table.find_all("a"):
        # print(i["title"])
        arr=i["title"].split("——")
        title=arr[0]
        author=arr[1]
        data.append({"title":title,"author":author})
    return data


data = jls_extract_def("https://www.yqshuwang.com/")
df=pd.DataFrame(data)
print(df.head())