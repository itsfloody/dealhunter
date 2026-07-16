import asyncio

from dealhunter.engine import DealHunter
from dealhunter.scrapers.demo import DemoScraper


async def main():
    engine = DealHunter(
        scrapers=[
            DemoScraper(),
        ]
    )

    await engine.run()


if __name__ == "__main__":
    asyncio.run(main())
