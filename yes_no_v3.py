loop = ""
while loop.lower() != "xxx":
    # Ask user if they have played before
    played_before = input("Have you done this quiz before?").strip().lower()
    # If played_before = yes print Program Continues
    if played_before == "yes" or played_before == "y":
        print("Program Continues")
    # If played_before = no print Display Instructions
    elif played_before == "no" or played_before == "n":
        print("Display Instructions")
    # If played_before = anything else print <error> please enter yes or no
    else:
        print("Please enter Yes or No")
