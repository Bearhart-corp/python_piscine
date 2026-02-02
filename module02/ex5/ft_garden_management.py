class Plant:
    water_tank = 10

    def __init__(self, name: str, water_level: int, sunlight_hours: int):
        self.name = name
        self.water_level = water_level
        self.sunlight_hours = sunlight_hours
        self.age = 0
        self.height = 0

    def add_plant(name: str, water_level: int, sunlight_hours: int):
        # vérifier que le nom soit valide
        obj = Plant(name, water_level, sunlight_hours)
        if not name:
            raise PlantError()
        GardenManager.plants.append(obj)
        return f"Added {name} successfully"


class GardenError(Exception):
    def __init__(self, detail: str):
        if detail == "":
            detail = "Still no water in the tank to water the plants!"
        super().__init__(f"Error: {detail}")


class PlantError(GardenError):
    def __init__(self):
        super().__init__("Plant name cannot be empty!")


class WaterError(GardenError):
    def __init__(self, plant: Plant):
        msg = f"Checking {plant.name}: "
        if plant.water_level > 10:
            super().__init__(
                f"{msg}Water level {plant.water_level}"
                " is too high (max 10)")
        elif plant.water_level < 2:
            super().__init__(f"{msg}Water level {plant.water_level}"
                             " is too low (min 1)")


class SunError(GardenError):
    def __init__(self, plant: Plant):
        super().__init__(f"Sun hours {plant.sunlight_hours}"
                         f" is not correct")


class GardenManager:
    plants = []

    def check_tank():
        try:
            if Plant.water_tank <= 0:
                raise GardenError("")
            else:
                print("We have enough water")
        except GardenError as e:
            print(f"{e}")
        finally:
            print("System recovered and continuing...")

    def water_plants(plant_list):
        print("\nWatering plants...")
        print("Opening watering system")
        try:
            for plant in plant_list:
                if Plant.water_tank > 0:
                    Plant.water_tank -= 1
                    print(f"Watering {plant.name} - success")
                else:
                    raise GardenError("")
        except GardenError as e:
            print(f"{e}")
        finally:
            print("Closing watering system (cleanup)\n")

    @staticmethod
    def check_plant_health(plant_list: list):
        print("Checking plant health...\n")
        for p in plant_list:
            try:
                if p.water_level < 1 or p.water_level > 10:
                    raise WaterError(p)
                elif p.sunlight_hours < 2 or p.sunlight_hours > 12:
                    raise SunError(p)
                else:
                    print(f"{p.name}: healty (water: {p.water_level} sun:"
                          f" {p.sunlight_hours})")
            except SunError as e:
                print(f"{e}")
            except WaterError as e:
                print(f"{e}")

    def test_garden_management():
        print("=== Garden Management System ===\n")
        print("Adding plants to garden...")
        try:
            print(Plant.add_plant("tomato", 8, 10))
        except PlantError as e:
            print(f"{e}")
        try:
            print(Plant.add_plant("Lettuce", 9, 4))
        except PlantError as e:
            print(f"{e}")
        print("\nTesting empty plant name...")
        try:
            print(Plant.add_plant(None, 8, 10))
        except PlantError as e:
            print(f"{e}")
        print(Plant.add_plant("Bad Plant water", 15, 8))
        print(Plant.add_plant("Bad Plant sun", 8, 0))
        GardenManager.water_plants(GardenManager.plants)
        GardenManager.check_plant_health(GardenManager.plants)
        print("\nTesting error recovery...")
        GardenManager.check_tank()
        print(f"Water tank level: {Plant.water_tank}")
        GardenManager.water_plants(GardenManager.plants)
        print(f"Water tank level: {Plant.water_tank}")
        GardenManager.water_plants(GardenManager.plants)
        print(f"Water tank level: {Plant.water_tank}")
        GardenManager.check_tank()
        print("\nGarden management system test complete!")


if __name__ == "__main__":
    GardenManager.test_garden_management()
# manque des trucs...
