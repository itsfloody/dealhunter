BANNED_INGREDIENTS = [
    "stevia",
    "steviol",
    "steviol glycosides",
    "rebaudioside",
    "reb a",
]


def contains_banned_ingredient(
    ingredients: list[str],
) -> bool:
    """
    Returns True if a product contains
    an ingredient we want to avoid.
    """

    combined = " ".join(
        ingredients
    ).lower()

    return any(
        banned in combined
        for banned in BANNED_INGREDIENTS
    )
