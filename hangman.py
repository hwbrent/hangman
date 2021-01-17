
import random

command = input("Enter 'y' to start or / to add a word, or quit() to quit | ")
print()

if command.lower() == "/":
    inp = input("Enter a word to add to the file. Spell correctly & only use letters: ")
    print()
    word = inp.lower()

    infile = open("hangman_words.txt","r")
    read = infile.read()
    infile.close()

    if not word in infile: # puts the word into the words.txt file
        infile.close()
        opn = open("hangman_words.txt","a")
        opn.write(f',{word}')
        opn.close()
        henlo = input("Enter 'y' to start, or anything else to quit: ")
        print()
        if not henlo == "y":
            quit()

elif command.lower() == "quit()":
    quit()
elif command.lower() != "y":
    print("Invalid input")
    quit()

def chooseWord():
    infile = open("hangman_words.txt")
    red = infile.read()
    lst = red.split(",")
    infile.close()
    

    num = random.randrange(0,len(lst))
    return lst[num]

new = chooseWord()
#print(new)

wordguess = []
outp = []

for letter in new:
    wordguess.append(letter)
    if letter == new[-1]:
        outp.append(" __ ")
    else:
        outp.append(" __")

def printer(): 
    base = ""
    for value in outp:
        if (value == ' __') or (value == ' __ '):
            base += value
        else:
            base += f" {value}"
    return base

def indexFinder(input,target):
    index = 0
    solution = []
    for letter in input:
        if letter == target:
            solution.append(index)
        index += 1
    return solution

guesses_remaining = [6]
guesses = []
def guesser():
    guesses.sort()
    print(f"{printer()} - Letters guessed: {guesses}, Remaining: {guesses_remaining}")
    guess = input("Guess a letter: ")
    if guess in guesses:
        print()
        print("You've already guessed this letter, silly!")
    else:
        guesses.append(guess)
        if guess.lower() in wordguess: # if the letter guessed is in the word to be guessed
            indices = indexFinder(new,guess) # the indices of the guessed letter in the word to be guessed
            for index in indices:
                outp[index] = guess
        else:
            guesses_remaining[0] -= 1

while outp != wordguess:
    if guesses_remaining[0] <= 0:
        print()
        print("Game over! You lost :( . The word you were looking for was",new)
        print()
        quit()
    print()
    guesser()

print()
print(f"Well done! You guessed that the word was **{new}**!")
print()

quit()

#############################################################################
'''
var "new" --- word to be guessed
wordguess = [] --- list containing letters of word to be guessed
outp = [] --- the __ visual thing
'''
#############################################################################