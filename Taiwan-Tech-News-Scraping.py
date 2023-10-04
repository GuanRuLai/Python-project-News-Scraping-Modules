from technews import TechNews
news3 = TechNews("business").get_news_by_page(3)
# print(news3)

from datetime import datetime
now = datetime.now()
# set date format
str_time = now.strftime("%Y-%m-%d %H:%M:%S")
date1 = str_time[:10] # current date

content = news3["news_contents"]
for key in content:
    mononews = content[key]
    print("新聞標題：", mononews["title"])
    print("新聞連結：", mononews["link"])
    if "ago" in mononews["date"]:
        mononews["date"] = date1
    print("發布日期：", mononews["date"])
    print("===============================================")