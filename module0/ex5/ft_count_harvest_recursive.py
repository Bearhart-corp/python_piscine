def recur(quantity):
    if quantity > 1 :
        recur(quantity - 1)
    print(f"Day {quantity}")
    

def ft_count_harvest_recursive() -> None:
    quantity = 5
    print(f"Days until harvest: {quantity}")
    recur(quantity)
    print("Harvest time!")