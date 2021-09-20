# Functions
def how_many_questions(question, choice_1, choice_2, choice_3):
    # error statement for whenever the user enters an invalid input
    error = "Please enter 10, 15 or 20"
    # Loop
    valid = False
    while not valid:
        # Check if input entered is valid
        try:
            # Ask how many rounds user wants to play
            response = int(input(question))
            # If questions_amount is equal to 10, 15 or 20 it print it
            if response == choice_1 or response == choice_2 or response == choice_3:
                print("You chose to play {} rounds".format(response))
                return response
            # If questions_amount it not one of the choices print please enter 10, 15 or 20
            else:
                print(error)
        except ValueError:
            print(error)


# Main Routine
question_amount = how_many_questions("How many questions would you like to play? 10, 15 or 20?", 10, 15, 20)
