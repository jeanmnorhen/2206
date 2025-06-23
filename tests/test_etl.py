import pytest
from src.warehouse.etl import ETLProcessor
import pandas as pd

def test_transform_data():
    etl = ETLProcessor()
    df = pd.DataFrame([{'name': 'Produto', 'price': 100}])
    result = etl.transform_data(df)
    assert not result.empty
    assert 'name' in result.columns
