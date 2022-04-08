import requests, csv, json
from pprint import pprint
from bs4 import BeautifulSoup



url = 'https://oilprice.com/oil-price-charts'
response = requests.get(url)

page = BeautifulSoup(response.text, 'html.parser')

f = open('oilprice.csv', mode="w", encoding='utf-8')
csvwriter = csv.writer(f)

tables = page.find_all("tbody")
for table in tables:
    trs = table.find_all("tr")
    for tr in trs:
        tds = tr.find_all("td")
        if len(tds) <=1:
            continue
        else:
            name = tds[1].text
            price = tds[2].text
            change = tds[3].text
            percentage = tds[4].text.split("/n")
            lst = [name, price, change, percentage]
            csvwriter.writerow(lst)
            print("done!")
print("all done!")
response.close()
f.close()




