"""
Módulo de Carrito de Compras
Gestión de items, cantidades, totales
"""

class ShoppingCart:
    """Carrito de compras"""
    
    def __init__(self, user_id):
        self.user_id = user_id
        self.items = {}
    
    def add_item(self, product_id, quantity=1, price=0):
        """Agrega item al carrito"""
        if quantity <= 0:
            raise ValueError("Cantidad debe ser positiva")
        
        if price < 0:
            raise ValueError("Precio no puede ser negativo")
        
        if product_id in self.items:
            self.items[product_id]['quantity'] += quantity
        else:
            self.items[product_id] = {
                'quantity': quantity,
                'price': price
            }
        
        return True
    
    def remove_item(self, product_id):
        """Elimina item del carrito"""
        if product_id not in self.items:
            raise ValueError("Item no existe en carrito")
        
        del self.items[product_id]
        return True
    
    def update_quantity(self, product_id, quantity):
        """Actualiza cantidad de item"""
        if product_id not in self.items:
            raise ValueError("Item no existe")
        
        if quantity <= 0:
            return self.remove_item(product_id)
        
        self.items[product_id]['quantity'] = quantity
        return True
    
    def get_total(self):
        """Calcula total del carrito"""
        total = 0
        for item in self.items.values():
            total += item['quantity'] * item['price']
        return total
    
    def clear(self):
        """Vacía el carrito"""
        self.items = {}
        return True
    
    def get_item_count(self):
        """Cuenta total de items"""
        return sum(item['quantity'] for item in self.items.values())
