
urls=getUrls()
for url in urls[0:5]:
    for i in range(1,2):
        data=scrape(url["url"]+f"/pg{i}",url["name"])
        print("Done with "+url["name"]+f" - {i}")
log(data)