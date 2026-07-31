from data import game_data
from random import randint
class GameFunctions:
    total_number = len(game_data) -1
    def __init__(self):
        self.total_number= len(game_data)-1
        self.previous_indices =[]
    def fetchData(self,a,b):
        if a not in self.previous_indices:
            self.previous_indices.append(a)
        if b not in self.previous_indices:
            self.previous_indices.append(b)

        guess_data = [game_data[a], game_data[b]]

        return guess_data



    def guessChecker(self, slot_a , slot_b, guess)-> int|bool:

        match guess:
            case "1" | ">"|"a":
                if slot_a["followers"] > slot_b["followers"]:
                    return 1
                else:
                    return False

            case "2" | "<"|"b":
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
                print("Wrong input entered!")
                return False



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


