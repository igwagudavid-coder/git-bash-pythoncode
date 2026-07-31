from random import randint
from GameFunctions import GameFunctions


def main():
    num = GameFunctions.total_number
    score =0
    a = randint(0,num)
    b = randint(0,num)
    while a==b:
        b = randint(0,num)

    func = GameFunctions()

    while True:

        data = GameFunctions.fetchData(func,a,b)
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
                        f"\n\n Is A. 1. > 2. < or 3. = ")

        greater_number =GameFunctions.guessChecker(func,slot_a, slot_b,guess)
        if greater_number:
            score +=1
            new_numbers =GameFunctions.nextNumberGenerator(func,a,b,greater_number)
            a = new_numbers[0]
            b = new_numbers[1]
        else:
            break


    print(f"You had {score} guesses right!")


if __name__ =="__main__":
    main()