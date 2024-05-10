from typing import List
from inventory_report.importers import CsvImporter, JsonImporter
from inventory_report.inventory import Inventory
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


def _import_inventory(file_path: str) -> Inventory:

    if file_path.endswith('.json'):
        importer = JsonImporter(file_path)
    elif file_path.endswith('.csv'):
        importer = CsvImporter(file_path)
    else:
        return None

    return Inventory(importer.import_data())


def _get_inventories(file_paths: List[str]) -> List[Inventory]:
    inventories = []
    for file_path in file_paths:
        inventory = _import_inventory(file_path)
        if inventory:
            inventories.append(inventory)
    return inventories


def process_report_request(file_paths: List[str], report_type: str) -> str:
    inventories = _get_inventories(file_paths)
    if not inventories:
        return "No valid files found to generate report."
    if report_type == "simple":
        report = SimpleReport()
    elif report_type == "complete":
        report = CompleteReport()
    else:
        raise ValueError("Report type is invalid.")
    for inventory in inventories:
        report.add_inventory(inventory)

    return report.generate()
