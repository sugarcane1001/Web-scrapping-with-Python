from bs4 import BeautifulSoup
import requests

'''
url = "http://www.ibm.com"
data  = requests.get(url).text 
soup = BeautifulSoup(data,"html5lib")

for link in soup.find_all('a',href=True):
    print(link.get('href'))
print()

for link in soup.find_all('img'):
    print(link)
    print(link.get('src'))
'''
    
url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DA0321EN-SkillsNetwork/labs/datasets/HTMLColorCodes.html"
data  = requests.get(url).text
soup = BeautifulSoup(data,"html5lib")
table = soup.find('table')

for row in table.find_all('tr'): 
    # Get all columns in each row.
    cols = row.find_all('td') 
    color_name = cols[2].string # store the value in column 3 as color_name
    color_code = cols[3].text # store the value in column 4 as color_code
    print("{}--->{}".format(color_name,color_code))




