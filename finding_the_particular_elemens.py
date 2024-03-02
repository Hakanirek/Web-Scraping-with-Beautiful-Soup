from bs4 import BeautifulSoup

with open("website.html") as file:
    contents = file.read()

soup = BeautifulSoup(contents, "html.parser")  # write lxml

# this function found the all the elements which have the a tag.

all_anchor_tag = soup.find_all(name="a")
# print(all_anchor_tag)

# this function found the all the elements which have the p tag
all_p_tag = soup.find_all(name="p")
# print(all_p_tag)

# For text in the tags we use getText()
# for tag in all_anchor_tag:
#    print(tag.getText())


# For links in the tags we use get()
# tagın istenilen özelliğine ulaşmak için get metodunun içine istediğimiz özelliği yazıyoruz
# for tag in all_anchor_tag:
#    print(tag.get("href"))

# ******************** by the attributes ***********************************
# find tags by the attributes
heading = soup.find(name="h1", id="name")
# print(heading)
# print(heading.getText())

# find tags by the attributes
section = soup.find(name="h3", class_="heading")
# print(section)
# print(section.getText())
# print(section.get("class"))


# ********************** by the CSS Selector *********************************
company_url = soup.select_one(selector="p a")
# (company_url)
# print(company_url.getText())

# Css selector by id
h1 = soup.select_one(selector="#name")
print(h1)

# Css selector by class
h3 = soup.select(selector=".heading")
print(h3)