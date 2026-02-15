from ex3.GameStrategy import GameStrategy


class AggressiveStrategy(GameStrategy):
    """
    Docstring for AggressiveStrategy
    sort the hand by cost
    takes 2 cards max add to the cards played
    ret infos
    """
    def execute_turn(self, hand: list, battlefield: list) -> dict:
        sorted_hand = sorted(hand, key=lambda card: card.cost)
        cards_played = []
        mana_used = 0
        damage_dealt = 0
        for card in sorted_hand[:2]:
            cards_played.append(card.name)
            mana_used += card.cost
            damage_dealt += card.cost
        targets = self.prioritize_targets(["Enemy Player"])
        return {
            "cards_played": cards_played,
            "mana_used": mana_used,
            "targets_attacked": targets,
            "damage_dealt": damage_dealt
        }

    def get_strategy_name(self) -> str:
        return "AgressiveStrategy"

    def prioritize_targets(self, available_targets: list) -> list:
        return available_targets

# Prioritizes attacking and dealing damage
# • Plays low-cost creatures first for board presence
# • Targets enemy creatures and player directly
# • Returns comprehensive turn execution results
