from dataclasses import dataclass

from dealhunter.models.product import Product


@dataclass
class DealScore:
    product: Product
    price_per_kg: float
    protein_cost_per_kg: float
    score: float


def calculate_deal_score(product: Product) -> DealScore:
    """
    Calculate the value of a protein product.

    Lower protein cost = better deal.
    """

    price_per_kg = product.price_per_kg

    if product.protein_percent:
        protein_cost = price_per_kg / (product.protein_percent / 100)
    else:
        protein_cost = price_per_kg

    # Lower cost is better, convert to score
    score = 100 / protein_cost

    return DealScore(
        product=product,
        price_per_kg=round(price_per_kg, 2),
        protein_cost_per_kg=round(protein_cost, 2),
        score=round(score, 2),
    )
