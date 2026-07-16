from dealhunter.database.repository import (
    get_average_price_per_kg,
    get_lowest_price_per_kg,
)


def test_price_history():

    average = get_average_price_per_kg(
        "R1 Whey"
    )

    lowest = get_lowest_price_per_kg(
        "R1 Whey"
    )

    assert average is not None
    assert lowest is not None
