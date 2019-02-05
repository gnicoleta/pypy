import requests
from bs4 import BeautifulSoup
import validators

url = input("Enter a website to extract the URL's from: ")
response = requests.get("http://" + url) #Sends a GET request and return response object

#Content of the response, in unicode.
content = response.text

#A string or a file-like object representing markup to be parsed
soup = BeautifulSoup(content, features="html.parser")

# find_all = Extracts a list of Tag objects that match the given criteria.
#            You can specify the name of the Tag and any
#            attributes you want the Tag to have.
for link in soup.find_all('a'):
    good_link = link.get('href')
    if validators.url(good_link):
        print(good_link)
