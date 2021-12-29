from bs4 import BeautifulSoup as bs
import requests

isbn = input("Please enter ISBN-13 value: ")
isbn = isbn.replace("-", "")
link = "https://isbndb.com/book/"+isbn

page = requests.get(link, timeout=5)
soup = bs(page.text, 'html.parser')

title = soup.title.text
title = title.split(":")
title = title[0].strip()


author = ""
price = ""
for tr in soup.find_all('tr'):
    tr = tr.text.split("\n")
    for each in range(len(tr)):
        tr[each] = tr[each].strip()
        if tr[each] == "Authors":
            author = tr[each+1]
        if tr[each] == "New":
            price = tr[each+1]
            break

price = float(price.replace("$", ""))
print(title)
print(author)
print(price)
