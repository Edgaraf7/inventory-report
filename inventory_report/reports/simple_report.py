from datetime import datetime
from inventory_report.inventory import Inventory
from inventory_report.product import Product
from typing import List

class SimpleReport:
    def __init__(self):
        self.inventories: List[Inventory] = []

    def add_inventory(self, inventory: Inventory):
        self.inventories.append(inventory)

    def generate(self) -> str:
        oldest_manufacturing_date = None
        closest_expiration_date = None
        largest_inventory_company = None
        largest_inventory_count = 0

        for inventory in self.inventories:
            for product in inventory.data:
                # Encontra a data de fabricação mais antiga
                if oldest_manufacturing_date is None or product.manufacturing_date < oldest_manufacturing_date:
                    oldest_manufacturing_date = product.manufacturing_date
                
                # Encontra a data de validade mais próxima (não vencida)
                if product.expiration_date > datetime.now().strftime("%Y-%m-%d"):
                    if closest_expiration_date is None or product.expiration_date < closest_expiration_date:
                        closest_expiration_date = product.expiration_date
                
                # Calcula a empresa com o maior estoque
                if inventory.data.count(product) > largest_inventory_count:
                    largest_inventory_company = product.company_name
                    largest_inventory_count = inventory.data.count(product)
        
        report = f"Oldest manufacturing date: {oldest_manufacturing_date}\n"
        report += f"Closest expiration date: {closest_expiration_date}\n"
        report += f"Company with the largest inventory: {largest_inventory_company}"

        return report
