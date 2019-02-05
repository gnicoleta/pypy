import requests
import urllib3
from bs4 import BeautifulSoup
import validators

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
url = input("Enter a website to extract from: ")
response = requests.get("http://" + url, verify=False)  # Sends a GET request and return response object

# Ignore ssl verification
session = requests.Session()
session.verify = False

# Content of the response, in unicode.
content = response.text

# A string or a file-like object representing markup to be parsed
soup = BeautifulSoup(content, features="html.parser")


class Link:
    def __init__(self, soup):
        self.soup = soup

    def check_link(self, good_link):
        if validators.url(good_link):
            return good_link

    def parsing_method(self):
        for link in soup.find_all('a'):
            good_link = self.check_link(str(link.get('href')))
            if good_link!= None:
                print(good_link)

class PDF(Link):
    def __init__(self, soup):
        self.soup = soup

    def check_link(self, good_link):
        if validators.url(good_link) and good_link.rsplit('.',1)[-1] == 'pdf':
            return good_link

def menu():
    option = True
    links = Link(soup)
    pdfs = PDF(soup)

    while(option):
        print("\n1. Get links from page")
        print("2. Get pdfs from page")
        print("3. Exit\n")

        option = input("Enter option: ")
        if option == "1":
            links.parsing_method()
        elif option == "2":
            pdfs.parsing_method()
        elif option == "3":
            option = False
        elif option != "":
            print("\n Not a valid option")

menu()
