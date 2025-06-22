from flask import Flask, jsonify
from agents.scraper import EcommerceScraper

app = Flask(__name__)

@app.route('/products')
def get_products():
    scraper = EcommerceScraper()
    products = scraper.extract_products('https://www.extra.com.br/tv/b')
    return jsonify(products)

if __name__ == '__main__':
    app.run(debug=True)
