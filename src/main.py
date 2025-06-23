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
    
    # Add your main logic here
def save_products(firebase_client, products):
    for product in products:
        firebase_client.save_product(product)
           
if __name__ == "__main__":
    main()
