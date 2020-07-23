import requests
from bs4 import BeautifulSoup

URL = 'https://en.wikipedia.org/wiki/NASA'

response = requests.get(URL)
# print(response)

content = response.content
soup = BeautifulSoup(content, "html.parser")
# print(soup.prettify())

result = soup.find(class='mw-parser-output')
print(result.length())


def get_citations_needed_count(URL):
    pass


def get_citations_needed_report(URL):
    pass




if __name__ == "__main__":
    pass
