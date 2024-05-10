from inventory_report.inventory import Inventory
from datetime import datetime


class SimpleReport:
    def __init__(self):
        self.inventories = []

    def add_inventory(self, inventory: Inventory) -> None:
        self.inventories.append(inventory)

    def generate(self) -> str:
        try:
            if not self.inventories:
                return "No data available."

            oldest_date = self._get_oldest_manufacturing_date()
            closest_expiration = self._get_closest_expiration_date()
            largest_company = self._get_company_with_largest_inventory()

            report = (
                f"Oldest manufacturing date: {oldest_date}\n"
                f"Closest expiration date: {closest_expiration}\n"
                f"Company with the largest inventory: {largest_company}"
            )
            return report
        except ValueError:
            return "An error occurred while generating the report."

    def _get_oldest_manufacturing_date(self) -> datetime:
        try:
            return min(
                product.manufacturing_date
                for inventory in self.inventories
                for product in inventory.data
            )
        except ValueError:
            return "No products available"

    def _get_closest_expiration_date(self) -> str:
        now_date = datetime.now().date()
        valid_products = [
            product
            for inventory in self.inventories
            for product in inventory.data
            if datetime.strptime(product.expiration_date, '%Y-%m-%d').date()
            > now_date
        ]
        if valid_products:
            try:
                return min(
                    product.expiration_date for product in valid_products)
            except ValueError:
                return "Tried to find minimum of empty list"

    def _get_company_with_largest_inventory(self) -> str:
        company_inventory_counts = {}
        for inventory in self.inventories:
            for product in inventory.data:
                company = product.company_name
                company_inventory_counts[
                    company] = company_inventory_counts.get(company, 0) + 1

        try:
            return max(
                company_inventory_counts,
                key=company_inventory_counts.get
            )
        except ValueError:
            return "No company available"
