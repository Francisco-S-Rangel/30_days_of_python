# Python Web Scraping

# Web scraping is the process of extracting and collecting data from websites and storing it on a local machine or in a database.

import requests
from bs4 import BeautifulSoup

# url = "https://archive.ics.uci.edu/dataset/222/bank+marketing"
# # Maybe the link above will stop working eventually cause the page can removed it

# response = requests.get(url)
# status = response.status_code
# print(status)

# content = response.content
# soup = BeautifulSoup(content, "html.parser")
# print(soup.title)
# print(soup.title.get_text())
# print(soup.body)

# print("\n----------------------------------\n")

# tables = soup.find_all("table", {'cellpadding':'3'})
# print(tables)

# if len(tables) > 0:
#     table = tables[0]
#     for td in table.find("tr").find_all("td"):
#         print(td.text)

# print("No table in this page!")

url_wiki = "https://en.wikipedia.org/wiki/List_of_presidents_of_the_United_States"

# Somethimes the request will not work - cause it needs a token or header in order to get autorizathion
header = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(url_wiki, headers= header)
print(response.status_code)

soup = BeautifulSoup(response.content, "html.parser")

table = soup.find("table", class_="wikitable")

rows = table.find_all("tr")

for row in rows:
    cols = row.find_all(["th", "td"])
    data = [c.get_text(strip=True) for c in cols]
    print(data)