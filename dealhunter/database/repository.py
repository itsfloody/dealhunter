from dealhunter.database.models import ProductRecord
from dealhunter.database.session import SessionLocal
from dealhunter.models.product import Product


def save_products(products: list[Product]):

    with SessionLocal() as session:

        for product in products:

            record = ProductRecord(
                store=product.store,
                brand=product.brand,
                name=product.name,
                weight_kg=product.weight_kg,
                price=product.price,
                price_per_kg=product.price_per_kg,
                scraped_at=product.scraped_at,
            )

            session.add(record)

        session.commit()
