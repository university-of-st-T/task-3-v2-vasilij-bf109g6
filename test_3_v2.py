def calculate_total(prices, *discounts, **options):

    total = sum(prices)

    for discount in discounts:
        total *= (1 - discount / 100)

    tax = options.get("tax", 0)
    total *= (1 + tax / 100)

    round_to = options.get("round_to", 2)
    if round_to is not None:
        total = round(total, round_to)

    return total

prices = [100, 150, 300]
return total = calculate_total(prices, 10, 5, tax=20, round_to=1)

