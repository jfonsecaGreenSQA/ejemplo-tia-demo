"""Tests para módulo search.py - SIMPLIFICADOS"""
import pytest
from src.search import SearchEngine

# 5 tests representativos
def test_index_product():
    search = SearchEngine()
    result = search.index_product('p1', 'Laptop', 'Gaming laptop', 'Electronics', 1000)
    assert result == True

def test_search_by_keyword():
    search = SearchEngine()
    search.index_product('p1', 'Laptop', 'Gaming laptop', 'Electronics', 1000)
    results = search.search('laptop')
    assert len(results) == 1

def test_search_by_category():
    search = SearchEngine()
    search.index_product('p1', 'Laptop', 'Gaming laptop', 'Electronics', 1000)
    results = search.search_by_category('Electronics')
    assert len(results) == 1

def test_search_by_price_range():
    search = SearchEngine()
    search.index_product('p1', 'Laptop', 'Gaming laptop', 'Electronics', 1000)
    results = search.search_by_price_range(500, 1500)
    assert len(results) == 1

def test_get_suggestions():
    search = SearchEngine()
    search.index_product('p1', 'Laptop', 'Gaming laptop', 'Electronics', 1000)
    suggestions = search.get_suggestions('lap')
    assert 'laptop' in suggestions
