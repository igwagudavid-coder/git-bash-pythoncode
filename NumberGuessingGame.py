from random import randint
import guessingGameFunctions

def main():
    print(guessingGameFunctions.welcome_logo)
    number = randint(1, 100)


    attempts = guessingGameFunctions.pick_level()
    while attempts > 0:
        guess = int(input("\nWhat's your guess? :"))
        correctNumber = guessingGameFunctions.checkGuess(number , guess)

        if correctNumber:
            print(guessingGameFunctions.win_logo)
            break
        attempts -=1
        guessingGameFunctions.loseCheck(number , attempts)


if __name__ == "__main__":
    main()