import json
from random import randint
class GameFunctions:

    def __init__(self):
        with open("game_data.json", "r") as file:
            self.game_data= json.load(file)
        self.total_number= len(self.game_data)-1
        self.previous_indices =[]
        with open("logos.json", "r") as file:
            self.logos = json.load(file)

    def fetchData(self,a,b):
        if a not in self.previous_indices:
            self.previous_indices.append(a)
        if b not in self.previous_indices:
            self.previous_indices.append(b)

        guess_data = [self.game_data[a], self.game_data[b]]

        return guess_data



    def guessChecker(self, slot_a , slot_b, guess)-> int|bool:

        match guess:
            case "1" | ">"|"a":
                print(self.logos[1])
                if slot_a["followers"] > slot_b["followers"]:

                    return 1
                else:
                    return False

            case "2" | "<"|"b":
                print(self.logos[2])
                if slot_a["followers"] < slot_b["followers"]:

                    return 2
                else:
                     return False

            case "3" | "=":
                if slot_a["followers"] == slot_b["followers"]:
                    return 3
                else:
                    return False
            case _:
                raise ValueError("Wrong input entered!")




    def nextNumberGenerator(self, a,b , g_num):
        if len(self.previous_indices) >= self.total_number:
            raise IndexError("All 200 items have been used in this game session!")
        match g_num:
            case 1 | 3:

                new_a = a
            case 2:

                new_a = b
            case _:
                raise ValueError("Error in program, Shutting down!")


        new_b = randint(0, self.total_number)
        while new_b == new_a or new_b in self.previous_indices:
            new_b = randint(0, self.total_number)

        return [new_a, new_b]


    def gameEnd(self, score):
        if score== 0:
            print(self.logos[-1])

    def dataChecker(self, choice):
        checks =0
        for i in range(5):
            if choice.lower() == "yes" or choice.lower() == "y":
                index = int(input(f"What number account would you want to see (you have a maximum of {5-checks} accounts)? "))
                data = self.game_data[index]
                print(f"Name: {data["name"]}"
                      f"\nProfession: {data["profession"]}"
                      f"\nCountry: {data["country"]}"
                      f"\nFollowers: {data['followers']}"
                      )
                checks +=1
            else:
                break

            if checks <5:
                choice = input("Would you like to check another one (Y/N)? ")

