import random, time
fruits = ['pear', 'mango', 'apple', 'banana', 'apricot', 'pineapple', 'cantaloupe', 'grapefruit', 'jackfruit', 'papaya']
superHeroes = ['hawkeye', 'robin', 'Galactus', 'thor', 'mystique', 'superman', 'deadpool', 'vision', 'sandman', 'aquaman']
selection = ""
name = input("what is your name: ").title()
print(f"Hello, {name} let's start playing Hangman!")
time.sleep(1)
print("The objective of the game is to guess the secret word chosen by the computer.")
time.sleep(1)
print("You can guess only one letter at a time. Don't forget to press 'enter key' after each guess.")
time.sleep(2)
print("Let the fun begin!")
time.sleep(1)

def playGame(secretWord):
    #initialise variable
    global selection
    blankWord = ""
    guessedLetters = []
    for i in secretWord:
        blankWord += "_"
    guesses = len(secretWord) + 2
    #game loop
    while True:
        #check for end of game and end game loop
        if guesses <= 0:
            print (f"Too bad you lose, the word was {secretWord}")
            time.sleep(1)
            break
        elif blankWord == secretWord:
            print (f"Correct, {secretWord}, You win")
            time.sleep(1)
            break
        else:
            print (f"{name}, Your word is {blankWord} you have {guesses} left")
            #letter input validation loop
            while True:
                guess = input("Guess a letter: ").lower()
                if guess in guessedLetters:
                    print ("you already guessed this")
                #bonus marks for checking input is a single letter (and not any other character)
                elif not guess.isalpha():
                    print ("letters only please")
                elif len(guess) > 1:
                    print ("one at a time please")
                #if input valid add letter to guessed and exit validation loop
                else:
                    guessedLetters.append(guess)
                    break
        #update blank word if letter in word
        if guess in secretWord:
            for i in range(len(secretWord)):
                if secretWord[i] == guess:
                    blankWord = blankWord[:i] + guess + blankWord[i+1:]
        #if letter not in word subtract one guess
        else:
            guesses-=1
    #Reset menu selection so user can choose different category or exit
    selection = ""
#menu loop playGame function if correct selection or break loop to exit
while True:
    if selection == "F":
        playGame(random.choice(fruits))

    elif selection == "S":
        playGame(random.choice(superHeroes))
    elif selection == "X":
        print ("have a nice day")
        break
    else:
        selection = input (f"Hi, {name} type F for fruits, S for superheroes or X to exit: ").capitalize()




