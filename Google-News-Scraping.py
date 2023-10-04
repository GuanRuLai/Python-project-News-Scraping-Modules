from scraparazzie import scraparazzie
client = scraparazzie.NewsClient(language = "chinese traditional",
                                 location = "Taiwan",
                                 query = "口罩",
                                 max_results = 10) # 5 < max_results < 100

# return news datas in dict type
items = client.export_news()
# print(items)

# show the number of news data
print(len(items))

for i, item in enumerate(items):
    print("第" + str(i + 1) + "則新聞")
    print("新聞標題：" + item["title"])
    print("新聞機構：" + item["source"])
    print("新聞連結：" + item["link"])
    print("新聞時間：" + item["publish_date"])
    print("===================================================================================")