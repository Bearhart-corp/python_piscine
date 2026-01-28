class SecurePlant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.__height = 0
        self.__age = 0
        print(f"Plant created: {self.name}")

    def get_data(self):
        print(f"\nCurrent Plant: {self.name}"
              f" ({self.height}cm, {self.age} days)")

    def set_height(self, height: int):
        if height < 0:
            print(f"\nInvalid operation attempted:"
                  f" height {height}cm [REJECTED]\n"
                  f"Security: Negative height rejected")
        else:
            self.height = height
            print(f"Height updated: {height}cm [OK]")

    def set_age(self, age: int):
        if age < 0:
            print(f"\nInvalid operation attempted: age {age} [REJECTED]\n"
                  f"Security: Negative age rejected")
        else:
            self.age = age
            print(f"Age updated: {age} days [OK]")


if __name__ == "__main__":
    print("=== Garden Security System ===")
    tomate = SecurePlant("Tomate", 11, 12)
    tomate.set_height(25)
    tomate.set_age(30)
    tomate.set_height(-5)
    tomate.set_age(-10)
    tomate.get_data()
