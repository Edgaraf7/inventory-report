from inventory_report.reports.simple_report import SimpleReport


class CompleteReport(SimpleReport):
    def generate(self) -> str:
        simple_report = super().generate()
        company_inventory = self._get_company_inventory()

        complete_report = (f"{simple_report}\nStocked products by company:\n")
        for company, count in company_inventory.items():
            complete_report += f"- {company}: {count}\n"

        return complete_report

    def _get_company_inventory(self) -> dict:
        company_inventory = {}
        for inventory in self.inventories:
            for product in inventory.data:
                company = product.company_name
                if company in company_inventory:
                    company_inventory[company] += 1
                else:
                    company_inventory[company] = 1
        return company_inventory
