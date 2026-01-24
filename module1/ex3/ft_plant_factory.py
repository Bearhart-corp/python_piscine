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
    return seed % 200

def is_unique(seen, i: int, seed: int, seed2: int)-> int:
    for j in range(0, i):
        if seed == seen[j][0] and seed2 == seen[j][1]:
            return False
    return True

if __name__ == "__main__":
    plants = {}
    seen = [[0] * 2 for _ in range(400)]
    i = 0
    seed = 0x15
    seed2 = 0x17
    names = ["Acer", "Salvia", "Verbena", "Laurus", "Rubus", "Ulmus",
"Juniperus", "Ficus", "Plantago", "Artemisia", "Quercus", "Betula",
"Alnus", "Populus", "Fraxinus", "Malva", "Ruta", "Mentha", "Thymus", "Cistus"]

    print("\n=== Plant Factory Output ===\n")
    for i in range(0, 100):
        seed = rand_maison(seed, i)
        seed2 = rand_maison(seed2, i)
        seen[i][0] = 1 << (seed % len(names))
        seen[i][1] = 1 << (seed2 % len(names))
        while is_unique(seen, i, seed % len(names), seed2 % len(names)) == False:
            seed = rand_maison(seed, i)
            seed2 = rand_maison(seed2, i)
        seen[i][0] = (seed % len(names))
        seen[i][1] = (seed2 % len(names))
        name = names[seed % len(names)] + " " +  names[seed2 % len(names)]
        plants[name] = Plant(name, seed, seed2)
        plants[name].display()
    print(f"\nTotal plants created: {i + 1}")
