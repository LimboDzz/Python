import json

import requests

from random import randint

foodChoice=input("Please choose your food: ")

url=f"https://api.punkapi.com/v2/beers?food={foodChoice}"

def jls_extract_def(url):
    res=requests.get(url)
    results=json.loads(res.text)
    # print(len(results))
    beerList=[]
    for result in results:
        beerList.append({"name":result["name"],"tagline":result["tagline"],"abv":result["abv"]})
    return beerList


beerList = jls_extract_def(url)
print(beerList[randint(0, len(beerList))])