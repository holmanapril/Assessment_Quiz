# Functions
def how_many_questions(question, choice_1, choice_2, choice_3):
    error = "Please enter 10, 15 or 20"

    valid = False
    while not valid:
        try:
            # Ask question
            response = int(input(question))
            if response == choice_1 or response == choice_2 or response == choice_3:
                print("You chose to play {} rounds".format(response))
                valid = True
            else:
                print(error)
        except ValueError:
            print(error)


# Main Routine
question_amount = how_many_questions("How many questions would you like to play? 10, 15 or 20?", 10, 15, 20)
