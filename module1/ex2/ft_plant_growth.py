class Plant:
    def __init__(self, name: str, height: int, age: int, count) -> None:
        self.name = name
        self.height = height
        self.age = age
        self.count = count
        
    def grow(self, cm: int=0, day: int=1):
        self.height += cm
        self.count += cm
        self.age += day
    
    def get_info(self):
        print(f"{self.name}: {self.height}cm, {self.age} days old")
    
    def simul(self, days, daily_grow):
        for day in range(1, days + 1):
            print(f"=== Day {day} ===")
            self.grow(cm=daily_grow)
            self.get_info()
    
if __name__ == "__main__":
    tomato = Plant("Tomato", 25, 10, 0)
    beens = Plant("Beens", 35, 1, 0)
    brocoli = Plant("Brocoli", 10, 2, 0)
    tomato.simul(7, 10)
    print(f"Growth this week: +{tomato.count}cm\n")
    beens.simul(7, 2)
    print(f"Growth this week: +{beens.count}cm\n")
    brocoli.simul(7, 1)
    print(f"Growth this week: +{brocoli.count}cm\n")
