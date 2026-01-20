class Plants:
    def __init__(self, name, height, age, msg):
        self.name = name
        self.height = height
        self.age = age
        self.msg = msg

if __name__ == "__main__":
    tomato = Plants("Tomate", "25cm", 1, "day old")
    kartofel = Plants("Kartofel", "0cm", 123, "days old")
    pear = Plants("Pear", "120cm", 365, "days old")
    print("=== Garden Plant Registry ===")
    print(f"{tomato.name}: {tomato.height}, {tomato.age} {tomato.msg}")
    print(f"{kartofel.name}: {kartofel.height}, {kartofel.age} {kartofel.msg}")
    print(f"{pear.name}: {pear.height}, {pear.age} {pear.msg}")