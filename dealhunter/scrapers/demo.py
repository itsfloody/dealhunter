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
                shipping=0,
                protein_percent=80,
                ingredients=[
                    "Whey protein concentrate",
                    "Cocoa",
                    "Sucralose",
                ],
                url="https://example.com",
            )
        ]
