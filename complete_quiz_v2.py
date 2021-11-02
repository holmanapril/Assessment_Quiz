# Imports random
import random


# Functions
def yes_no(question):
    valid = False
    while not valid:
        played_before = input(question).strip().lower()
        # If played_before = yes print Program Continues
        if played_before == "yes" or played_before == "y":
            return played_before
        # If played_before = no print Display Instructions
        elif played_before == "no" or played_before == "n":
            instructions()
            return played_before
        # If played_before = anything else print <error> please enter yes or no
        else:
            print("Please enter Yes or No")


def instructions():
    print()
    print("*** How to play ***")
    print()
    print("Choose the amount of questions you would like play with(10, 15 or 20)")
    print("Answer the questions as well as you can, press enter once you have answered")
    print("Once you have answered as many questions as you asked to play your score will be shown")
    print()
    print("*** Tips and Information ***")
    print()
    print("When answering questions do not use 'the' before any of your answers, this will make your answers wrong")
    print("Pay very close attention to your spelling, if your spelling is incorrect you will get it wrong")
    print("When writing name answers use the persons full name")
    print("Capital letters do not matter")
    print()


def how_many_questions(question, choice_1, choice_2, choice_3, choice_4):
    # error statement for whenever the user enters an invalid input
    error = "Please enter 10, 15, 20 or 30"
    # Loop
    valid = False
    while not valid:
        # Check if input entered is valid
        try:
            # Ask how many rounds user wants to play
            response = int(input(question))
            # If questions_amount is equal to 10, 15 or 20 it print it
            if response == choice_1 or response == choice_2 or response == choice_3 or response == choice_4:
                print("You chose to play {} rounds".format(response))
                print()
                return response
            # If questions_amount it not one of the choices print please enter 10, 15, 20 or 30
            else:
                print(error)
        except ValueError:
            print(error)


