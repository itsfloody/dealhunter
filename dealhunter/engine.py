from __future__ import annotations

import asyncio

from dealhunter.filters.ingredients import contains_banned_ingredient
from dealhunter.ranking.scorer import DealScore, calculate_deal_score
from dealhunter.scrapers.base import BaseScraper
from dealhunter.utils.logging import logger

class DealHunter:
    def __init__(self, scrapers: list[BaseScraper]):
        self.scrapers = scrapers

    async def run(self) -> list[DealScore]:
        products = await self._scrape_products()
        products = self._filter_products(products)
        deals = self._rank_products(products)

        self._display(deals)

        return deals

    async def _scrape_products(self):
        tasks = [
            scraper.scrape()
            for scraper in self.scrapers
        ]

        results = await asyncio.gather(
            *tasks,
            return_exceptions=True,
        )

        products = []

        for scraper, result in zip(
            self.scrapers,
            results,
        ):
            if isinstance(result, Exception):
                logger.error(
                    "%s failed: %s",
                    scraper.name,
                    result,
                )
                continue

            logger.info(
                "%s returned %s products",
                scraper.name,
                len(result),
            )

            products.extend(result)

        return products

    def _filter_products(self, products):
        accepted = []

        for product in products:
            if contains_banned_ingredient(
                product.ingredients
            ):
                print(
                    f"Rejected {product.name} "
                    "(banned ingredient)"
                )
                continue

            accepted.append(product)

        return accepted

    def _rank_products(self, products):
        deals = [
            calculate_deal_score(product)
            for product in products
        ]

        deals.sort(
            key=lambda deal: deal.score,
            reverse=True,
        )

        return deals

    def _display(self, deals: list[DealScore]) -> None:
        print("\n🏆 Best Deals\n")

        for deal in deals:
            print(
                f"{deal.product.brand} - "
                f"{deal.product.name}"
            )
            print(
                f"Store: {deal.product.store}"
            )
            print(
                f"Price/kg: ${deal.price_per_kg}"
            )
            print(
                f"Protein-adjusted: "
                f"${deal.protein_cost_per_kg}/kg"
            )
            print(
                f"Score: {deal.score}"
            )
            print("-" * 40)
