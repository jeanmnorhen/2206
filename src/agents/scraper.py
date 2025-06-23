import asyncio
from crawl4ai import AsyncWebCrawler
import json
from urllib.parse import urljoin, parse_qs
import os
from dotenv import load_dotenv

class EcommerceScraper:
    def __init__(self, term):
        self.term = term
        self.base_url = "https://www.extra.com.br"

    async def extract_products(self, headers={}):
        url = f"{self.base_url}/{self.term}/b"
        async with AsyncWebCrawler() as crawler:
            response = await crawler.arun(url=url, headers=headers)
            html = response.html
            products = self.extract_product_list(html)
            return products

    def extract_product_list(self, html):
        product_list = []
        product_container = html('#js-products .product-item')
        for item in product_container:
            product_data = self.extract_product(item)
            if product_data:
                product_list.append(product_data)
        return product_list

    def extract_product(self, item):
        name = item.select_one('.product-item__title a').text
        price = item.select_one('.product-item__price span').text
        image_url = urljoin(self.base_url, item.select_one('.product-item__image img')['src'])
        source_url = self.base_url + item.select_one('.product-item__link')['href']

        product_data = {
            "name": name,
            "price": price.strip("R$ "),
            "categories": ["Electronics"],  # You can modify this to match the actual category of products
            "brand": "Extra",
            "imageUrl": image_url,
            "sourceUrl": source_url
        }
        return product_data