from dealhunter.database.models import ProductRecord
from dealhunter.database.session import SessionLocal
from dealhunter.models.product import Product
from sqlalchemy import func

def save_products(
    products: list[Product],
) -> None:

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

def get_average_price_per_kg(
    product_name: str,
) -> float | None:

    with SessionLocal() as session:

        result = session.query(
            func.avg(
                ProductRecord.price_per_kg
            )
        ).filter(
            ProductRecord.name == product_name
        ).scalar()

        return result

def get_lowest_price_per_kg(
    product_name: str,
) -> float | None:

    with SessionLocal() as session:

        result = session.query(
            func.min(
                ProductRecord.price_per_kg
            )
        ).filter(
            ProductRecord.name == product_name
        ).scalar()

        return result


