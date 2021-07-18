from requests import get
from src import doomAsciiTitle, visualiseGuesses

# Random words API - https://github.com/mcnaveen/Random-Words-API#random-words-api
# Credit to https://patorjk.com/software/taag/ for the ascii art below. Best fonts - alpha, doom, doh

print(f"""{doomAsciiTitle}
Welcome to hangman, this time using an API to get a random word for you to guess!
""")

if input("Enter 'Y' to begin, or anything else to quit: ") != "Y":
    quit()

def run():
    responseObject = get("https://random-words-api.vercel.app/word").json()[0]
    # Example --> {'word':'Urticate','definition':'To sting; to flog with nettles  ','pronunciation':'Urtikate'}
    word = responseObject["word"].lower()
    definition = responseObject["definition"].strip()
    pronunciation = responseObject["pronunciation"].strip()

    wordList = ["___ " for char in word]

    incorrectGuessesMade = 0
    guessedCorrectly = False
    gameOver = False
    while not (guessedCorrectly or gameOver):
        if incorrectGuessesMade == 11:
            gameOver = True
            break
        if [f'_{char}_ ' for char in word] == wordList:
            guessedCorrectly = True
            break
        guessedLetter = input("Enter letter(s) to be guessed: ")
        if guessedLetter == "quit()":
            quit()
        #secret!!
        if guessedLetter == "QWERTY":
            print(word)
            continue
        guessedLetter = guessedLetter.strip().lower()
        if len(guessedLetter) == 1:
            if guessedLetter in word:
                indices = [i for i in range(len(word)) if word[i] == guessedLetter] # list comprehension with indices where guessedLetter occurs in word
                # now loop through indices to replace the underscores in wordList with the letter that the user just correctly guessed
                for index in indices:
                    wordList[index] = f'_{guessedLetter}_ '
            else: # if the letter they guessed isn't in the word
                incorrectGuessesMade += 1
        else: # i.e. they guess the entire word
            if guessedLetter != word:
                incorrectGuessesMade += 1
            else:
                guessedCorrectly = True
        print(visualiseGuesses(incorrectGuessesMade))
        print(*wordList,f"  guesses left = {11-incorrectGuessesMade}")
    
    if guessedCorrectly:
        print(f"""
Congratulations! You successfully guessed the word!
The word was {word}.
Definition: {definition}.
Pronunciation: {pronunciation}.
        """)
        again = input("Enter 'y' to play again, or anything else to quit ")
        if again != "y":
            quit()

    if gameOver:
        print(f"""
Unlucky! You weren't able to guess the word.
The word was {word}.
Definition: {definition}.
Pronunciation: {pronunciation}.
        """)

while True:
    run()
