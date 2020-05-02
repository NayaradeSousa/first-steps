""" Generating a value randomly, keeps that value, and gives
    the user five chances to guess the value generated.
"""
import random as rd


if __name__ == '__main__':
    while True:
        print("Would you like to guess the number I drew? [Y/N]")
        answer = input()
        if answer == "N" or answer == "n":
            print("Ok! We'll game later!")
            break
        else:
            drawn_number = rd.randint(1, 50)
            chance = 1
            print(" Ok! Let's game.\n I have drawn a whole number that is between 1 and 50. \n "
                  "You have 5 chances to guess.")
            while chance <= 5:
                print("Try ", chance, ":")
                bet = int(input())
                if bet == drawn_number:
                    print("YOU WIN! Congrats")
                    break
                elif bet != drawn_number and chance < 4:
                    chance += 1
                    print("Wrong number. Try again!")
                elif chance == 4:
                    chance += 1
                    print("This is your last chance")
                else:
                    print("You lost. The draw number was: ", drawn_number)
                    break
