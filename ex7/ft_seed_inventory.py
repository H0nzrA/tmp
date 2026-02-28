def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:

    tails = ""
    if unit == "packets":
        tails = f"{quantity} packets available"
    elif unit == "grams":
        tails = f"{quantity} grams total"
    elif unit == "area":
        tails = f"covers {quantity} square meters"
    else:
        print("Unknown unit type")
        return
    print(f"{seed_type.capitalize()}: {tails}")
