def simulate_purchase(price: float, category: str | None, ats: float) -> tuple[str, list[str]]:
    after = ats - price
    if after >= 0:
        return (f"OK — still on plan. ATS after purchase: ${after:.2f}", [])
    suggestions = [f"Reduce {category or 'another category'} by ${abs(after):.2f}", "Delay purchase or split over two periods"]
    return (f"Off plan by ${abs(after):.2f}", suggestions)
