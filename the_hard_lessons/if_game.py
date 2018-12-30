
from sys import exit




def saibaba():
    print('He has been known to have a health challenge requiring him to jet abroad regularly for treatment')
    print("He has been known for lopsided appointments")
    print("He has been known to give people responsibility without accountability")
    print("He is a laisiz fair leader,wanting to please all political jugganut")
    print("His body language tells investors to stay claer,joblessness increases")
    print('By what margin do you think he will win ?')

    choice = input("> ")
    how_much = int(choice)

    if how_much < 50:
        print("You are reasonble")
        exit(0)

    else:
        indecisive("Is he that popular,be realistic")












def atikulated():
    print("He was a former customs officer")
    print("He is allege to be corrupt but  all cases against him in the law court has been thrown out")
    print("He is known to a shrewed business man with a sharp negotiation skills")
    print("He has been known to manage human and material resources to achieve set objective and goals")
    print("a prosperious and unified country or a bankrupt country")

    prosperious_and_unified_country = False

    while True:
        choice = input("> ")
        if choice == "He's corrupt":
            indecisive("He has not been pronounced guilty by any court of competent jurisdiction")
        if choice == "I'm atikulated" and not prosperious_and_unified_country:
            print("He becomes the president")
            print("A new chapter of prosperity opens before you!")
            prosperious_and_unified_country = True

        if choice == "I'm atikulated" and prosperious_and_unified_country:
            indecisive("Power is with the electorate, if you reneged on your promises, we shall vote you out accordinly")
        if choice == 'dissapointed' and prosperious_and_unified_country:
            saibaba()
        else:
            print("I dont understand that decision")




def fresh_start():
    print("You have made the most idealistic choice")
    print("This is our first taste at power, this need some getting use to!")
    print("Would be [p]patient be patient with us as we put effort to solving our tough issue or you will [j] jump ship")



    choice = input("> ")

    if 'patience' in choice:
        start()
    elif 'jump' in choice:
        indecisive("It's unfortunates")
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
