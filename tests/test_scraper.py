import pytest
from src.agents.scraper import EcommerceScraper

def test_extract_product_data(monkeypatch):
    # Mock requests.get and Ollama LLM for isolated test
    class MockResponse:
        text = '<html><body><h1>Produto Teste</h1></body></html>'
    
    def mock_get(url):
        return MockResponse()
    
    class MockLLM:
        def __call__(self, prompt):
            return '{"name": "Produto Teste", "price": "R$ 100,00"}'
    
    monkeypatch.setattr('requests.get', mock_get)
    scraper = EcommerceScraper()
    scraper.llm = MockLLM()
    result = scraper.extract_product_data('http://fakeurl.com')
    assert result is not None
    assert 'Produto Teste' in result['data']
