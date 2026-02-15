from ex0.Card import Card


class SpellCard(Card):
    def __init__(self, name: str, cost: int,
                 rarity: str, effect_type: str) -> None:
        self.name = name
        self.cost = cost
        self.rarity = rarity
        self.effect_type = effect_type
        if effect_type == "damage":
            self.damage = cost
            self.heal = 0
        else:
            self.damage = 0
            self.heal = cost

    def play(self, game_state: dict) -> dict:
        if game_state["available_mana"] >= self.cost:
            game_state["available_mana"] -= self.cost
            result = {
                "card_played": self.name,
                "mana_used": self.cost,
                "effect": "text"
            }
        else:
            result = {
                "card_played": self.name,
                "mana_used": 0,
                "effect": "Not enough mana to play this card"
            }
        return result

    def resolve_effect(self, targets: list) -> dict:
        pass
