import game

BaC = game.Game()
print()

answer = [0, 0]
while answer[0] != 4:
    guess = input()

    answer = BaC.make_guess(guess)

    print(f'B: {answer[0]}\tC: {answer[1]}')

pritn("You win!")
