# Imports random
import random


def ask_questions():
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
             "How many eyes does a bee have?", "How many hearts does an octopus have?", "What vehicle Volkswagen best known for in the world?",
             "What is the slogan of Apple Inc.?", "How long is an Olympic swimming pool (in meters)?", "Thor was the son of which God?", "What geometric shape is generally used for stop signs?",
             "'Astro Boy' is what genre of a video game?", "How many bags of wool did “Baa Baa Black Sheep” have?", "How many fish were used to feed the 5,000 along with the loaves?",
             "What is the Hebrew term for “commandment”?", "What’s another name for a footrest?", "What is the name of the biggest technology company in South Korea?",
             "What kind of food is Penne?", "What is the most consumed manufactured drink in the world?", "At which venue is the British Grand Prix held?",
             "Name the first actor to play Dumbledore in the Harry Potter films?", "What is the capital city of Australia?", "Which animal can be seen on the Porsche logo?",
             "What is the common name for dried plums?", "Which original Avenger was not in the first few movies?", "What is Hawkeye’s real name?"]
    answers = ["oysters", "web browsers", "maize", "chickpeas", "vodka", "germany", "italy", "leg", "skin", "knee cap", "calcium", "black widow",
           "asia", "led zeppelin", "country", "suzanne collins", "seven", "three", "hugh jackman", "six", "three", "austria", "canis lupus", "five", "three",
           "beetle", "think different", "fifty", "odin", "octagon", "action", "three", "two", "mitzvah", "ottoman", "samsung", "pasta", "tea", "silverstone",
           "richard harris", "canberra", "horse", "prunes", "wasp", "clint barton"]
    # Asks user a question
    response = input(questions[ask]).strip().lower()
    if response == answers[ask]:
        print("Correct")
    else:
        print("Incorrect")
        print()
        print("The correct answer is {}".format(answers[ask].capitalize()))


# Main Routine
ask_questions()
