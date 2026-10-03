def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    if unit == "packets":
        print(
            f"{seed_type.capitalize()} seeds: {quantity} packets available"
        )
    elif unit == "grams":
        print(
            f"{seed_type.capitalize()} seeds: {quantity} grams total"
        )
    elif unit == "area":
        print(
            f"{seed_type.capitalize()} seeds: covers {quantity} square meters"
        )
    else:
        print("Unknown unit type")

# if __name__ == "__main__":
#    ft_seed_inventory("tomato", 45, "packets")
#    ft_seed_inventory("verza", 43, "seeds")
