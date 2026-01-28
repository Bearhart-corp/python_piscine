class Plants:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age
        self.other = None
        if age > 1:
            self.msg = "days"
        else:
            self.msg = "day"

    def get_info(self, other: str):
        self.other = other
        print(f"{self.name} ({type(self).__name__}): {self.height}cm, "
              f"{self.age} days, {self.other}")


class Flower(Plants):
    def __init__(self, name: str, height: int, age: int, color: str) -> None:
        super().__init__(name=name, height=height, age=age)
        self.color = color

    def bloom(self):
        print(f"{self.name} is blooming beautifully!")


class Tree(Plants):
    def __init__(self, name: str, height: int,
                 age: int, trunk_diameter: int) -> None:
        super().__init__(name=name, height=height, age=age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self):
        print(f"{self.name} provides "
              f"{int(self.height * (self.trunk_diameter / 100))}"
              f" square meters of shade")


class Vegetables(Plants):
    def __init__(self, name: str, height: int, age: int,
                 harvest_season: str, nutritional_value: str) -> None:
        super().__init__(name=name, height=height, age=age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value


if __name__ == "__main__":
    print("=== Garden Plant Types ===\n")
    lys = Flower("Lys", 10, 20, "rouge")
    tulipe = Flower("Tulipe", 12, 45, "jaune")
    boulot = Tree("Boulot", 150, 720, 15)
    chene = Tree("Chene", 400, 1825, 45)
    brocoli = Vegetables("Brocoli", 20, 45, "Spring", "A")
    concumber = Vegetables("concumber", 15, 60, "Summer", "A")
    chene.get_info(f"{chene.trunk_diameter}cm diameter")
    chene.produce_shade()
    lys.get_info(f"{lys.color}")
    lys.bloom()
    brocoli.get_info(f"{brocoli.harvest_season} harvest "
                     f"\n{brocoli.name} is rich in vitamin "
                     f"{brocoli.nutritional_value}")
