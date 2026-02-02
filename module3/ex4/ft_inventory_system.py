import sys

class NumberArgError(Exception):
    def __init__(self):
        super().__init__("No args provided.")

def main():
    len_arg = len(sys.argv)
    try:
        if len_arg == 1:
            raise NumberArgError
    except NumberArgError as e:
        print(f"{e}")
        return
    inventory = {}
    tot_item = 0
    for arg in sys.argv[1:]:
        key, value = arg.split(':')
        inventory.update({key: int(value) if value else 0})
        tot_item += inventory.get(key)
    print("\n=== Inventory System Analysis ===\n")
    print(f"Total items in inventory: {tot_item}")
    print(f"Unique item types: {len(inventory)}")
    print("\n=== Current Inventory ===\n")
    for k, v in inventory.items():
        print(f"{k}: {v} units ({100 / (tot_item / v):.1f}%)")
    print("\n=== Inventory Statistics ===")
    big_key = max(inventory,  key=inventory.get)
    big_value = max(inventory.values())
    small_key = min(inventory,  key=inventory.get)
    small_value = min(inventory.values())
    print(f"Most abundant: {big_key}({big_value} units)")
    print(f"Least abundant: {small_key}({small_value} units)")

    print("\n=== Item Categories ===")
    print("?????\n")

    print("\n=== Management Suggestions ===")
    restock = [k for k in inventory if inventory[k] < 2]
    print(f"Restock needed: {restock}")
    print("\n=== Dictionary Properties Demo ===")
    print(f"Dictionary keys: {inventory.keys()}")
    print(f"Dictionary values: {inventory.values()}")
    print(f"Sample lookup - 'sword' in inventory :" , 'sword' in inventory)

if __name__ == "__main__":
    main()
