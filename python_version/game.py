from typing import TypeAlias
from random import randint


MoveHint: TypeAlias = tuple[str, list[int]]


class Game:
    def __init__(self) -> None:
        self.number: str
        self.riddled_number: dict[str, int]
        self.moves: list[MoveHint]

        self.reset_game()

    def generate_number(self) -> str:
        nums = [i for i in range(10)]

        generated_num = ""

        for i in range(4):
            index = randint(0, len(nums)-1)
            generated_num += str(nums[index])
            nums.pop(index)

        return generated_num

    def reset_game(self) -> None:
        self.number = self.generate_number()
        self.riddled_number = {}
        self.moves = []

        for i, num in enumerate(self.number):
            self.riddled_number[num] = i

    def make_guess(self, guess: str) -> list[int]:
        # TODO: make error if guess contain other symbols
        if not guess.isdigit():
            return [0, 0]

        # TODO: make error if guess longer than number
        if len(guess) > len(self.number) or len(guess) < len(self.number):
            return [0, 0]

        bulls = 0
        cows = 0

        for i, g in enumerate(guess):
            if g in self.riddled_number:
                if self.riddled_number[g] == i:
                    bulls += 1
                else:
                    cows += 1

        self.moves.append((guess, [bulls, cows]))

        if bulls == 4:
            self.reset_game()

        return [bulls, cows]
