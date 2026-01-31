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

    def water_auto(self):
        for garden in self.gardens:
            for plant in garden.plants:
                if plant.water_reserves < plant.water_need:
                    plant.water_reserves = Plant.max_water_cap
                    print(f"Watering {plant.name} in {garden.name}")

    def display_all_garden(self):
        for garden in self.gardens:
            print(f"\n{garden.name}\n")
            for plant in garden.plants:
                plant.display()

    def daily_update_all(self):
        for garden in self.gardens:
            garden.daily_update()

    def simulator(self, days: int):
        for i in range(days):
            self.daily_update_all()

    def generation_auto(self, nbr_garden: int, nbr_plants: int):
        dico = []
        plants = []
        garden_names = ["Neo", "Morpheus", "Trinity", "Agent Smith",
                        "The Oracle", "Niobe", "The Merovingian",
                        "Persephone", "Link", "Seraph", "Mouse", "Dozer",
                        "Tank", "Commander Lock", "Ghost", "Switch",
                        "Apoc", "Cypher", "Bane", "Sati"]

        k = 0
        for i in range(nbr_garden):
            dico.append(f"test{i}")

        for j in range(0, nbr_garden):
            garden = self.add_garden(f"\033[0;32m=== {garden_names[j]}'s"
                                     f"Garden ===\033[0;0m")

        for garden in self.gardens:
            plants = garden.gen_plants(nbr_plants[k], id(dico[k]))
            k += 1
            for plant in plants:
                garden.add_plant(plant)

    def simulator_auto(self, nbr_days: int):
        for i in range(nbr_days):
            print(f"\nDay Number {i} in the simulation ")
            self.display_all_garden()
            self.simulator(1)
            self.water_auto()

    def who_died(self):
        nobody = 0
        for garden in self.gardens:
            if len(garden.plants) == 0:
                nobody = 1
                print(f"The {garden.name} quit the matrix")
        if nobody == 0:
            print("Nobody died")

    @staticmethod
    def validate_height(height):
        print(f"Height validation test: {(height >= 0)}")

    class GardenStats:
        def __init__(self, garden):
            self.garden = garden

        def count_plants(self):
            return len(self.garden.plants)

        def total_growth(self):
            total = 0
            for plant in self.garden.plants:
                total += plant.height
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
    def is_unique(seen, i: int, seed: int, seed2: int, len: int) -> int:
        if seen[(seed * len) + seed2] == 1:
            return False
        return True

    def gen_plants(self, n: int, input_seed: int) -> None:
        if n > 400:
            return print("error")
        plants = []
        seen = [[0] for _ in range(400)]
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
                                       seed2 % len_names, len_names):
                seed = Garden.rand_maison(seed, i)
                seed2 = Garden.rand_maison(seed2, i)
            # we fill the seen table
            seen[(seed % len_names) * len_names + (seed2 % len_names)] = 1
            name = names[seed % len_names] + " " + names[seed2 % len_names]
            plants.append(Plant(name, seed % 10 + 1, seed2 % 10 + 1))
        return plants

    def add_plant(self, plant):
        self.plants.append(plant)

    def total_water_need(self):
        count = 0
        for plant in self.plants:
            count += plant.water_need()
        return count

    def daily_update(self):
        dead_plants = []
        for p in self.plants:
            p.age += 1
            p.height += p.grow_cap
            p.water_reserves -= p.water_need
            if p.water_reserves < 0 or (p.life_expectency - p.age) <= 0:
                print(f"{p.name} from {self.name} is dead #snif")
                dead_plants.append(p)
        for p in dead_plants:
            self.plants.remove(p)

    def stats(self):
        return GardenManager.GardenStats(self)


class Plant:
    max_water_cap = 50

    def __init__(self, name: str, water_need: int, grow_cap: int):
        self.name = name
        self.water_need = water_need
        self.grow_cap = grow_cap
        self.age = 0
        self.height = 0
        self.water_reserves = 11
        self.life_expectency = 10 * water_need

    def display(self, block_width=40):
        label = ["Plant name", "Height", "Age",
                 "Water Needs", "Growth Capacity", "Water Reserve"]

        print(f"{label[0]:{' '}<15}:{self.name}")
        print(f"{label[1]:{' '}<15}:{self.height} cm")
        print(f"{label[2]:{' '}<15}:{self.age} day{'s' * (self.age > 1)}")
        print(f"{label[3]:{' '}<15}:{self.water_need}")
        print(f"{label[4]:{' '}<15}:{self.grow_cap}")
        print(f"{label[5]:{' '}<15}:{self.water_reserves}")
        print("-" * 40)

    def water_the_plant(self):
        self.water_reserves = Plant.max_water_cap


class FloweringPlant(Plant):
    def __init__(self, name: str, color: str) -> None:
        super().__init__(name=name, )
        self.color = color

    def bloom(self):
        print(f"{self.name} is blooming beautifully!\n")


class PrizeFlower(FloweringPlant):
    def points(self):
        return id(self.color) % 20


def main(nbr_garden: int, nbr_plants: list, nbr_day_in_the_matrix: int):
    total = 0
    if nbr_garden >= 20:
        return print("is it too much garden to handle for the matrix")
    for i in range(len(nbr_plants)):
        total += nbr_plants[i]
        if total >= 100:
            return print("is it too much plants to handle for the matrix")
    nbr_day_2simulate = nbr_day_in_the_matrix
    manager = GardenManager()
    manager.generation_auto(nbr_garden, nbr_plants)
    manager.simulator_auto(nbr_day_2simulate)
    manager.who_died()


if __name__ == "__main__":
    plants_nbr = [5, 5, 5, 5]
    main(len(plants_nbr), plants_nbr, 75)
