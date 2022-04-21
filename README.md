# Wordle-Solver
This project is in response to NYT adding double letters to Wordle. Written in Python 3.6 in my freetime, this class can be added to a project with the given word list text file or a custom word list text file to predict games of wordle.
## Instalation
To use in your program,
1. Place the Wordle_Solver.py file into your project and use it as a namespace. Alternatively, you may just use WordleBot from Wordle_Solver. `import Wordle_Solver` or `from Wordle_Solver import WordleBot`
2. Place the .txt file from ZippedWords.zip into your project so that the Wordle_Solver may access it for reference when creating a list of words. If you wish to use your own text file, name your text file *Words.txt*.
3. Instantiate a Wordle Bot in your main method with an optional integer for length. The default length of a word is 5 letters, as is the standard in Wordle.
`solver = Wordle_Solver.WordleBot()`
## Methods
There are several methods attached to this Wordle Solver, meaning that this class alone cannot solve a Wordle. However because of this, you can fine tune your program.

- `print(solver)`  Print statement will print the number of possible words remaining.
- `solver.removeGuess(word)`  Method removes a word from the Wordle Solver's list of words
- `solver.blackLet(character)`  Method will take a character and add it to the Wordle Solver's list of non-usable characters.
- `solver.yellowLet(character)`  Method will ask the user for the index of the yellow character given, and remove any impossible words.
- `solver.greenLet(character)`  Method will ask the user for the index of the green character given, and remove any impossible words.
- `solver.getGuesses()`  Method will cycle through its list of words and grade them based on probability of success. It will then **return** the best word in its list as a string.
## Program Example
      from Wordle_Solver import WordleBot

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

          for letter in guess:
              result = input(f'What was the best result of the letter {letter} (g/y/b): ')

              if result.lower() == "g":
                  wordleSolver.greenLet(letter)

              if result.lower() == "y":
                  wordleSolver.yellowLet(letter)

              if result.lower() == "b":
                  wordleSolver.blackLet(letter)
