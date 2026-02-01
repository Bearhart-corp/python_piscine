def garden_operations():
    print("Testing ValueError...")
    try:
        int("abc")
    except ValueError as error:
        print(f"ValueError: {error}")
    print("\nTesting ZeroDivisionError...")
    try:
        10 // 0
    except ZeroDivisionError as err:
        print(f"ZeroDivisionError: {err}")
    print("\nTesting FileNotFoundError...")
    try:
        open("mon/path")
    except FileNotFoundError as e:
        print(f"FileNotFoundError: {e}")
    print("\nTesting KeyError...")
    try:
        dico = {}
        dico["random"]
    except KeyError as er:
        print(f"KeyError: {er}")


def test_error_types():
    print("=== Garden Error Types Demo ===\n")
    garden_operations()


if __name__ == "__main__":
    test_error_types()
