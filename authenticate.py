import requests
from bs4 import BeautifulSoup
import creds

postUrl="https://the-internet.herokuapp.com/authenticate"
getUrl="https://the-internet.herokuapp.com/secure"

data={
    "username":creds.username,
    "password":creds.password
}

with requests.session() as session:
    postRes=session.post(postUrl,data=data)
    if(postRes.status_code==200):
        getRes=session.get(getUrl)
        print(BeautifulSoup(getRes.text,"html.parser").prettify())
    else:
        print("Post error.")