from ex4.TournamentCard import TournamentCard
import random
# stocker les cartes (dict id → card)
# créer des matchs
# décider du gagnant
# mettre à jour wins/losses
# mettre à jour rating
# produire un leaderboard trié


class TournamentPlatform():
    def register_card(self, card: TournamentCard) -> str:
        pass

    def create_match(self, card1_id: str, card2_id: str) -> dict:
        c1 = TournamentCard("test", card1_id, 1200)
        c2 = TournamentCard("test2", card2_id, 1150)
        odd = random.uniform(0, 100) * (c1.rating / c2.rating)
        if odd < 50:
            winner = c1
            loser = c2
        else:
            winner = c2
            loser = c1
        winner.update_wins(1)
        loser.update_losses(1)
        return {
            "winner": winner.id_name,
            "loser": loser.id_name,
            "winner_rating": winner.rating,
            "loser_rating": loser.rating
        }

    def get_leaderboard(self) -> list:
        pass

    def generate_tournament_report(self) -> dict:
        pass
