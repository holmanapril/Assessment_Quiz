# Imports random
import random


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
                print()
                return response
            # If questions_amount it not one of the choices print please enter 10, 15 or 20
            else:
                print(error)
        except ValueError:
            print(error)


def ask_questions():
    # creates variables that counts the score and rounds
    score = 0
    amount_questions_asked = 1
    # Picks random number from 0, 44
    ask = random.randint(0, 44)
    # All my questions and answers
    questions = ["What animals are pearls found in?", "Google Chrome, Safari, Firefox, and Explorer are different types of what?",
                 "What other name does “corn” go by?", "What’s the primary ingredient in hummus?", "Which kind of alcohol is Russia is notoriously known for?",
                 "Which European nation was said to invent hot dogs?", "Which country is responsible for giving us pizza and pasta?",
                 "In which body part can you find the femur?", "What is your body’s largest organ?", "Which bone are babies born without?",
                 "Which element is said to keep bones strong?", "Which Avenger is the only one who could calm the Hulk down?", "Which continent is the largest?",
                 "What was the name of the rock band formed by Jimmy Page?", "What genre of music did Taylor Swift start in?", "The Hunger Games series was written by which author?",
                 "How many films did Sean Connery play James Bond in?", "How many Lord of the Rings films are there?", "Who played Wolverine?",
                 "When Michael Jordan played for the Chicago Bulls, how many NBA Championships did he win?", "How many presidents have been impeached?",
                 "World War I began with the death of Archduke Franz Ferdinand, of which country?", "What’s the scientific name of a wolf?",
                 "How many eyes does a bee have?", "How many hearts does an octopus have?", "What vehicle Volkswagen best known for in the world?", "What is the slogan of Apple Inc.?",
                 "In which year did World War I begin?", "Thor was the son of which God?", "How many cards are there in a deck of Uno?", "'Astro Boy' is what genre of a video game?",
                 "How many bags of wool did “Baa Baa Black Sheep” have?", "How many fish were used to feed the 5,000 along with the loaves?", "What is the Hebrew term for “commandment”?",
                 "What’s another name for a footrest?", "Broadway was established in what year in New York?", "What kind of food is Penne?", "How many permanent teeth does a dog have?",
                 "At which venue is the British Grand Prix held?", "Name the first actor to play Dumbledore in the Harry Potter films?", "What is the capital city of Australia?",
                 "Which animal can be seen on the Porsche logo?", "What is the common name for dried plums?", "Which original Avenger was not in the first few movies?",
                 "What is Hawkeye’s real name?"]
    answers = ["oysters", "web browsers", "maize", "chickpeas", "vodka", "germany", "italy", "leg", "skin", "knee cap", "calcium", "black widow",
               "asia", "led zeppelin", "country", "suzanne collins", "7", "3", "hugh Jackman", "6", "3", "austria", "canis lupus", "5", "3",
               "beetle", "think different", "1914", "odin", "108", "action", "3", "2", "mitzvah", "ottoman", "1750", "pasta", "42", "silverstone",
               "richard harris", "canberra", "horse", "prunes", "wasp", "clint barton"]
    # Loops questions until user has played the amount of questions they wanted to play
    while amount_questions_asked != question_amount:
        # Asks user a question
        response = input(questions[ask]).strip().lower()
        if response == answers[ask]:
            print()
            print("Correct")
            print()
            score += 1
            amount_questions_asked += 1
        else:
            print()
            print("Incorrect")
            print()
            print("The correct answer is {}".format(answers[ask].capitalize()))
            print()
            amount_questions_asked += 1

        questions.remove(questions[ask])
        answers.remove(answers[ask])
    # Prints score out
    print("Final Score = {}/{}".format(score, amount_questions_asked))
    print()
    print("Great Job!")


# Main Routine
question_amount = how_many_questions("How many questions would you like to play? 10, 15 or 20?", 10, 15, 20)
ask_questions()
