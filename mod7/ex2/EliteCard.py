from ex0.Card import Card
from ex2.Magical import Magical
from ex2.Combatable import Combatable


class EliteCard(Card, Magical, Combatable):
    def __init__(self, name: str, damage: int, combat_type: str,
                 defense: int):
        self.name = name
        self.damage = damage
        self.combat_type = combat_type
        self.defense = defense
        self.still_alive = True
        self.pv = 10
    # card

    def play(self, game_state: dict) -> dict:
        pass
    # combatable

    def attack(self, target) -> dict:
        result = {
            'attacker': self.name,
            'target': target,
            'damage': self.damage,
            'combat_type': self.combat_type
        }
        return result

    def defend(self, incoming_damage: int) -> dict:
        self.pv -= incoming_damage
        result = {
            'defender': self.name,
            'damage_taken': incoming_damage,
            'damage_blocked': self.defense,
            'still_alive': (self.pv > 0)
        }
        return result

    def get_combat_stats(self) -> dict:
        pass
    # magical

    def cast_spell(self) -> dict:
        result = {
            'caster': self.name,
            'spell': "fireball",
            'targets': ['Enemy1', 'Enemy2'],
            'mana_used': 4
        }
        return result

    def get_magic_stats(self) -> dict:
        pass

    def channel_mana(self, amount: int) -> dict:
        result = {
            'channeled': amount,
            'total_mana': 4,
        }
        return result
