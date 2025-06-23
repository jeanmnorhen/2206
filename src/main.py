import os
from dotenv import load_dotenv
from src.agents.scraper import EcommerceScraper
from src.database.firebase_client import FirebaseClient
from src.warehouse.etl import ETLProcessor
from src.warehouse.dashboard import Dashboard

def main():
    load_dotenv()
    
    # Initialize components
    firebase_client = FirebaseClient()
    scraper = EcommerceScraper()
    etl = ETLProcessor()
    dashboard = Dashboard()

    term = os.getenv("TERM")  # Replace this with the actual term you want to use for scraping
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36'}
    scraper = EcommerceScraper(term)
    firebase_client = FirebaseClient()

    products = scraper.extract_products(headers)  # Calling the newly implemented function to extract products

    # Add your main logic here
def save_products(firebase_client, products):
    for product in products:
        firebase_client.save_product(product)
           
if __name__ == "__main__":
    main()
