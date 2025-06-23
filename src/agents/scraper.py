from langchain_community.llms import Ollama
from bs4 import BeautifulSoup
import requests

class EcommerceScraper:
    def __init__(self):
        self.llm = Ollama(model="deepseek-coder:instruct", base_url="http://192.168.0.56:11434")
        
    def extract_product_data(self, url):
        try:
            print(f"Baixando página: {url}")
            headers = {'User-Agent': 'Mozilla/5.0'}
            response = requests.get(url, headers=headers, timeout=10)
            response.raise_for_status()
            print("Página baixada, processando com BeautifulSoup...")
            soup = BeautifulSoup(response.text, 'html.parser')
            # Aqui, extraia apenas os cards de produto relevantes
            produtos = []
            for card in soup.select('div[data-testid="product-card-desktop"]'):
                nome = card.select_one('h3.product-card__title span[aria-hidden="true"]')
                preco = card.select_one('div.product-card__highlight-price[aria-hidden="true"]')
                img = card.select_one('img.product-card__image')
                link = card.select_one('h3.product-card__title a')
                produtos.append({
                    "name": nome.text.strip() if nome else None,
                    "price": preco.text.strip() if preco else None,
                    "imageUrl": img['src'] if img else None,
                    "productLink": link['href'] if link else None,
                    "sourceUrl": url
                })
            print(f"Produtos extraídos: {len(produtos)}")
            return produtos
        except Exception as e:
            print(f"Erro no scraping: {e}")
            return []
            
    def search_ecommerce_sites(self, country_code):
        """Find and analyze e-commerce sites for a given country"""
        # Add your search logic here
        pass
