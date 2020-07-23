import requests
from bs4 import BeautifulSoup

URL = 'https://en.wikipedia.org/wiki/NASA'


def drill_down(URL):
    response = requests.get(URL)
    # print(response)

    soup = BeautifulSoup(response.content, "html.parser")
    # print(soup.prettify())

    body = soup.find('body')
    # print(body)

    body_content = soup.find(id='content')
    # print(body_content)

    actual_body_content = soup.find(id='bodyContent')
    # print(actual_body_content)

    mw_content = soup.find(id='mw-content-text')
    # print(mw_content)

    mw_parser = soup.find(class_='mw-parser-output')
    # print(mw_parser)

    cite_reqs = soup.find_all(class_='noprint Inline-Template Template-Fact')
    # print(cite_reqs)
    # print(len(cite_reqs))   # Returned correct count of citations needed on page
    return cite_reqs


def get_citations_needed_count(URL):
    cite_reqs = drill_down(URL)
    return len(cite_reqs)


def get_citations_needed_report(URL):
    cite_report = drill_down(URL)
    citation_text = [c.parent.text.replace('[citation needed]', '') for c in cite_report]
    print(citation_text)
    # Use list and string methods to break out the citation_text list into individual strings.





if __name__ == "__main__":
    URL = 'https://en.wikipedia.org/wiki/NASA'
    print(get_citations_needed_count(URL))
    print(get_citations_needed_report(URL))

