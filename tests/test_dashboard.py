import pytest
from src.warehouse.dashboard import Dashboard

def test_dashboard_init():
    dash = Dashboard()
    assert dash is not None
