# Function for yes_no
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
            print("Display Instructions")
            return played_before
        # If played_before = anything else print <error> please enter yes or no
        else:
            print("Please enter Yes or No")


# Main Routine
show_instructions = yes_no("Have you played before?")
