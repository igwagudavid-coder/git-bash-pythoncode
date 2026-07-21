def pick_level():
    pick = input("Pick a level, easy or hard : ")
    if pick == "easy":
        tries= 10
        print("Guess a number between 1 and 100!")
        print(f"\n\nYou have {tries} tries!")
        return tries

    elif pick == "hard":
        tries =5
        print("Guess a number between 1 and 100!")
        print(f"\n\nYou have {tries} tries!")
        return tries

    else: print("\nWrong input!")


def checkGuess(number,guess)-> bool:
    if guess == number:
        return True
    elif   guess > number:
        print("\nToo high, guess again")
        return False
    elif guess < number:
        print("\nToo low, guess again")
        return False


def loseCheck(number, attempts):
    if attempts>0 :
        print(f"\nYou have {attempts} guesses left! ")
    else:
        print("\n\nYou lose!!!")
        print(f"\nThe number was {number}")
        print(lose_logo)


win_logo = r"""
                                                                      .           
                                                                    .o8           
     .ooooo.   .ooooo.  ooo. .oo.    .oooooooo oooo d8b  .oooo.   .o888oo  .oooo.o
    d88' `"Y8 d88' `88b `888P"Y88b  888' `88b  `888""8P `P  )88b    888   d88(  "8
    888       888   888  888   888  888   888   888      .oP"888    888   `"Y88b. 
    888   .o8 888   888  888   888  `88bod8P'   888     d8(  888    888 . o.  )88b
    `Y8bod8P' `Y8bod8P' o888o o888o `8oooooo.  d888b    `Y888""8o   "888" 8""888P'
                                    d"     YD                                     
                                    "Y88888P'                                     
    """


lose_logo = r"""
oooo                                                          .o. .o. .o.
`888                                                          888 888 888
 888   .ooooo.   .oooo.o  .ooooo.  oooo d8b oooo d8b oooo d8b 888 888 888
 888  d88' `88b d88(  "8 d88' `88b `888""8P `888""8P `888""8P Y8P Y8P Y8P
 888  888   888 `"Y88b.  888ooo888  888      888      888     `8' `8' `8'
 888  888   888 o.  )88b 888    .o  888      888      888     .o. .o. .o.
o888o `Y8bod8P' 8""888P' `Y8bod8P' d888b    d888b    d888b    Y8P Y8P Y8P
"""


welcome_logo = r"""
__        __   _                            _ _ _ 
\ \      / /__| | ___ ___  _ __ ___   ___  | | | |
 \ \ /\ / / _ \ |/ __/ _ \| '_ ` _ \ / _ \ | | | |
  \ V  V /  __/ | (_| (_) | | | | | |  __/ |_|_|_|
   \_/\_/ \___|_|\___\___/|_| |_| |_|\___| (_|_|_)
"""