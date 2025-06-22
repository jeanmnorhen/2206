from crawl4ai import CrawlerHub
from bs4 import BeautifulSoup

class EcommerceScraper:
    def __init__(self):
        self.crawler = CrawlerHub()
        
    def extract_products(self, url):
        response = self.crawler.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        product_cards = soup.find_all('div', class_='product-card')
        
        products = []
        for card in product_cards:
            product = {
                'title': card.find('h3', class_='product-name').text.strip(),
                'price': card.find('div', class_='price').text.strip(),
                'link': card.find('a')['href']
            }
            products.append(product)
            
        return products
