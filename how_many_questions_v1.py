# Asks how many questions user would like to play
question_amount = int(input("How many questions would you like to play? 10, 15 or 20?"))
# If questions_amount is equal to 10, 15 or 20 it print it
if question_amount == 10 or question_amount == 15 or question_amount == 20:
    print("You chose {} rounds".format(question_amount))
# If questions_amount it not one of the choices print please enter 10, 15 or 20
else:
    print("Please enter 10, 15 or 20")
