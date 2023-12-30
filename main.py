from WordleSolverV2 import WordleBot

wordleSolver = WordleBot()

while input("Has the wordle been solved? (y/n): ").lower() == "n":
    guess = wordleSolver.getGuesses()

    # Print number of possible words
    print(wordleSolver)

    # Ask if wordle recognizes this word:
    while input(f'Does wordle recognize "{guess}"? (y/n): ').lower() == "n":
        # Remove the word and choose another if word was not recognized
        wordleSolver.removeGuess(guess)
        guess = wordleSolver.getGuesses()

    for index, letter in enumerate(guess):
        result = input(f'What was the best result of the letter {letter} (g/y/b): ')

        if result.lower() == "g":
            wordleSolver.greenLet(letter, index)

        if result.lower() == "y":
            wordleSolver.yellowLet(letter, index)

        if result.lower() == "b":
            wordleSolver.blackLet(letter, index)