class Plant:
    def __init__(self, name: str, water_level: int, sunlight_hours: int):
        self.name = name
        self.water_level = water_level
        self.sunlight_hours = sunlight_hours
        self.age = 0
        self.height = 0

    def add_plant(name: str, water_level: int, sunlight_hours: int):
        # vérifier que le nom soit valide
        if not name:
            raise PlantError("adding plant: Plant name cannot be empty!")
        # vérifier water_level et sunlight_hours valides
        if water_level < 1:
            raise PlantError(f"Water level {water_level} is too low (min 1)\n")
        if water_level > 10:
            raise PlantError(f"Water level {water_level}"
                             f" is too high (max 10)\n")
        if sunlight_hours < 2:
            raise PlantError(f"Sunlight hours {sunlight_hours}"
                             f" is too low (min 2)\n")
        if sunlight_hours > 12:
            raise PlantError(f"Sunlight hours {sunlight_hours}"
                             f"is too high (max 12)")
        obj = Plant(name, water_level, sunlight_hours)
        GardenManager.plants.append(obj)
        return f"Added {name} successfully"


class GardenError(Exception):
    pass


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


class GardenManager:
    plants = []

    def water_plants(plant_list):
        print("\nWatering plants...")
        print("Opening watering system")
        try:
            for plant in plant_list:
                if plant.water_level < 1:
                    raise WaterError(f"Not enought water for {plant.name}")
                print(f"Watering {plant.name} - success")
        except WaterError as e:
            print(f"Error: {e}")
        finally:
            print("Closing watering system (cleanup)\n")

    @staticmethod
    def check_plant_health(plant_list: list):
        print("Checking plant health...\n")
        for p in plant_list:
            try:
                if p.water_level < 1 or p.water_level > 10:
                    raise PlantError(f"Water level {p.water_level}"
                                     f" invalid for {p.name}")
                if p.sunlight_hours < 2 or p.sunlight_hours > 12:
                    raise PlantError(f"Sunlight hours {p.sunlight_hours}"
                                     f"invalid for {p.name}")
                print(f"{p.name}: healty (water: {p.water_level} sun:"
                      f" {p.sunlight_hours})")
            except PlantError as e:
                print(f"Error checking {p.name}: {e}")

    def test_garden_management():
        print("=== Garden Management System ===\n")
        print("Adding plants to garden...")
        try:
            print(Plant.add_plant("tomato", 8, 10))
        except PlantError as e:
            print(f"Error: {e}")
        try:
            print(Plant.add_plant("Lettuce", 8, 10))
        except PlantError as e:
            print(f"Error: {e}")
        print("\nTesting empty plant name...")
        try:
            print(Plant.add_plant(None, 8, 10))
        except PlantError as e:
            print(f"Error: {e}")
        print("Testing bad water level...")
        try:
            print(Plant.add_plant("tomato", 15, 8))
        except PlantError as e:
            print(f"Error: {e}")
        print("Testing bad sunlight hours...")
        try:
            print(Plant.add_plant("tomato", 8, 0))
        except PlantError as e:
            print(f"Error: {e}")
        GardenManager.water_plants(GardenManager.plants)
        GardenManager.check_plant_health(GardenManager.plants)
        print("\nGarden management system test complete!")


if __name__ == "__main__":
    GardenManager.test_garden_management()
# manque des trucs...
