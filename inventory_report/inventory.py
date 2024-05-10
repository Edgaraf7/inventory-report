from typing import List
from inventory_report.product import Product

class Inventory:
    def __init__(self, data: List[Product] = None):
        self._data = [] if data is None else data

    @property
    def data(self) -> List[Product]:
        return self._data.copy()

    def add_data(self, products: List[Product]):
        self._data.extend(products)
