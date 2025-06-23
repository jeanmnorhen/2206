from langchain_community.llms import Ollama
from bs4 import BeautifulSoup
import requests
import time
import random

class EcommerceScraper:
    def __init__(self):
        self.llm = Ollama(model="deepseek-coder:instruct", base_url="http://192.168.0.56:11434")
        
    def extract_product_data(self, url):
        for attempt in range(3):
            try:
                print(f"Baixando página: {url} (tentativa {attempt+1})")
                headers = {
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
                    'Accept-Language': 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7',
                    'Accept-Encoding': 'gzip, deflate, br',
                    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                    'Referer': 'https://www.extra.com.br/',
                    'Connection': 'keep-alive',
                }
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
            except requests.exceptions.HTTPError as e:
                print(f"Erro HTTP: {e}")
                if response.status_code == 403 and attempt < 2:
                    print("403 Forbidden, tentando novamente após delay...")
                    time.sleep(random.uniform(2, 5))
                    continue
                else:
                    break
            except Exception as e:
                print(f"Erro no scraping: {e}")
                break
        return []
            
    def search_ecommerce_sites(self, country_code):
        """Find and analyze e-commerce sites for a given country"""
        # Add your search logic here
        pass
