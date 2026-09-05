from random import randint
from GameFunctions import GameFunctions
from formatter import accountFormatter

def main():
    game = GameFunctions()
    print(game.logos[0])
    num = game.total_number
    score =0
    a = randint(0,num)
    b = randint(0,num)
    while a==b:
        b = randint(0,num)



    while True:

        data = game.fetchData(a,b)
        slot_a = data[0]
        slot_b = data[1]
        print("--------A--------")
        accountFormatter(slot_a)
        print("--------B--------")
        accountFormatter(slot_b)
        guess = input("is A: 1. higher(>),  2. lower(<), 3.Equal(=) ")
        greater_number = game.guessChecker( slot_a, slot_b, guess)

        if greater_number:
            print(game.logos[3])
            score +=1
            new_numbers =game.nextNumberGenerator(a,b,greater_number)
            a = new_numbers[0]
            b = new_numbers[1]
        else:
            print(game.logos[4])

            print(f"You had {score} guesses right!")
            game.gameEnd(score)
            break
    choice = input("Would you like to  check some follower data (Y/N)? ")
    game.dataChecker( choice)




if __name__ =="__main__":
    main()