class Player:
    def __init__(self, name: str, achiev: set, lvl: int):
        self.name = name
        self.achiev = achiev
        self.lvl = lvl
    
    @staticmethod
    def display(players: list):
        for player in players:
            print(f"Player {player.name:{' '}<8} achievements: {player.achiev}")

def main():
    print("=== Achievement Tracker System ===\n")
    players = []
    myset = {'first_kill', 'level_10', 'treasure_hunter', 'speed_demon'}
    myset1 = {'level_10', 'speed_demon'}
    myset2 = {'first_kill', 'treasure_hunter', 'speed_demon'}
    tom = Player("Tom", myset, 11)
    lara = Player("Lara", myset1, 24)
    lilou = Player("Lilou", myset2, 4)
    players.append(tom)
    players.append(lara)
    players.append(lilou)
    Player.display(players)
    print("\n=== Achievement Analytics ===\n")
    a = myset.union(myset1)
    a = a.union(myset2)
    print(f"All unique achievements: {a}")
    print(f"Total unique achievement: {len(a)}")
    b = myset.intersection(myset1)
    b = b.intersection(myset2)
    print(f"Common to all players: {b}")
    a = a.difference(b)
    print(f"Rare achievements (1 player): {a}")
    print(f"{tom.name} vs {lara.name} common: {tom.achiev.intersection(lara.achiev)}")
    print(f"{lara.name} unique: {lara.achiev.difference(tom.achiev)}")
    print(f"{lilou.name} unique: {lilou.achiev.difference(lara.achiev)}")

if __name__ == "__main__":
    main()