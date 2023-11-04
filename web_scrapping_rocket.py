
from bs4 import BeautifulSoup
import requests

table="<table><tr><td id='flight'>Flight No</td><td>Launch site</td> <td>Payload mass</td></tr><tr> <td>1</td><td><a href='https://en.wikipedia.org/wiki/Florida'>Florida<a></td><td>300 kg</td></tr><tr><td>2</td><td><a href='https://en.wikipedia.org/wiki/Texas'>Texas</a></td><td>94 kg</td></tr><tr><td>3</td><td><a href='https://en.wikipedia.org/wiki/Florida'>Florida<a> </td><td>80 kg</td></tr></table>"
table_bs = BeautifulSoup(table, 'html5lib')
print(table_bs.prettify())


table_rows=table_bs.find_all('tr')
print(table_rows)
print()

first_row =table_rows[0]
print(first_row)
print()

for i,row in enumerate(table_rows):
    print("row",i)
    cells=row.find_all('td')
    for j,cell in enumerate(cells):
        print('colunm',j,"cell",cell)
print()

print(table_bs.find_all(id="flight"))
print()

print(table_bs.find_all(href="https://en.wikipedia.org/wiki/Florida"))
print()







