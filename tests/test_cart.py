"""Tests para módulo cart.py - SIMPLIFICADOS"""
import pytest
from src.cart import ShoppingCart

# 5 tests representativos
def test_add_item():
    cart = ShoppingCart('user123')
    result = cart.add_item('product1', 2, 50.0)
    assert result == True

def test_remove_item():
    cart = ShoppingCart('user123')
    cart.add_item('product1', 2, 50.0)
    result = cart.remove_item('product1')
    assert result == True

def test_get_total():
    cart = ShoppingCart('user123')
    cart.add_item('product1', 2, 50.0)
    cart.add_item('product2', 1, 30.0)
    assert cart.get_total() == 130.0

def test_update_quantity():
    cart = ShoppingCart('user123')
    cart.add_item('product1', 2, 50.0)
    cart.update_quantity('product1', 5)
    assert cart.items['product1']['quantity'] == 5

def test_clear_cart():
    cart = ShoppingCart('user123')
    cart.add_item('product1', 2, 50.0)
    cart.clear()
    assert len(cart.items) == 0
