class GardenError(Exception):
    def __init__(self, msg):
        super().__init__(msg)


class PlantError(GardenError):
    def __init__(self, msg):
        super().__init__(msg)

    def plant_error():
        raise PlantError("The tomato plant is wilting!\n")


class WaterError(GardenError):
    def __init__(self, msg):
        super().__init__(msg)

    def water_error():
        raise WaterError("Not enough water in the tank!\n")


def main():
    print("=== Custom Garden Errors Demo ===\n")
    print("Testing PlantError...")
    """in class PLantError do raise error and catch it in except then print"""
    try:
        PlantError.plant_error()
    except PlantError as e:
        print(f"Caught PlantError: {e}")
    print("Testing WaterError...")
    try:
        WaterError.water_error()
    except WaterError as e:
        print(f"Caught WaterError: {e}")
    print("Testing catching all garden errors...")
    try:
        PlantError.plant_error()
    except GardenError as e:
        print(f"Caught a garden error: {e}")
    try:
        WaterError.water_error()
    except GardenError as e:
        print(f"Caught a garden error: {e}")
    print("All custom error types work correctly!")


if __name__ == "__main__":
    main()
