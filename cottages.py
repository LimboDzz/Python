import requests
from bs4 import BeautifulSoup
import pandas as pd
def scrape(url,data):
    res=requests.get(url)
    doucment=BeautifulSoup(res.text,"html.parser")
    cards=doucment.find_all("dd-product-card")
    for card in cards:
        price=card.find("strong").text
        name=card.find("h2").text
        breadcrumb=card.find("p",class_="breadcrumb").text
        reference=card.find("p",class_="reference").text
        info={"name":name,"price":price,"breadcrumb":breadcrumb,"reference":reference}
        data.append(info)

data=[]
n=int(input("How many pages would you like? (1-7) "))
for i in range(1,n+1):
    url=f"https://www.brittany-ferries.co.uk/holidays/search?vt=0&s=ASC&aps=cottages&p={i}"
    scrape(url, data)
# print(data)
df=pd.DataFrame(data)
df.to_csv(f"cottages_1_{n}.csv")