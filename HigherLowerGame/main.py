from random import randint
from GameFunctions import GameFunctions


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
        guess = input(f"A. \n"
                      f"Name: {slot_a["name"]}"
                      f"\nProfession: {slot_a["profession"]}"
                      f"\nCountry: {slot_a["country"]}\n"
                      f"\nand B.\n"
                      f"Name: {slot_b["name"]}"
                      f"\nProfession: {slot_b["profession"]}"
                      f"\nCountry: {slot_b["country"]}\n"
                        f"\n\n Is A: \n1. {game.logos[1]} \n2. {game.logos[2]} \nor 3. = : ")

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