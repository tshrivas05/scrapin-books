# scrapin-books
playing around with BeautifulSoup and Pandas to derive some conclusions from books.toscrape.com

_____

books.toscrape.com is a web scraping sandbox that allows users to scrape books from their catalogue. despite the data being ficticious, this analysis is meant to demonstrate the different skills that can be performed and conclusions that can be drawn from the data provided. so, for this notebook, we will be treating books.toscrape's data as if it were an early Amazon's equivalent (online book retailer) and exploring what factors contribute to selling more books.

______

## files

### webscrapy.py
extracting book information from all 50 pages of books.toscrape.com using BeautifulSoup and storing them in a json file

### books.json
book data storage because why would I put myself through 404s again

### analysis.ipynb
extracting the information from the data - what factors of books affect their stockage and rating? are there any patterns in the books stocked by books.toscrape.com?
