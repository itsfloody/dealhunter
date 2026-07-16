import asyncio

from dealhunter.utils.logging import setup_logging

from dealhunter.engine import DealHunter
from dealhunter.scrapers.demo import DemoScraper


async def main():

    setup_logging()

    engine = DealHunter(
        scrapers=[
            DemoScraper(),
        ]
    )

    await engine.run()


if __name__ == "__main__":
    asyncio.run(main())
