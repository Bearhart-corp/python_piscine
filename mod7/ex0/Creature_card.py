from ex0.Card import Card


class CreatureCard(Card):
    def __init__(self, name: str, cost: int,
                 rarity: str, attack: int, health: int):
        super().__init__(name, cost, rarity)
        if attack < 0:
            raise ValueError
        if health < 0:
            raise ValueError
        self.attack = attack
        self.health = health

    def play(self, game_state: dict) -> dict:
        if game_state["available_mana"] >= self.cost:
            game_state["available_mana"] -= self.cost
            game_state["board"].append(self)
            result = {
                "card_played": self.name,
                "mana_used": self.cost,
                "effect": "Creature summoned to battlefield"
            }
        else:
            result = {
                "card_played": self.name,
                "mana_used": 0,
                "effect": "Not enough mana to play this card"
            }
        return result

    def attack_target(self, target: Card) -> dict:
        dico = {
            "attacker": self.name,
            "target": target.name,
            "damage_dealt": self.attack,
            'combat_resolved': True
        }
        target.health -= self.attack
        if target.health < 0:
            target.health = 0
        return dico
