# Functions
def yes_no(question):
    valid = False
    while not valid:
        played_before = input(question).strip().lower()
        # If played_before = yes print Program Continues
        if played_before == "yes" or played_before == "y":
            print("Program Continues")
            return played_before
        # If played_before = no print Display Instructions
        elif played_before == "no" or played_before == "n":
            instructions()
            return played_before
        # If played_before = anything else print <error> please enter yes or no
        else:
            print("Please enter Yes or No")


def instructions():
    print("                  *** How to play ***")
    print()
    print("Choose the amount of questions you would like play with(10, 15 or 20)")
    print()
    print("Answer the questions as well as you can, press enter once you have answered")
    print()
    print("Once you have answered as many questions as you asked to play your score will be shown")
    print()
    print("              *** Tips and Information ***")
    print()
    print("When answering questions do not use 'the' before any of your answers, this will make your answers wrong")
    print()
    print("Pay very close attention to your spelling, if your spelling is incorrect you will get it wrong")
    print()


# Main Routine
show_instructions = yes_no("Have you played before?")
start = input("Press <Enter> to start").lower()
