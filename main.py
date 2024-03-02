from bs4 import BeautifulSoup
import lxml  # when website is cml used that instead of html parser

with open("website.html") as file:
    contents = file.read()

soup = BeautifulSoup(contents, "html.parser")  # write lxml

# Writing the title tag
print(soup.title)

# Writing the name of title tag
print(soup.title.name)

# Writing the string of title tag
print(soup.title.string)

# Writing the h1 tag
print(soup.h1)

# Writing the ul tag
print(soup.ul)

# Writing the a tag
print(soup.a)

# Indent the html code
# print(soup.prettify())
