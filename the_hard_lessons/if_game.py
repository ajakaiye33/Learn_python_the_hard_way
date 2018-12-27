
from sys import exit


































def fresh_start():
    print("You have made the most idealistic choice")
    print("This is our first taste at power, this need some getting use to!")
    print("Would be [p]patient be patient with us as we put effort to solving our tough issue or you will [j] jump ship")



    choice = input("> ")

    if 'patience' in choice:
        start()
    elif 'jump' in choice:
        indecisive()
    else:
        fresh_start()








def indecisive(curse):
    print(curse, "You have lost your voice")
    exit(0)





def start():
    print("You have just collected your permanent voters card")
    print("Before you are three choices for who you want to vote as the next president")
    print("would it be [A] Atiku ?")
    print("would it be [B] Buhari ?")
    print("would it be [C]the third force consensus candidate ?")


    choice = input("  >")

    if choice == 'A':
        atikulated()
    elif choice == 'B':
        saibaba()
    elif choice == 'C':
        fresh_start()
    else:
        indecisive("You don't deserve to be a citizen, you have failed to excercise your right.")



start()
