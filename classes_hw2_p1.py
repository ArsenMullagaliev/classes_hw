import random
from abc import ABC, abstractmethod


class AnimeMon(ABC):

    @classmethod
    @abstractmethod
    def inc_exp(self, value: int):
        return None

    @property
    @abstractmethod
    def exp(self):
        pass


class BasePokemon(AnimeMon):

    def __init__(self, name: str, poketype: str, exp: int = 0):
        self.name = name
        self.poketype = poketype
        self._exp = exp

    def __str__(self) -> str:
        return f'{self.name}/{self.poketype}'

    def inc_exp(self, value: int) -> None:
        self._exp += value
        return None

    @property
    def exp(self) -> int:
        return self._exp


class EmojiMixin:
    emoji_dict = {
        'grass': '🌿',
        'fire': '🔥',
        'water': '🌊',
        'electric': '⚡',
    }

    def __str__(self) -> str:
        return f'{self.name}/{self.emoji_dict[self.poketype]}'


class Pokemon(EmojiMixin, BasePokemon):
    def __init__(self, name: str, poketype: str, exp: int = 0):
        super().__init__(name=name, poketype=poketype, exp=exp)


class Digimon(AnimeMon):

    def __init__(self, name: str, exp: int = 0):
        self.name = name
        self._exp = exp

    def inc_exp(self, value: int):
        self._exp += value

    @property
    def exp(self):
        return self._exp


def train(animemon: AnimeMon):
    step_size, level_size = 10, 100
    sparring_qty = (level_size - animemon.exp % level_size) // step_size
    for i in range(sparring_qty):
        win = random.choice([True, False])
        if win:
            animemon.inc_exp(step_size)


if __name__ == '__main__':

    bulbasaur = Pokemon(name='Bulbasaur', poketype='grass')
    train(bulbasaur)
    print(f'{bulbasaur.name} has {bulbasaur.exp} experience.')
    agumon = Digimon(name='Agumon')
    train(agumon)
    print(f'{agumon.name} has {agumon.exp} experience.')
