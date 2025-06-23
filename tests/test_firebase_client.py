import pytest
from src.database.firebase_client import FirebaseClient

def test_save_product(monkeypatch):
    class MockDB:
        def child(self, name):
            return self
        def push(self, data):
            self.saved = data
            return True
    
    monkeypatch.setattr('src.database.firebase_client.db', MockDB())
    client = FirebaseClient()
    client.db = MockDB()
    product = {'name': 'Produto Teste', 'price': 100}
    client.save_product(product)
    assert hasattr(client.db, 'saved')
    assert client.db.saved['name'] == 'Produto Teste'
