def check_temperature(temp_str: str) -> None:
    try:
        temp = int(temp_str)
        if temp < 0:
            print(f"Error: {temp}°C is too cold for plants (min 0°C)\n")
        elif temp > 40:
            print(f"Error: {temp}°C is too hot for plants (max 40°C)\n")
        else:
            print(f"Temperature {temp}°C is perfect for plants!\n")
    except ValueError:
        return (print("Enter a correct value please\n"))


def main():
    yes = 'Y'
    while True:
        print("=== Garden Temperature Checker ===\n")
        check_temperature(input("Testing temperature: "))
        while yes in ('y', 'Y', 'n', 'N'):
            yes = input("Do you wanna continue ? [Y/n]")
            if yes in ('Y', 'y'):
                break
            elif yes in ('n', 'N'):
                return
            else:
                print("type a correct input")
    return 0


if __name__ == "__main__":
    main()
