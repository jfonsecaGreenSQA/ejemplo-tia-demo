"""
Módulo de Búsqueda
Motor de búsqueda de productos
"""

class SearchEngine:
    """Motor de búsqueda"""
    
    def __init__(self):
        self.products = []
        self.index = {}
    
    def index_product(self, product_id, name, description, category, price):
        """Indexa un producto para búsqueda"""
        product = {
            'id': product_id,
            'name': name,
            'description': description,
            'category': category,
            'price': price
        }
        
        self.products.append(product)
        
        # Indexar palabras
        words = (name + ' ' + description).lower().split()
        for word in words:
            if word not in self.index:
                self.index[word] = []
            self.index[word].append(product_id)
        
        return True
    
    def search(self, query):
        """Busca productos por query"""
        if not query:
            return []
        
        words = query.lower().split()
        product_ids = set()
        
        for word in words:
            if word in self.index:
                product_ids.update(self.index[word])
        
        results = [p for p in self.products if p['id'] in product_ids]
        return results
    
    def search_by_category(self, category):
        """Busca por categoría"""
        return [p for p in self.products if p['category'] == category]
    
    def search_by_price_range(self, min_price, max_price):
        """Busca por rango de precio"""
        return [p for p in self.products 
                if min_price <= p['price'] <= max_price]
    
    def get_suggestions(self, partial_query):
        """Obtiene sugerencias de búsqueda"""
        if not partial_query:
            return []
        
        partial = partial_query.lower()
        suggestions = set()
        
        for word in self.index.keys():
            if word.startswith(partial):
                suggestions.add(word)
        
        return sorted(list(suggestions))[:5]
