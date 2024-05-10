import pytest
from inventory_report.product import Product


def test_product_report():
    product_data = {
        "id": "1",
        "product_name": "farinha",
        "company_name": "Farinini",
        "manufacturing_date": "01-05-2021",
        "expiration_date": "02-06-2023",
        "serial_number": "TY68 409C JJ43 ASD1 PL2F",
        "storage_instructions":
        "precisa ser armazenado em local protegido da luz",
    }

    product = Product(**product_data)

    # Test Trecho 1
    assert f"The product {product.id} - farinha" in str(product)

    # Test Trecho 2
    assert "with serial number TY68 409C JJ43 ASD1 PL2F" in str(product)

    # Test Trecho 3
    assert "manufactured on 01-05-2021" in str(product)

    # Test Trecho 4
    assert "by the company Farinini" in str(product)

    # Test Trecho 5
    assert "valid until 02-06-2023" in str(product)

    # Test Trecho 6
    assert "must be stored accordingto the following instructions: precisa ser armazenado em local protegido da luz" in str(product)


if __name__ == "__main__":
    pytest.main()
