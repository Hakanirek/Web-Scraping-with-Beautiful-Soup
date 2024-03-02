from bs4 import BeautifulSoup
import requests
URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"


response = requests.get(URL)
response.encoding = "utf-8"
empire_web_page = response.text

soup = BeautifulSoup(empire_web_page, "html.parser")

title_tags = soup.find_all(name="h3", class_="title")

titles = [title.get_text() for title in title_tags]
print(titles)

# reversing the list
titles = titles[::-1]
print(titles)



with open("100_movies.txt", mode="w") as file:
    for title in titles:
        file.write(f"{title}\n")


