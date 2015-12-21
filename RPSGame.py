import random


def menu():
    
    print "Choose one of three options."
    print "'0' for rock."
    print "'1' for paper."
    print "'2' for scissors."

    choice = raw_input("Your throw: ")
    if choice == '':
        choice = '0'

    return int(choice)

def compThrow(low,high):

    cThrow = random.randint(low,high)
    return cThrow

def printMessage(side, selection):
    if side == "U":
        user = "Player "
    elif side == "C":
        user = "Computer "
    else:
        user = "Unknown "

    if selection == 0:
        item = " Rock"
    elif selection == 1:
        item = " Paper"
    elif selection == 2:
        item = " Scissors"
    else:
        item = " Unknown"

    print user, "selected", item


print "Welcome to the Rock, Paper, Scissors Game!"

while(1):
    
    userSelection = menu()
    
    if userSelection not in (0,1,2):
        print "Invalid Choice."
    else:
        compSelect = compThrow(0,2)
        printMessage("U", userSelection)
        printMessage("C", compSelect)

        if userSelection == compSelect:
            print "Tie."
        else:
            if userSelection == 0 and compSelect == 1:
                print "Computer won."
            elif userSelection == 0 and compSelect == 2:
                print "You won."
            elif userSelection == 1 and compSelect == 0:
                print "You won."
            elif userSelection == 1 and compSelect == 2:
                print "Computer won."
            elif userSelection == 2 and compSelect == 0:
                print "Computer won."
            elif userSelection == 2 and compSelect == 1:
                print "You won."


    playAgain = raw_input("Would you like to play again (Y/N)?").upper()
    if playAgain == "N":
        break


