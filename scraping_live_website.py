from bs4 import BeautifulSoup
import requests

response = requests.get(url="https://news.ycombinator.com/")

# print(response.text)
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")

# for find the first elements of each
article_tag = soup.find(name="span", class_="titleline").get_text()
article_link = soup.select_one(selector=".titleline a").get("href")
article_score = soup.find(name="span", class_="score").get_text()

# print(article_tag)
# print(article_link)
# print(article_score)

# for find the all elements of each
article_tags = soup.find_all(name="span", class_="titleline")
articles = [tag.get_text() for tag in article_tags]

article_links_tags = soup.select(selector=".titleline a")
article_links = [tag.get("href") for tag in article_links_tags]

article_scores_tags = soup.find_all(name="span", class_="score")
article_scores = [int(score.get_text().split()[0]) for score in article_scores_tags]

# print(articles)
# print(article_links)
# print(article_scores)


# finding the most upvotes article
index_of_max_upvotes = article_scores.index(max(article_scores))
print(articles[index_of_max_upvotes])
print(article_links[index_of_max_upvotes])
print(max(article_scores))
