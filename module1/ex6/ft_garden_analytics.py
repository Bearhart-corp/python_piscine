class GardenManager:

    def __init__(self):
        self.garden_stat = self.GardenStats
        self.gardens = []

    def add_garden(self, name: str):
        garden = Garden(name)
        self.gardens.append(garden)
        return garden

    def create_garden_network(self):
        return self.gardens

    @staticmethod
    def validate_height(height):  # quimporte l'instance donnee
        print(f"Height validation test: {(height >= 0)}")

    class GardenStats:
        def __init__(self, garden):
            self.garden = garden

        def count_plants(self):
            return len(self.garden.plants)

        def total_growth(self):
            total = 0
            for plant in self.garden.plants:
                total += self.garden.plants.height
            return total

        def type_breakdown(self):
            res = {}
            for plant in self.garden.plants:
                t = type(plant).__name__
                res[t] = res.get(t, 0) + 1
            return res


class Garden:

    def __init__(self, name: str):
        self.name = name
        self.plants = []

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

    def gen_plants(self, n: int, input_seed: int) -> None:
        if n > 400:
            return print("error")
        plants = []
        seen = [[0] * 2 for _ in range(400)]
        i = 0
        seed = input_seed
        seed2 = input_seed << 2 ^ 0x55
        names = ["Acer", "Salvia", "Verbena", "Laurus", "Rubus", "Ulmus",
                 "Juniperus", "Ficus", "Plantago", "Artemisia", "Quercus",
                 "Betula", "Alnus", "Populus", "Fraxinus", "Malva",
                 "Ruta", "Mentha", "Thymus", "Cistus"]
        len_names = len(names)

        for i in range(n):
            seed = Garden.rand_maison(seed, i)
            seed2 = Garden.rand_maison(seed2, i)
            while not Garden.is_unique(seen, i, seed % len_names,
                                       seed2 % len_names):
                seed = Garden.rand_maison(seed, i)
                seed2 = Garden.rand_maison(seed2, i)
            seen[i][0] = (seed % len_names)
            seen[i][1] = (seed2 % len_names)
            name = names[seed % len_names] + " " + names[seed2 % len_names]
            plants.append(Plant(name, seed, seed2))
        return plants

    def add_plant(self, plant):
        self.plants.append(plant)

    def total_water_need(self):
        count = 0
        for plant in self.plants:
            count += plant.water_need()
        return count

    def grow_all(self):
        for p in self.plants:
            p.age += 1

    def stats(self):
        return GardenManager.GardenStats(self)


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
        return id(self.color) % 20


def main(nbr_garden: int, nbr_plants: list):
    manager = GardenManager()
    dico = []
    plants = []
    k = 0
    for i in range(0, 10):
        dico.append(f"test{i}")

    for j in range(0, nbr_garden):
        garden = manager.add_garden(f"Garden{j}")

    for garden in manager.gardens:
        plants = garden.gen_plants(nbr_plants[k], id(dico[k]))
        k += 1
        print(f"\n{garden.name}\n")
        for plant in plants:
            garden.add_plant(plant)
            plant.display()
        stats = GardenManager.GardenStats(garden)
        print(f"\n{stats.count_plants()}")


if __name__ == "__main__":
    main(3, [4, 3, 20])
