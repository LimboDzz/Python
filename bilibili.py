from requests_html import HTMLSession
requests=HTMLSession()
url="https://www.bilibili.com/"
res=requests.get(url)
res.html.render(sleep=1)
cards=res.html.find(".video-card-recotitle")
for card in cards:
    