# Lab 17 - Web Scraping
Challenge:  code up a web scraper that can automate the process of manually using a web site.

## Author
Thomas Sherer, 2020-07-22

## Tools and Setup
This project was created using Poetry.
Added to Poetry were Black, bs4, pytest-watch and requests.

## Feature Tasks and Requirements
Scrape a Wikipedia page and record which passages need citations (e.g. [History of Mexico](https://en.wikipedia.org/wiki/History_of_Mexico) has 7 __*"citation needed"*__ cases, as of this writing).
- Your web scraper should report the number of citations needed.
- Your web scraper should identify those cases AND include the relevant passage.
    - e.g. Citation needed for *"lorem spam and impsum eggs"*
    - Consider the "relevant passage" to be the parent element that contains the passage, often a paragraph element.

## Implementation Notes
- Count function must be named __`get_citations_needed_count`__
    - __`get_citations_needed_count`__ takes in a __*url*__ and returns __*an integer*__.
- Report function must be named __`get_citations_needed_report`__
    - __`get_citations_needed_report`__ takes in a __*url*__ and returns __*a string*__.
    - The string should be formatted with each citation needed on it's own line, in the order found.
- Module must be named __`scraper.py`__

## Attributions and Citations
[Page under test - production](https://en.wikipedia.org/wiki/NASA) courtesy of Wikipedia. <br>
[Page under test - comparison testing](https://en.wikipedia.org/wiki/History_of_Mexico) also courtesy of Wikipedia. <br>
- Merry Cimakasky helped with soup drill-down and testing
- Natalie Sinner helped with soup.find_parent code
- RealPython help:
https://realpython.com/beautiful-soup-web-scraper-python/#find-elements-by-html-class-name
- bs4 docs:
https://www.crummy.com/software/BeautifulSoup/bs4/doc/#find-parents-and-find-parent
- .gitignore content courtesy of https://www.toptal.com/developers/gitignore/api/python
