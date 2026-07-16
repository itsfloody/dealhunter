from dealhunter.models.product import Product
from dealhunter.scrapers.base import BaseScraper


class DemoScraper(BaseScraper):
    name = "Demo Store"

    async def scrape(self) -> list[Product]:
        return [
            Product(
                store="Demo Store",
                brand="Rule 1",
                name="R1 Whey",
                flavour="Chocolate",
                weight_kg=2.27,
                price=119.99,
                protein_percent=80,
                ingredients=[
                    "Whey protein concentrate",
                    "Cocoa",
                    "Sucralose",
                ],
                url="https://example.com/r1",
            ),
            Product(
                store="Demo Store",
                brand="Budget Whey",
                name="Budget Whey",
                flavour="Vanilla",
                weight_kg=2,
                price=90,
                protein_percent=70,
                ingredients=[
                    "Whey protein concentrate",
                ],
                url="https://example.com/budget",
            ),
            Product(
                store="Demo Store",
                brand="Premium Whey",
                name="Premium Whey",
                flavour="Chocolate",
                weight_kg=2,
                price=130,
                protein_percent=85,
                ingredients=[
                    "Whey isolate",
                ],
                url="https://example.com/premium",
            ),
        ]
