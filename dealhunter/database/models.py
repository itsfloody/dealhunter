from datetime import datetime

from sqlalchemy import (
    DateTime,
    Float,
    Integer,
    String,
)

from sqlalchemy.orm import (
    DeclarativeBase,
    Mapped,
    mapped_column,
)


class Base(DeclarativeBase):
    pass


class ProductRecord(Base):

    __tablename__ = "products"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
    )

    store: Mapped[str] = mapped_column(
        String
    )

    brand: Mapped[str] = mapped_column(
        String
    )

    name: Mapped[str] = mapped_column(
        String
    )

    weight_kg: Mapped[float] = mapped_column(
        Float
    )

    price: Mapped[float] = mapped_column(
        Float
    )

    price_per_kg: Mapped[float] = mapped_column(
        Float
    )

    scraped_at: Mapped[datetime] = mapped_column(
        DateTime
    )
