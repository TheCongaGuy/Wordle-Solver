# Class to solve wordles
class WordleBot:
    # Initialize a wordle bot with a list of 5 letter words and a known letter dictionary:
    # Additionally, add a ranking system for each letter in the alphabet:
    def __init__(self, letters = 5):
        # Constant number of letters in a word
        WordleBot.letters = letters

        # List of english letters & followup dictionary to rank those letters
        self.letterList = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        self.letterRank = {}

        # List of usable 5 letter words
        self.wordList = []
        # List of all letters that have been tested
        self.triedLetters = []
        # List of letters that do not show (Black letters)
        self.notUsed = []
        # List of letters who's position is not known (Yellow letters)
        self.yellowLetters = []
        # Dictionary of letters who's position has been correctly identified (Green letters)
        self.knownLetters = {}

        # Access the words document
        wordsAddress = open("Words.txt")

        # For each line in the word document:
        for line in wordsAddress:
            # If the word is 5 letters long excluding the \n:
            if len(line) == letters + 1:
                # Append it to the word list, removing the \n
                self.wordList.append(line[:-1])

        # For each letter in the letter list:
        for letter in self.letterList:
            print(f'Ranking Letter "{letter}"')
            # Instantiate a count for how many times that letter is used and total letters
            rankLetterCount = 0
            allLetterCount = 0
            # For each word in the word list:
            for word in self.wordList:
                # For each letter in the word:
                for wLet in word:
                    # If the letter is equal to the current ranked letter; add to the counter
                    if letter == wLet:
                        rankLetterCount += 1
                    # Count the letter
                    allLetterCount += 1

            # Assign that letter to the dictionary with it's percentage ranking
            self.letterRank[letter] = rankLetterCount / allLetterCount

    # Print statement setup:
    def __repr__(self):
        return f'{len(self.wordList)} words remaining.'

        # For each letter in the letter list:
        for letter in self.letterList:
            # Instantiate a count for how many times that letter is used and total letters
            rankLetterCount = 0
            allLetterCount = 0
            # For each word in the word list:
            for word in self.wordList:
                # For each letter in the word:
                for wLet in word:
                    # If the letter is equal to the current ranked letter; add to the counter
                    if letter == wLet:
                        rankLetterCount += 1
                    # Count the letter
                    allLetterCount += 1

            # Assign that letter to the dictionary with it's percentage ranking
            self.letterRank[letter] = rankLetterCount / allLetterCount

    # Method to obtain a guess:
    def getGuesses(self):
        # Instantiate a grading system
        grades = {"" : -99999}

        # Instantiate a counter for items deleted
        deleted = 0

        # For each of the guesses:
        for guess in self.wordList:
            # Keep a new score
            score = 0
            # For each letter of the guess:
            for letter in guess:
                # If the guess contains a letter not used; remove the letter from guess list, and word list
                if letter in self.notUsed:
                    # To avoid error; check to see if the word is still in the word list
                    if guess in self.wordList:
                        self.wordList.remove(guess)
                        deleted += 1

                        if deleted % 1000 == 0:
                            print(f'{deleted} items removed...')
                    continue
                
                # If the guess contains a yellow letter; add 2 to it's score
                elif letter in self.yellowLetters:
                    score += 2 * self.letterRank[letter]

                # If the guess contains a green letter; add 1 to it's score
                elif letter in self.knownLetters:
                    if guess.index(letter) == self.knownLetters[letter]:
                        score += 1 * self.letterRank[letter]

                # If it is an unused letter, add a special calculation to its score
                else:
                    score += (WordleBot.letters - 2 - (1 / WordleBot.letters * len(self.yellowLetters)) - len(self.knownLetters) // 1) * self.letterRank[letter]

                # If there is more than one instance of this letter; subtract 1 point from it's score
                if guess.count(letter) > 1:
                    score -= 1

            # Add the guess, and it's score to the grading system
            grades[guess] = score

        # Instantiate the selected word
        selectedWord = ""

        # For each graded word:
        for word in grades.keys():
            # If this graded word is better than the next; select this word
            if grades[selectedWord] < grades[word]:
                selectedWord = word

        # Return the selected word
        return selectedWord

# Instantiate a wordle bot
wordleSolver = WordleBot()

# While the word has not been guessed:
while input("Has the wordle been solved? (y/n): ").lower() == "n":    
    # Get a guess
    guess = wordleSolver.getGuesses()

    # Print number of possible words
    print(wordleSolver)

    # Ask if wordle recognizes this word:
    while input(f'Does wordle recognize "{guess}"? (y/n): ').lower() == "n":
        # Remove the word and choose another if word was not recognized
        wordleSolver.wordList.remove(guess)
        guess = wordleSolver.getGuesses()

    # For each letter in the guess:
    for letter in guess:
        # If the letter has not been guessed before:
        if letter not in wordleSolver.triedLetters:
            wordleSolver.triedLetters.append(letter)
        result = input(f'What was the best result of the letter {letter} (g/y/b): ')
        # If the result was green; ask for the index
        if result.lower() == "g":
            if letter in wordleSolver.yellowLetters:
                wordleSolver.yellowLetters.remove(letter)
            index = int(input(f'What was the index of the green {letter} (1-{WordleBot.letters}): ')) - 1
            wordleSolver.knownLetters[letter] = index
            changed = True
            while changed:
                changed = False
                for word in wordleSolver.wordList:
                    if letter in word and word[index] != letter:
                        wordleSolver.wordList.remove(word)
                        changed = True

        if result.lower() == "y":
            index = int(input(f'What was the index of the yellow {letter} (1-{WordleBot.letters}): ')) - 1
            wordleSolver.yellowLetters.append(letter)
            # Remove all words that have that letter in that index
            changed = True
            while changed:
                changed = False
                for word in wordleSolver.wordList:
                    if word[index] == letter:
                        wordleSolver.wordList.remove(word)
                        changed = True

        if result.lower() == "b":
            wordleSolver.notUsed.append(letter)
    #wordleSolver.rankLetters()