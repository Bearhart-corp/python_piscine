class Plant:
    def __init__(self, name: str, height: int, age: int):
        self.name = name
        self.height = height
        self.age = age

    def display(self):
        print(f"Created: {self.name} ({self.height}cm, {self.age} days)")

def rand_maison(seed, even: int) -> int:
    i = even
    even = not (even & 1)
    seed = (((seed * 13 + i + 37 + even) ^ (0xa5 * even + i)) >> 1)
    seed = ((seed ^ 0x5555 + 0x1111 - i + even) ^ 0x3333 + i)
    return seed % 300

if __name__ == "__main__":
    plants = {}
    i = 0
    seed = 0x15
    seed2 = 0x17
    names = ["Tomato", "Carrot", "Onion", "Broccoli", "Pepper",
    "Cabbage", "Lettuce", "Spinach", "Potato", "Radish",
    "Celery", "Cucumber", "Garlic", "Beetroot", "Cauliflower",
    "Pumpkin", "Zucchini", "Eggplant", "Pea", "Corn",
    "Turnip", "Leek", "Asparagus", "Artichoke", "Okra",
    "Parsnip", "Kale", "Chard", "Fennel", "Endive",
    "Shallot", "Scallion", "Rutabaga", "Daikon", "Chili",
    "Ginger", "Horseradish", "Yam", "SweetPotato", "Watercress"]

    print("\n=== Plant Factory Output ===\n")
    for name in names:
        seed = rand_maison(seed, i)
        seed2 = rand_maison(seed2, i)
        plants[name] = Plant(name, seed, seed2)
        plants[name].display()
        i += 1
    #plants["Tomato"].display()
    print(f"\nTotal plants created: {len(names)}")
        