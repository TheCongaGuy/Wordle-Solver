# New Class to solve Wordle problems
class WordleBot:
    def __init__(self):
        # Data members
        self.rankedLetters = {}
        self.wordList = []
        self.totalConfidence = 1

        # Open the Dictionary file and extract all 5 letter words
        wordFile = open("Words.txt")
        self.wordList = [word[:-1] for word in wordFile if len(word) == 6]
        wordFile.close()

        self.__rankLetters()
    
    # Print Statement Setup
    def __repr__(self):
        return f'{len(self.wordList)} words remaining.'

    # Get's the next most likely word in it's word list
    def getGuesses(self):
        bestWord = ""
        bestScore = -1

        for word in self.wordList:
            currentScore = 0
            for letter in word:
                # Add a bonus if the letter is unique
                if word.count(letter) == 1:
                    currentScore += self.rankedLetters[letter]
                
                currentScore += self.rankedLetters[letter]
            
            if currentScore > bestScore:
                bestWord = word
                bestScore = currentScore

        return bestWord

    def removeGuess(self, word):
        self.wordList.remove(word)
        self.__rankLetters()

    # Remove all words that do not have the passed letter in the specified index
    def greenLet(self, letter, index):
        # A while loop must be used here because the iterator in a for each loop is shifted
        # each time a word is deleted
        i = 0
        while i < len(self.wordList):
            word = self.wordList[i]
            if word[index] != letter:
                self.wordList.remove(word)
            else:
                i += 1
        
        self.__rankLetters()

    # Remove all words that do not have the specified letter, and have the letter in the specified index
    def yellowLet(self, letter, index):
        i = 0
        while i < len(self.wordList):
            word = self.wordList[i]
            if word[index] == letter or letter not in word:
                self.wordList.remove(word)
            else:
                i += 1
        
        self.__rankLetters()

    # Remove all words containing this letter
    def blackLet(self, letter, index):
        # Check if the letter appears in the word
        if input(f'Does "{letter}" appear in the word? (y/n): ').lower() == "n":
            i = 0
            while i < len(self.wordList):
                word = self.wordList[i]
                if letter in word:
                    self.wordList.remove(word)
                else:
                    i += 1
        
        else:
            i = 0
            while i < len(self.wordList):
                word = self.wordList[i]
                if word[index] == letter:
                    self.wordList.remove(word)
                else:
                    i += 1
        
        self.__rankLetters()

    # Helper Method ranks all letters by how often they appear
    def __rankLetters(self):
        # Clear previous ranking
        self.rankedLetters.clear()
        self.totalConfidence = 0

        # Count the number of times each letter appears
        for word in self.wordList:
            for letter in word:
                self.rankedLetters[letter] = self.rankedLetters.get(letter, 0) + 1
                self.totalConfidence += 1