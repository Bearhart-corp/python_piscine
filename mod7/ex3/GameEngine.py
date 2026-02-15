from ex3.CardFactory import CardFactory
from ex3.GameStrategy import GameStrategy


class GameEngine():
    def configure_engine(self, factory:
                         CardFactory, strategy: GameStrategy) -> None:
        self.factory = factory
        self.strategy = strategy
        self.turns_simulated = 0
        self.total_damage = 0
        self.cards_created = 0

    def simulate_turn(self) -> dict:
        """
        :create 3 cards
        :in hand add values
        :exec a turn
        :ret info
        """
        deck = self.factory.create_themed_deck(3)
        hand = list(deck.values())
        result = self.strategy.execute_turn(hand, [])
        self.turns_simulated += 1
        self.total_damage += result["damage_dealt"]
        self.cards_created += len(hand)
        return result

    def get_engine_status(self) -> dict:
        return {
            "turns_simulated": self.turns_simulated,
            "strategy_used": self.strategy.get_strategy_name(),
            "total_damage": self.total_damage,
            "cards_created": self.cards_created
        }
