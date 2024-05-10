from abc import ABC, abstractmethod
from typing import List, Dict, Type


class Importer(ABC):
    def __init__(self, path: str):
        self.path = path

    @abstractmethod
    def import_data(self) -> List[dict]:
        pass


class JsonImporter(Importer):
    def import_data(self) -> List[dict]:
        # Implementação específica para importar dados de arquivos JSON
        pass


class CsvImporter(Importer):
    def import_data(self) -> List[dict]:
        # Implementação específica para importar dados de arquivos CSV
        pass


# Não altere a variável abaixo

IMPORTERS: Dict[str, Type[Importer]] = {
    "json": JsonImporter,
    "csv": CsvImporter,
}
