def calculate_cost(tokens: int, price_per_1k: float) -> float:
    """
    Calculate cost based on token usage.
    """
    return (tokens / 1000) * price_per_1k