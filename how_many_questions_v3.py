# error statement for whenever the user enters an invalid input
error = "Please enter 10, 15 or 20"
# Loop
valid = False
while not valid:
    # Check if input entered is valid
    try:
        # Ask how many rounds user wants to play
        question_amount = int(input("How many questions would you like to play? 10, 15 or 20?"))
        # If questions_amount is equal to 10, 15 or 20 it print it
        if question_amount == 10 or question_amount == 15 or question_amount == 20:
            print("You chose to play {} rounds".format(question_amount))
            valid = True
        # If questions_amount it not one of the choices print please enter 10, 15 or 20
        else:
            print(error)
    except ValueError:
        print(error)
