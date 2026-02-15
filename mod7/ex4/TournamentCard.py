from ex0.Card import Card
from ex2.Combatable import Combatable
from ex4.Rankable import Rankable

# Avoir un id unique
# Avoir un rating (ex: 1200)
# Avoir wins / losses
# Pouvoir attaquer
# Pouvoir jouer
# Pouvoir recalculer son rating
# EA​=1/(1+10(RB​−RA​)/400)
# RA′​=RA​+K×(SA​−EA​)


class TournamentCard(Card, Combatable, Rankable):
    def __init__(self, name: str, id_name: str, rating: int):
        self.name = name
        self.rating = rating
        self.wins = 0
        self.losses = 0
        self.id_name = id_name

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

    def calculate_rating(self) -> int:
        pass

    def get_tournament_stats(self) -> dict:
        pass

    def update_wins(self, wins: int) -> None:
        self.wins += 16
        self.rating += int(16 * (1 + ((wins + 1) / 4)))

    def update_losses(self, losses: int) -> None:
        self.losses += losses
        self.rating -= int(16 * (1 + ((losses + 1) / 4)))

    def get_rank_info(self) -> dict:
        pass
