def check_plant_health(plant_name: str, water_level: int, sunlight_hours: int):
    if plant_name is None or plant_name == "":
        raise ValueError("Plant name cannot be empty!\n")

    if water_level < 1:
        raise ValueError(f"Water level {water_level} is too low (min 1)\n")
    if water_level > 10:
        raise ValueError(f"Water level {water_level} is too high (max 10)\n")

    if sunlight_hours < 2:
        raise ValueError(f"Sunlight hours {sunlight_hours} is too low (min 2)"
                         f"\n")
    if sunlight_hours > 12:
        raise ValueError(f"Sunlight hours {sunlight_hours}"
                         f"is too high (max 12)")

    return "Plant 'tomato' is healthy!\n"


def test_plant_checks():
    """fonction qui test la fonction qui check les plantes"""
    print("=== Garden Plant Health Checker ===\n")
    print("Testing good values...")
    try:
        print(check_plant_health("tomato", 8, 10))
    except ValueError as e:
        print(f"Error: {e}")
    print("Testing empty plant name...")
    try:
        check_plant_health(None, 8, 10)
    except ValueError as e:
        print(f"Error: {e}")
    print("Testing bad water level...")
    try:
        check_plant_health("tomato", 15, 10)
    except ValueError as e:
        print(f"Error: {e}")
    print("Testing bad sunlight hours...")
    try:
        check_plant_health("tomato", 8, 0)
    except ValueError as e:
        print(f"Error: {e}")
    print("All error raising tests completed!")


if __name__ == "__main__":
    test_plant_checks()
