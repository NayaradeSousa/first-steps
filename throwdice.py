""" Generate a random value between a range that the user defines
    and also allows the user to run the script as many times as he wants.
    """
import random as rd

if __name__ == '__main__':
    while True:
        print("Do you want throw dice?[Y/N]")
        answer = input()
        if answer == "N" or answer == "n":
            print("Ok! We'll game later!")
            break
        else:
            print(" Ok! Let's game.\n Choose the number of faces of your dice: ")
            num = int(input())
            dice = rd.randint(1, num + 1)
            print("The number drawn was: ", dice)