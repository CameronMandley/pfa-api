def compute_available_to_spend(budget_lines: list[dict]) -> float:
    remaining = 0.0
    for bl in budget_lines:
        if bl.get("category") not in {"Rent","Debt","Savings"}:
            remaining += float(bl.get("planned", 0)) - float(bl.get("spent", 0))
    return round(remaining, 2)
