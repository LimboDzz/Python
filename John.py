from requests_html import HTMLSession

session=HTMLSession()

url="https://www.youtube.com/c/JohnWatsonRooney/videos"

res=session.get(url)

res.html.render(sleep=1,keep_page=True,scrolldown=1)

videos=res.html.find("#video-title")

for item in videos:
    video={
        "title":item.text,
        "link":item.absolute_links
    }
    print(video)