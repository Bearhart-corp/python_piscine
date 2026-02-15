from ex0.Card import Card


class ArtifactCard(Card):
    def __init__(self, name: str, cost: int,
                 rarity: str, durability: int, effect: str) -> None:
        self.name = name
        self.cost = cost
        self.rarity = rarity
        self.durability = durability
        self.effect = effect

    def play(self, game_state: dict) -> dict:
        if game_state["available_mana"] >= self.cost:
            game_state["available_mana"] -= self.cost
            game_state["board"].append(self)
            result = {
                "card_played": self.name,
                "mana_used": self.cost,
                "durability": self.durability,
                "effect": self.effect
            }
        else:
            result = {
                "card_played": self.name,
                "mana_used": 0,
                "effect": "Not enough mana to play this card"
            }
        return result

    def activate_ability(self) -> dict:
        result = {
                "card_played": self.name,
                "durability": self.durability,
                "effect": self.effect
            }
        return result
