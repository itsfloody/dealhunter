from abc import ABC, abstractmethod

from dealhunter.models.product import Product


class BaseScraper(ABC):
    """
    Base class all retailer scrapers inherit from.
    """

    name: str = "Unknown"

    @abstractmethod
    async def scrape(self) -> list[Product]:
        """
        Return products found by this scraper.
        """
        pass
