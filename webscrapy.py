import requests
from bs4 import BeautifulSoup
import json

headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) ",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8"}
url = 'https://books.toscrape.com/catalogue/'

#converting the soup into ints bc I don't want to do it later
num_conv = {'One': 1, 'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5}

books = {}
for page in range(1,51):
    soup = BeautifulSoup(requests.get(url + 'page-' + str(page) + '.html', headers= headers).content, 'html5lib')
    for link in soup.find_all('a'):
        if link.get('title') != None:
            #scrapes the books off of the page
            title = link.get('title')
            href = link.get('href')
            #gets individual book info
            subsoup = BeautifulSoup(requests.get(url + href).content, 'html5lib')
            if subsoup.find('p', 'price_color') != None:
                price = subsoup.find('p', 'price_color').contents[0]
            else:
                price = None
            if subsoup.find('p', 'instock availability') != None:
                available = subsoup.find('p', 'instock availability').contents[2].strip().split('(')[0].lower().strip()
            else:
                available = None
            if subsoup.find('p', 'instock availability') != None:
                stock = subsoup.find('p', 'instock availability').contents[2].strip().split('(')[1].split(' ')[0] 
            else:
                stock = None
            if subsoup.find('p','star-rating') != None:
                stars = num_conv[subsoup.find('p','star-rating').attrs['class'][1]]
            else:
                stars = None 
            if subsoup.find('div', id='product_description') != None:
                description = subsoup.find('div', id='product_description').next_sibling.next_sibling.contents[0] 
            else:
                description = None
            if subsoup.find('li') != None:
                category = subsoup.find('li').next_sibling.next_sibling.next_sibling.next_sibling.find('a').contents[0].lower()
            else: 
                category = None
            if subsoup.find('td') != None:
                upc = subsoup.find('td').contents[0] 
            else:
                upc = None
            #store in dictionary
            books[title] = {'upc': upc, 'category': category, 'stars': stars, 'price': price, 'availability': available, 'stock': stock, 'href': href, 'description': description}
    #just a visual indicator of progress for my impatient ass
    print('-')

#store into a json file!
json = json.dumps(books)
f = open('books.json', 'w')
f.write(json)
f.close()
            
