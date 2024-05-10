from typing import List
from inventory_report.reports.simple_report import SimpleReport

class CompleteReport(SimpleReport):
    def generate(self) -> str:
        # Utiliza o método generate da classe SimpleReport para obter as informações básicas do relatório
        report = super().generate()

        # Calcula a quantidade de produtos estocados por empresa
        stocked_products_by_company = {}
        for inventory in self.inventories:
            for product in inventory.data:
                company = product.company_name
                if company in stocked_products_by_company:
                    stocked_products_by_company[company] += 1
                else:
                    stocked_products_by_company[company] = 1
        
        # Formata a lista de empresas e a quantidade de produtos estocados por empresa
        company_list = "\n".join([f"- {company}: {count}" for company, count in stocked_products_by_company.items()])

        # Adiciona as informações de produtos estocados por empresa ao relatório
        report += "\nStocked products by company:\n" + company_list

        return report
