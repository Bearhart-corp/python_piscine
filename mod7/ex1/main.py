from ex1.Deck import Deck
from tools.card_generator import CardGenerator
from typing import Any


def draw_play(deck: Deck, game_state: dict[str, Any]) -> None:
    """
    :args = the Deck, the game state
    :return None
    :draw a card from the deck and play it
    """
    game_state["hand"].append(Deck.draw_card(deck))
    print(f"Drew: {game_state['hand'][-1].name} \
({game_state['hand'][-1].__class__.__name__})")
    print(f"Play result: {game_state['hand'][-1].play(game_state)}\n")


def main():
    """
    gen 10 cards, add in the deck, draw 1 ans play it
    draw another and play it too
    """
    game_state = {
        "available_mana": 6,
        "board": [],
        "hand": [],
        "opponent_board": []
    }
    print("\n=== DataDeck Deck Builder ===\n")
    print("Building deck with different card types...")
    gen = CardGenerator()
    deck = Deck()
    data_deck = gen.generate_random_deck(10)
    for data in data_deck:
        deck.add_card(data)
    # {print(f"{card.name}", end=", ") for card in deck.cards}
    print(f"\nDeck stats: {Deck.get_deck_stats(deck)}")
    print("\nDrawing and playing cards:\n")
    draw_play(deck, game_state)
    draw_play(deck, game_state)
    print('Polymorphism in action: Same interface,\
 different card behaviors!')


if __name__ == "__main__":
    main()
