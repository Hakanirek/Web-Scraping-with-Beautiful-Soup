from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")

yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")

# print(soup.title)
# For taking the one tag
# article_tag = soup.find(name="span", class_="titleline").find(name="a")
# article_text = article_tag.get_text()
# article_link = article_tag.get("href")

# article_upvote = soup.find(name="span", class_="score").get_text()

# print(article_tag)
# print(article_link)
# print(article_upvote)



# For taking the all tag
tags = soup.find_all(name="span", class_="titleline")
article_tags = [tag.find(name="a") for tag in tags]
article_texts = [tag.get_text() for tag in article_tags]
article_links = [tag.get("href")for tag in article_tags]
upvote_tags = soup.find_all(name="span", class_="score")


article_upvotes = [int(score.get_text().split()[0]) for score in upvote_tags]

#print(article_texts)
#print(article_links)
#print(article_upvotes)

# finding the most upvotet article
largest_number = max(article_upvotes)
largest_index = article_upvotes.index(largest_number)
print(article_texts[largest_index])
print(article_links[largest_index])
print(article_upvotes[largest_index])
