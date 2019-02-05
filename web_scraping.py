import requests
import urllib3
from bs4 import BeautifulSoup
import validators

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
url = input("Enter a website to extract the URL's from: ")
response = requests.get("http://" + url, verify=False)  # Sends a GET request and return response object

# Ignore ssl verification
session = requests.Session()
session.verify = False

# Content of the response, in unicode.
content = response.text

# A string or a file-like object representing markup to be parsed
soup = BeautifulSoup(content, features="html.parser")


# find_all = Extracts a list of Tag objects that match the given criteria.
#            You can specify the name of the Tag and any
#            attributes you want the Tag to have.

def get_links(soup):
    print("\nLinks in page:")
    for link in soup.find_all('a'):
        good_link = str(link.get('href'))
        if validators.url(good_link):
            print(good_link)

def get_pdfs(soup):
    print("\nPDFs in page:")
    for link in soup.find_all('a'):
        good_link = str(link.get('href'))
        if validators.url(good_link) and good_link.rsplit('.',1)[-1] == 'pdf':
            print(good_link)

def menu():
    option = True
    while(option):
        print("\n1. Get links from page")
        print("2. Get pdfs from page")
        print("3. Exit\n")

        option = input("Enter option: ")
        if option == "1":
            get_links(soup)
        elif option == "2":
            get_pdfs(soup)
        elif option == "3":
            option = False
        elif option != "":
            print("\n Not a valid option")

menu()

