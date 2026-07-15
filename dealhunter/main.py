import asyncio

from dealhunter.filters.ingredients import (
    contains_banned_ingredient,
)
from dealhunter.scrapers.demo import DemoScraper


async def main():

    scraper = DemoScraper()

    products = await scraper.scrape()

    for product in products:

        if contains_banned_ingredient(
            product.ingredients
        ):
            print(
                f"❌ {product.name} rejected "
                "because it contains a banned ingredient"
            )
            continue

        print(product)
        print(
            f"Price/kg: ${product.price_per_kg:.2f}"
        )


if __name__ == "__main__":
    asyncio.run(main())
