"""Tests para módulo payment.py"""
import pytest
from src.payment import PaymentProcessor

def test_process_payment_credit_card():
    processor = PaymentProcessor()
    result = processor.process_payment(100, 'credit_card', '1234567890123456')
    assert result['status'] == 'success'
    assert result['amount'] == 100

def test_process_payment_paypal():
    processor = PaymentProcessor()
    result = processor.process_payment(50, 'paypal')
    assert result['status'] == 'success'

def test_invalid_payment_method():
    processor = PaymentProcessor()
    with pytest.raises(ValueError):
        processor.process_payment(100, 'bitcoin')

def test_negative_amount():
    processor = PaymentProcessor()
    with pytest.raises(ValueError):
        processor.process_payment(-50, 'credit_card', '1234567890123456')

def test_invalid_card_number():
    processor = PaymentProcessor()
    with pytest.raises(ValueError):
        processor.process_payment(100, 'credit_card', '123')

def test_calculate_discount_save10():
    processor = PaymentProcessor()
    result = processor.calculate_discount(100, 'SAVE10')
    assert result == 90

def test_calculate_discount_save20():
    processor = PaymentProcessor()
    result = processor.calculate_discount(100, 'SAVE20')
    assert result == 80

def test_calculate_discount_vip():
    processor = PaymentProcessor()
    result = processor.calculate_discount(100, 'VIP')
    assert result == 75

def test_no_discount():
    processor = PaymentProcessor()
    result = processor.calculate_discount(100)
    assert result == 100

def test_invalid_discount_code():
    processor = PaymentProcessor()
    result = processor.calculate_discount(100, 'INVALID')
    assert result == 100

def test_refund_payment():
    processor = PaymentProcessor()
    result = processor.refund_payment('TXN-100-CRED')
    assert result['status'] == 'refunded'

def test_invalid_transaction_id():
    processor = PaymentProcessor()
    with pytest.raises(ValueError):
        processor.refund_payment('INVALID-ID')

def test_process_payment_crypto():
    processor = PaymentProcessor()
    result = processor.process_payment(200, 'crypto')
    assert result['status'] == 'success'

def test_debit_card_payment():
    processor = PaymentProcessor()
    result = processor.process_payment(75, 'debit_card', '9876543210987654')
    assert result['status'] == 'success'

def test_zero_amount():
    processor = PaymentProcessor()
    with pytest.raises(ValueError):
        processor.process_payment(0, 'paypal')
