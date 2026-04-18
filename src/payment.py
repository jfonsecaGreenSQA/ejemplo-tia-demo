"""
Módulo de Pagos
Procesamiento de transacciones y métodos de pago
"""

class PaymentProcessor:
    """Procesador principal de pagos"""
    
    def __init__(self):
        self.supported_methods = ['credit_card', 'debit_card', 'paypal', 'crypto']
    
    def process_payment(self, amount, method, card_number=None):
        """Procesa un pago"""
        if method not in self.supported_methods:
            raise ValueError(f"Método {method} no soportado")
        
        if amount <= 0:
            raise ValueError("Monto debe ser positivo")
        
        if method in ['credit_card', 'debit_card']:
            if not card_number or len(card_number) != 16:
                raise ValueError("Número de tarjeta inválido")
        
        # Simular procesamiento
        transaction_id = f"TXN-{amount}-{method[:4].upper()}"
        return {
            'status': 'success',
            'transaction_id': transaction_id,
            'amount': amount,
            'method': method
        }
    
    def calculate_discount(self, amount, discount_code=None):
        """Calcula descuento aplicable"""
        discounts = {
            'SAVE10': 0.10,
            'SAVE20': 0.20,
            'VIP': 0.25
        }
        
        if discount_code and discount_code in discounts:
            discount = amount * discounts[discount_code]
            return amount - discount
        
        return amount
    
    def refund_payment(self, transaction_id):
        """Procesa reembolso"""
        if not transaction_id or not transaction_id.startswith('TXN-'):
            raise ValueError("Transaction ID inválido")
        
        return {
            'status': 'refunded',
            'transaction_id': transaction_id
        }
