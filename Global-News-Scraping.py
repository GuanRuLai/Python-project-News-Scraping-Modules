import newspaper
paper = newspaper.build(url="https://www.ltn.com.tw/", language="zh")

# return url of news data
print("新聞連結：")
for i, item in enumerate(paper.articles):
    print(i + 1, item.url)

# return single news data in dict type
from newspaper import Article
article = Article("https://news.ltn.com.tw/news/life/breakingnews/4448106")
article.download()
# print(article.html)

article.parse()
print("新聞標題:")
print(article.title)
print("新聞內容：")
print(article.text)
print("新聞日期：")
print(article.publish_date)

# return full text of single news data
from newspaper import fulltext # cause error in chinese news websites
article1 = Article("https://www.cnbc.com/2020/10/27/trump-biden-foreign-policy-iran-china.html")
article1.download()
print(fulltext(article1.html))