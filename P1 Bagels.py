import random

guesses = 10
word =""

def compare(word, guess):
    partlyCorrect = False
    for a in range(3):
        if guess[a] == word[a]:
            print("Fermi", end=" ")
            partlyCorrect = True
        elif guess[a] in word:
            print("Pico",  end=" ")
            partlyCorrect = True
    return partlyCorrect

def generate():
    global word
    word = str(random.randint(100, 999))

def guessingGame():
    global word
    counter = 0
    flag = True
    
    while (counter < guesses and flag):
        counter += 1
        guess = input("Guess #" + str(counter) + ": \n")
        if (guess == word):
            print("You got it!")
            flag = False
        elif not compare(word, guess):
            print("Bagels")
        else:
            print()


print("I am thinking of a 3-digit number. Try to guess what it is. \n Here are some clues: \n")
print("When I say:   That means: \n Pico   One digit is correct but in the wrong position. \n Fermi   One digit is correct and in the right position\n Bagels   No digit is correct.")
generate()
print("I have thought up a number. \n You have " + str(guesses) + " to get it. \n")

guessingGame()

if input("Do you want to play again? (y or n) ") == "y":
    generate()
    guessingGame()
else:
    print("Thank you for playing!")