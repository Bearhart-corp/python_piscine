class GardenManager:
    def __init__(self):
        self.gardens = []
        # ou ss init et 1 seul manager avec une liste de jardin

    def add_garden(self, garden_name):
        self.gardens.append(garden_name)

    def create_garden_network(cls):
        pass

    @staticmethod
    def validate_height(height):  # quimporte l'instance donnee
        print(f"Height validation test: {(height >= 0)}")

    class GardenStats:
        def __init__(self, garden):
            self.garden = garden

        def count_plants(self):
            pass

        def total_growth(self):
            pass

        def type_breakdown(self):
            pass


class Garden:

    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.plants = []

    def add_plant(self, plant):
        if len(self.plants) >= self.capacity:
            return print("error")
        else:
            self.plants.append(plant)

    def total_water_need(self):
        count = 0
        for plant in self.plants:
            count += plant.water_need()
        return count

    def grow_all(self, plant):
        for p in self.plants:
            self.plants[p].age += 1

    def stats(self, GardenStats):
        pass


class Plant:
    def __init__(self, name: str, height: int, age: int):
        self.name = name
        self.height = height
        self.age = age

    def display(self):
        print(f"Created: {self.name} ({self.height}cm,"
              f" {self.age} day{'s' * (self.age > 1)})")


class FloweringPlant(Plant):
    def __init__(self, name: str, height: int, age: int, color: str) -> None:
        super().__init__(name=name, height=height, age=age)
        self.color = color

    def bloom(self):
        print(f"{self.name} is blooming beautifully!\n")


class PrizeFlower(FloweringPlant):
    def points(self):
        pass


class PlantFactory:
    @staticmethod
    def rand_maison(seed, even: int) -> int:
        i = even
        j = id(i) % 0x100
        even = not (even & 1)
        seed = (((seed * 13 + i + 37 + even) ^ (0xa5 * even + i) ^ j) >> 1)
        seed = ((seed ^ 0x5555 + 0x1111 - i + even) ^ 0x3333 + i) ^ j
        return seed % 200

    @staticmethod
    def is_unique(seen, i: int, seed: int, seed2: int) -> int:
        for j in range(0, i):
            if seed == seen[j][0] and seed2 == seen[j][1]:
                return False
        return True

    @staticmethod
    def gen_plants(n: int, input_seed: int) -> None:
        plants = {}
        if n > 400:
            return print("error")
        seen = [[0] * 2 for _ in range(400)]
        i = 0
        seed = input_seed
        seed2 = input_seed << 2 ^ 0x55
        names = ["Acer", "Salvia", "Verbena", "Laurus", "Rubus", "Ulmus",
                 "Juniperus", "Ficus", "Plantago", "Artemisia", "Quercus",
                 "Betula", "Alnus", "Populus", "Fraxinus", "Malva",
                 "Ruta", "Mentha", "Thymus", "Cistus"]
        len_names = len(names)

        for i in range(0, n):
            seed = rand_maison(seed, i)
            seed2 = rand_maison(seed2, i)
            while not is_unique(seen, i, seed % len_names, seed2 % len_names):
                seed = rand_maison(seed, i)
                seed2 = rand_maison(seed2, i)
            seen[i][0] = (seed % len_names)
            seen[i][1] = (seed2 % len_names)
            name = names[seed % len_names] + " " + names[seed2 % len_names]
            plants[name] = Plant(name, seed, seed2)
            plants[name].display(plants[name].age)


if __name__ == "__main__":
    dico = []
    for i in range(0, 10):
        dico.append(i)

    for j in range(0, 10):
        gen_plants(10, id(dico[j]))
        print(f"\n === garden number: {j}\n\n")


# GardenManager
#  ├── gardens (dict)
#  ├── add_garden()            → self
#  ├── create_garden_network() → cls
#  ├── validate_height()       → staticmethod
#  └── GardenStats (nested)
#        ├── count_plants()
#        ├── total_growth()
#        └── type_breakdown()

# Garden
#  ├── plants (list)
#  ├── add_plant()             → self
#  ├── grow_all()              → self
#  └── stats                   → GardenStats

# Plant
#  ├── grow()                  → self

# FloweringPlant(Plant)
#  ├── color
#  ├── blooming

# PrizeFlower(FloweringPlant)
#  ├── points
