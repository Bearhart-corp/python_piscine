from typing import Any, List, Dict, Union, Protocol   # noqa
from abc import ABC, abstractmethod


class Card(ABC):
    def __init__(self, name: str, cost: int, rarity: str) -> None:
        self.name = name
        self.cost = cost
        self.rarity = rarity

    @abstractmethod
    def play(self, game_state: dict) -> dict:
        return game_state

    def get_card_info(self) -> dict:
        dico = {}
        for elem in self:
            dico.append(elem)
        return dico

    def is_playable(self, available_mana: int) -> bool:
        available_mana -= self.cost
        return (available_mana > 0)
