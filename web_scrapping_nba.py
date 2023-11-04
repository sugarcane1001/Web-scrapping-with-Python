#!pip install html5lib
#!pip install bs4
from bs4 import BeautifulSoup # this module helps in web scrapping.
import requests  # this module helps us to download a web page

html="<!DOCTYPE html><html><head><title>Page Title</title></head><body><h3><b id='boldest'>Lebron James</b></h3><p> Salary: $ 92,000,000 </p><h3> Stephen Curry</h3><p> Salary: $85,000, 000 </p><h3> Kevin Durant </h3><p> Salary: $73,200, 000</p></body></html>"

soup = BeautifulSoup(html, 'html5lib')
print(soup.prettify())

tag_object=soup.title
print("tag object:",tag_object)
print("tag object type:",type(tag_object))
print()


tag_object=soup.h3
print(tag_object)

tag_child =tag_object.b
print(tag_child)

parent_tag=tag_child.parent
print(parent_tag)
print()


sibling_1=tag_object.next_sibling
print(sibling_1)

sibling_2=sibling_1.next_sibling
print(sibling_2)
print()


print(tag_child['id'])
print(tag_child.attrs)
print(tag_child.get('id'))
print()


print(soup.find_all(id="boldest"))






