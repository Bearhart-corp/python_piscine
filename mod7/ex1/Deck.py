from ex0.Card import Card
from ex0.Creature_card import CreatureCard
from ex1.spell_card import SpellCard
from ex1.ArtifactCard import ArtifactCard
import random


class Deck():
    def __init__(self):
        self.cards = []

    def add_card(self, card: Card) -> None:
        if "attack" in card:
            self.cards.append(CreatureCard(**card))
        elif "effect_type" in card:
            self.cards.append(SpellCard(**card))
        elif "durability" in card:
            self.cards.append(ArtifactCard(**card))

    def remove_card(self, card_name: str) -> bool:
        for card in self.cards:
            if card.name == card_name:
                self.cards.remove(card)
                return True
        return False

    def shuffle(self) -> None:
        random.shuffle(self.cards)

    def draw_card(self) -> Card:
        return self.cards.pop() if len(self.cards) > 0 else None

    def get_deck_stats(self) -> dict:
        result = {
            "total_cards": len(self.cards),
            "creatures": len([x for x in self.cards
                              if isinstance(x, CreatureCard)]),
            "spells": len([x for x in self.cards if isinstance(x, SpellCard)]),
            "artifacts": len([x for x in self.cards
                              if isinstance(x, ArtifactCard)]),
            "avg_cost": sum(card.cost for card in self.cards) / len(self.cards)
        }
        return result
