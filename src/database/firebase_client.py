import firebase_admin
from firebase_admin import credentials, db
import os

REQUIRED_FIELDS = ["name", "price", "categories", "brand", "imageUrl", "sourceUrl", "status"]

def validate_product(product):
    for field in REQUIRED_FIELDS:
        if field not in product or product[field] in [None, "", []]:
            raise ValueError(f"Campo obrigatório ausente: {field}")
    if not isinstance(product["price"], (int, float)):
        raise ValueError("O campo 'price' deve ser numérico.")
    if not isinstance(product["categories"], list):
        raise ValueError("O campo 'categories' deve ser uma lista.")
    # Adicione outras validações conforme necessário
    return True

class FirebaseClient:
    def __init__(self):
        cred_path = os.getenv('FIREBASE_CREDENTIALS_PATH')
        if not firebase_admin._apps:
            cred = credentials.Certificate(cred_path)
            firebase_admin.initialize_app(cred, {
                'databaseURL': 'your-database-url'
            })
        self.db = db.reference()
    
    def save_product(self, product_data):
        """Save product data to Firebase (batch support) with validation"""
        products_ref = self.db.child('products')
        if isinstance(product_data, list):
            for prod in product_data:
                validate_product(prod)
            updates = {products_ref.push().key: data for data in product_data}
            products_ref.update(updates)
        else:
            validate_product(product_data)
            products_ref.push(product_data)
    
    def get_products(self, filters=None, limit=100):
        """Retrieve products with optional filters and pagination"""
        products_ref = self.db.child('products')
        query = products_ref
        if filters:
            for key, value in filters.items():
                query = query.order_by_child(key).equal_to(value)
        query = query.limit_to_first(limit)
        return query.get()
    
    def update_product(self, product_id, updates):
        """Update existing product data"""
        product_ref = self.db.child('products').child(product_id)
        product_ref.update(updates)
