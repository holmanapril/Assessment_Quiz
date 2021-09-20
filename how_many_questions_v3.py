error = "Please enter 10, 15 or 20"

valid = False
while not valid:
    try:
        # Ask question
        question_amount = int(input("How much would you like to play with? "))
        if question_amount == 10 or question_amount == 15 or question_amount == 20:
            print("You chose to play {} rounds".format(question_amount))
            valid = True
        else:
            print(error)
    except ValueError:
        print(error)
