def test_create_product() -> None:
    raise NotImplementedError
from inventory_report.product import Product

def test_create_product() -> None:
    product_data = {
        "id": "1",
        "product_name": "Borracha",
        "company_name": "Papelaria Solar",
        "manufacturing_date": "2021-07-04",
        "expiration_date": "2029-02-09",
        "serial_number": "FR48",
        "storage_instructions": "Ao abrigo de luz solar"
    }

    product = Product(**product_data)

    assert product.id == product_data["id"]
    assert product.company_name == product_data["company_name"]
    assert product.product_name == product_data["product_name"]
    assert product.manufacturing_date == product_data["manufacturing_date"]
    assert product.expiration_date == product_data["expiration_date"]
    assert product.serial_number == product_data["serial_number"]
    assert product.storage_instructions == product_data["storage_instructions"]

    # Teste adicional para garantir que todos os atributos estão presentes
    assert hasattr(product, 'id')
    assert hasattr(product, 'company_name')
    assert hasattr(product, 'product_name')
    assert hasattr(product, 'manufacturing_date')
    assert hasattr(product, 'expiration_date')
    assert hasattr(product, 'serial_number')
    assert hasattr(product, 'storage_instructions')
