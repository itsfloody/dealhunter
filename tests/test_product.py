from dealhunter.models.product import Product


def test_price_per_kg():
    product = Product(
        store="NZ Protein",
        brand="Rule 1",
        name="R1 Whey",
        weight_kg=2,
        price=120,
        url="https://example.com",
    )

    assert product.price_per_kg == 60
