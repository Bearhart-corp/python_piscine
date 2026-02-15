from ex4.TournamentCard import TournamentCard
from ex4.TournamentPlatform import TournamentPlatform


def get_class_methods(cls):
    return [cls.__name__ for cls in type(cls).__bases__]


def main():
    print("\n=== DataDeck Tournament Platform ===\n")
    print("Registering Tournament Cards...\n")
    dragon = TournamentCard("Fire Dragon", "dragon_001", 1200)
    print(f"{dragon.name} (ID: {dragon.id_name}):")
    print(f"- Interfaces: {get_class_methods(dragon)}")
    print(f"- Rating: {dragon.rating}")
    print(f"- Record: {dragon.wins}-{dragon.losses}\n")

    wizard = TournamentCard("Ice Wizard", "wizard_001", 1150)
    print(f"{wizard.name} (ID: {wizard.id_name}):")
    print(f"- Interfaces: {get_class_methods(wizard)}")
    print(f"- Rating: {wizard.rating}")
    print(f"- Record: {wizard.wins}-{wizard.losses}\n")
    print("Creating tournament match...")
    t = TournamentPlatform()
    print(f"Match result: {t.create_match("dragon_001", "wizard_001")}")
    print("\nTournament Leaderboard")


if __name__ == "__main__":
    main()
