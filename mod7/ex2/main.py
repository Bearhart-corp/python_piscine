from ex0.Card import Card
from ex2.Combatable import Combatable
from ex2.Magical import Magical
from ex2.EliteCard import EliteCard


def get_class_methods(cls):
    return [name for name, v in cls.__dict__.items()
            if callable(v) and not name.startswith("__")]


def main():
    print("\n=== DataDeck Ability System ===\n")
    print("EliteCard capabilities:")
    print(f"- Card: {get_class_methods(Card)}")
    print(f"- Combatable: {get_class_methods(Combatable)}")
    print(f"- Magical: {get_class_methods(Magical)}")
    print("\nPlaying Arcane Warrior (Elite Card):\n")
    print("Combat phase:")
    # print(f"Attack result: ")
    elit = EliteCard("Arcane Warrior", 5, 'melee', 2)
    print(f"Attack result: {elit.attack('Enemy')}")
    print(f"Defense result: {elit.defend(3)}")
    print("\nMagic phase:")
    print(f"Spell cast: {elit.cast_spell()}")
    print(f"Mana channel: {elit.channel_mana(3)}")
    print("\nMultiple interface implementation successful!")


if __name__ == "__main__":
    main()