def ask_questions():
    # creates variables that counts the score and rounds
    score = 0
    amount_questions_asked = 1
    # All my questions and answers
    questions = ["What other name does “corn” go by?",
                 "Which kind of alcohol is Russia is notoriously known for?",
                 "Which European nation was said to invent hot dogs?",
                 "Which country is responsible for giving us pizza and pasta?",
                 "What is your body’s largest organ?",
                 "Which bone are babies born without?",
                 "Which element is said to keep bones strong?",
                 "Which Avenger is the only one who could calm the Hulk down?",
                 "Which continent is the largest?",
                 "What was the name of the rock band formed by Jimmy Page?",
                 "What genre of music did Taylor Swift start in?",
                 "The Hunger Games series was written by which author?",
                 "How many films did Sean Connery play James Bond in?",
                 "How many Lord of the Rings films are there?",
                 "Who played Wolverine?",
                 "When Michael Jordan played for the Chicago Bulls, how many NBA Championships did he win?",
                 "How many presidents have been impeached?",
                 "World War I began with the death of Archduke Franz Ferdinand, of which country?",
                 "What’s the scientific name of a wolf?",
                 "How many eyes does a bee have?",
                 "How many hearts does an octopus have?",
                 "What vehicle Volkswagen best known for in the world?",
                 "What is the slogan of Apple Inc.?",
                 "In which year did World War I begin?",
                 "Thor was the son of which God?",
                 "How many cards are there in a deck of Uno?",
                 "'Astro Boy' is what genre of a video game?",
                 "How many bags of wool did “Baa Baa Black Sheep” have?",
                 "How many fish were used to feed the 5,000 along with the loaves?",
                 "What is the Hebrew term for “commandment”?",
                 "What’s another name for a footrest?",
                 "Broadway was established in what year in New York?",
                 "What kind of food is Penne?",
                 "How many permanent teeth does a dog have?",
                 "At which venue is the British Grand Prix held?",
                 "Name the first actor to play Dumbledore in the Harry Potter films?",
                 "What is the capital city of Australia?",
                 "Which animal can be seen on the Porsche logo?",
                 "Which original Avenger was not in the first few movies?",
                 "What is Hawkeye’s real name?",
                 "Which Disney Princess has the least amount of screen time?",
                 "In Harry Potter, where does Vernon Dursley work?",
                 "How many letter tiles are there in a game of Scrabble?",
                 "Who designed the Eiffel Tower(full name)?",
                 "Name the longest river in the UK(Do not add river to answer)",
                 "Which English city was once known as Duroliponte?",
                 "What year did Vincent Van Gogh die?",
                 "What is Joe Biden's middle name?",
                 "What is the Olympic sport in which athletes cross the finish line backwards?",
                 "What is the lowest of the Prime numbers?",
                 "How many black and white squares are there on a chess board in total?",
                 "Brazil is the world’s largest exporter of which product?",
                 "Which planet is the hottest planet in our solar system?",
                 "What does the word ‘blitz’ translate to in German?",
                 "Which country is the natural habitat of the emu?",
                 "What is the metal that gives its name to a 70th wedding anniversary?",
                 "Which fast-food company piloted a chicken-flavored nail polish?",
                 "Name the well-known island country known for its three Rs: reggae, romance, and running.",
                 "In which Asian city can you find the historic waterfront called The Bund?",
                 "What is the world’s oldest and currently inhabited city?",
                 "Where can you find the traditionally Juniper-flavored beer called Sahti?",
                 "How many legs does a lobster have?",
                 "What is the largest moon of Saturn called?",
                 "What is Cher's last name?",
                 "What’s the maximum score you can achieve in 10-pin bowling?",
                 "What musical term is indicates a chord where the notes are played one after another rather than all together?",
                 "What color does gold leaf appear if you hold it up to the light?",
                 "Which gas is formed when a hydrogen bomb is detonated?",
                 "What's The Capital Of Paraguay?",
                 "Who Allegedly Wrote The Song “Golden Years” For Elvis Presley But Ended Up Recording It Himself?"]
    answers = ["maize",
               "vodka",
               "germany",
               "italy",
               "skin",
               "knee cap",
               "calcium",
               "black widow",
               "asia",
               "led zeppelin",
               "country",
               "suzanne collins",
               "7",
               "3",
               "hugh jackman",
               "6",
               "3",
               "austria",
               "canis lupus",
               "5",
               "3",
               "beetle",
               "think different",
               "1914",
               "odin",
               "108",
               "action",
               "3",
               "2",
               "mitzvah",
               "ottoman",
               "1750",
               "pasta",
               "42",
               "silverstone",
               "richard harris",
               "canberra",
               "horse",
               "wasp",
               "clint barton",
               "aurora",
               "grunnings",
               "100",
               "gustave eiffel",
               "severn",
               "cambridge",
               "1890",
               "robinette",
               "rowing",
               "2",
               "64",
               "coffee",
               "venus",
               "lightning",
               "australia",
               "platinum",
               "kfc",
               "jamaica",
               "shanghai",
               "damascus",
               "finland",
               "10",
               "titan",
               "sarkisian",
               "300",
               "arpeggio",
               "green",
               "helium",
               "asuncion",
               "david bowie"]

    # Loops questions until user has played the amount of questions they wanted to play
    while amount_questions_asked != question_amount + 1:
        print("Question {}:".format(amount_questions_asked))
        ask = random.randint(0, len(questions)-1)
        response = input(questions[ask]).strip().lower()
        if response == answers[ask]:
            print()
            decoration("Correct", "*")
            print()
            score += 1
            amount_questions_asked += 1
        else:
            # Says incorrect and says what the answer is
            print()
            decoration("Incorrect", "-")
            print()
            print("The correct answer is {}".format(answers[ask].title()))
            print()
            amount_questions_asked += 1

        # Removes questions asked
        questions.pop(ask)
        answers.pop(ask)
    # Prints score out
    print("Final Score = {}/{}".format(score, amount_questions_asked - 1))
    print()
    print("Great Job!")


def decoration(greeting, symbol):
    sides = symbol
    greeting = "{} {} {}".format(sides, greeting, sides)
    top_bottom = symbol * len(greeting)

    print(top_bottom)
    print(greeting)
    print(top_bottom)


# Main Routine
decoration("Welcome to my General Knowledge Quiz", "*")
show_instructions = yes_no("Have you played before?")
question_amount = how_many_questions("How many questions would you like to play? 10, 15, 20 or 30?", 10, 15, 20, 30)
start = input("Press <Enter> to start").lower()
ask_questions()
