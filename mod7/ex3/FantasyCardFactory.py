from ex3.CardFactory import CardFactory
from ex0.Creature_card import CreatureCard
from ex0.Card import Card
from ex1.spell_card import SpellCard
from ex1.ArtifactCard import ArtifactCard
from tools.card_generator import CardGenerator
import random
# Creates fantasy-themed creatures (Dragons, Goblins, etc.)
# • Creates elemental spells (Fire, Ice, Lightning)
# • Creates magical artifacts (Rings, Staffs, Crystals)
# • Supports extensible card type registration


class FantasyCardFactory(CardFactory):
    def create_creature(self, name_or_power:
                        str | int | None = None) -> Card:
        gen = CardGenerator()
        result = gen.get_random_creature()
        if result is None:
            return None
        else:
            return CreatureCard(**result)

    def create_spell(self, name_or_power:
                     str | int | None = None) -> Card:
        gen = CardGenerator()
        result = gen.get_random_spell()
        if result is None:
            return None
        else:
            return SpellCard(**result)

    def create_artifact(self, name_or_power:
                        str | int | None = None) -> Card:
        gen = CardGenerator()
        result = gen.get_random_artifact()
        if result is None:
            return None
        else:
            return ArtifactCard(**result)

    def create_themed_deck(self, size: int) -> dict:
        deck = {}
        for i in range(size):
            card_type = random.choice(["creature", "spell", "artifact"])
            if card_type == "creature":
                deck[i] = self.create_creature()
            elif card_type == "spell":
                deck[i] = self.create_spell()
            else:
                deck[i] = self.create_artifact()
        return deck

    def get_supported_types(self) -> dict:
        gen = self.create_themed_deck(3)
        return {
            "creatures": [c.name for c in gen.values()
                          if isinstance(c, CreatureCard)],
            "spells": [s.name for s in gen.values()
                       if isinstance(s, SpellCard)],
            "artifacts": [a.name for a in gen.values()
                          if isinstance(a, ArtifactCard)],
        }
