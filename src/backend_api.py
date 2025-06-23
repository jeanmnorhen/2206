import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from flask import Flask, request, jsonify
from flask_cors import CORS
from src.agents.scraper import EcommerceScraper
from datetime import datetime

app = Flask(__name__)
CORS(app)

scraper = EcommerceScraper()

@app.route('/scrape', methods=['GET', 'POST'])
def scrape_offers():
    if request.method == 'GET':
        term = request.args.get('term')
        # Exemplo: montar uma URL de busca a partir do termo
        # Aqui você pode definir um template de URL de e-commerce para busca
        if not term:
            return jsonify({'error': 'Missing term parameter'}), 400
        # Exemplo de URL de busca (ajuste conforme necessário)
        search_url = f"https://www.google.com/search?q={term}"
        result = scraper.extract_product_data(search_url)
        offers = []
        if result:
            offers.append({
                'name': result['data'].get('name', ''),
                'price': result['data'].get('price', None),
                'store': result['data'].get('store', ''),
                'url': search_url,
                'date': datetime.utcnow().strftime('%Y-%m-%d')
            })
        return jsonify(offers)
    else:
        data = request.get_json()
        product_id = data.get('productId')
        product_url = data.get('productUrl')
        # URLs de exemplo ou lógica para buscar URLs a partir do productId
        urls = data.get('urls', [])
        if product_url:
            urls.append(product_url)
        offers = []
        for url in urls:
            result = scraper.extract_product_data(url)
            if result:
                offers.append({
                    'name': result['data'].get('name', ''),
                    'price': result['data'].get('price', None),
                    'store': result['data'].get('store', ''),
                    'url': url,
                    'date': datetime.utcnow().strftime('%Y-%m-%d')
                })
        return jsonify({'offers': offers})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
