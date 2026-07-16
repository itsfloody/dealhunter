from datetime import datetime
from pydantic import BaseModel, Field


class Product(BaseModel):
    store: str
    brand: str
    name: str
    flavour: str | None = None

    weight_kg: float = Field(gt=0)

    price: float = Field(gt=0)
    shipping: float = Field(default=0)

    protein_percent: float | None = None

    ingredients: list[str] = []

    url: str

    scraped_at: datetime = Field(default_factory=datetime.utcnow)

    @property
    def total_cost(self) -> float:
        return self.price + self.shipping

    @property
    def price_per_kg(self) -> float:
        return self.total_cost / self.weight_kg
