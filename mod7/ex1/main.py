from ex0.Card import Card
from ex0.Creature_card import CreatureCard
from tools.card_generator import CardGenerator


def main():
    game_state = {
        "available_mana": 6,
        "board": [],
        "hand": [],
        "opponent_board": []
    }
    generator = CardGenerator()
    data = generator.get_creature("Fire Dragon")
    fire_dragon = CreatureCard(**data)
    print("\n=== DataDeck Card Foundation ===\n")
    print("Testing Abstract Base Class Design:\n")
    print("CreatureCard Info:")
    print(data)
    data = generator.get_creature("Goblin Warrior")
    gob = CreatureCard(**data)
    print("\nPlaying Fire Dragon with 6 mana available:")
    print(f"Playable: {Card.is_playable(fire_dragon,
                                        game_state["available_mana"])}")
    print(f"Play result: {fire_dragon.play(game_state)}")
    print("\nFire Dragon attacks Goblin Warrior:")
    print(f"Attack result: {fire_dragon.attack_target(gob)}")
    print("\nTesting insufficient mana (3 available):")
    print(f"Playable: {Card.is_playable(fire_dragon,
                                        game_state["available_mana"])}")
    print("\nAbstract pattern successfully demonstrated!")


if __name__ == "__main__":
    main()
