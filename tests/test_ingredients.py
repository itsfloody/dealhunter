from dealhunter.filters.ingredients import (
    contains_banned_ingredient,
)


def test_detects_stevia():

    ingredients = [
        "Whey protein concentrate",
        "Cocoa",
        "Stevia extract",
    ]

    assert contains_banned_ingredient(
        ingredients
    )


def test_allows_normal_product():

    ingredients = [
        "Whey protein concentrate",
        "Cocoa",
        "Sucralose",
    ]

    assert not contains_banned_ingredient(
        ingredients
    )
