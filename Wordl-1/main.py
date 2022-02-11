import random
import nltk

# Dictionary to check if user input is a valid word
from nltk.corpus import brown
word_list = brown.words()
word_set = set(word_list)

# Random seed to select new word from words.txt
from datetime import datetime
random.seed(datetime.now())


word_database = open("words.txt", "r")
wordlist = word_database.readlines()

word_database.close()


print("""                       _ _ 
__      _____  _ __ __| | |
\ \ /\ / / _ \| '__/ _` | |
 \ V  V / (_) | | | (_| | |
  \_/\_/ \___/|_|  \__,_|_|
                          """)
print(" Guess the five letter word!\n")
print("An asterisk (*) means that the letter \nyou guessed  is in the word but is \nin the wrong spot, A (X) means the  \nletter is not in the word. A letter \nthat remains means that it is in \nthe right spot! \n \n - - - - - - - - - - - - - - - - - - \n \n")



tries = 1
check=[0]*10
play = 1
 
guess = ""
x=random.randrange(5756)
word=wordlist[x]
word=word.upper()

while play == 1:
  
  word=word.upper()
  if tries == 1:
    print("\nGuess the five letter word!\n")
  guess= input("Guess: ")
  while len(guess) != 5:
    print ("\nEnter a five letter word \n")
    guess = input("Guess: ")
  while (guess in word_set) == False:
    print ("Not a valid word \n")
    guess = input("Guess: ")

  guess=guess.upper()

  if guess in word:
    if tries == 1:
      print("\nYou guessed the word correctly in", tries , "try!")
      play = int(input("Enter 1 to play again or 0 to quit: "))
      x=random.randrange(5756)
      word=wordlist[x]
    else:
      print("\nYou guessed the word correctly in", tries , "tries!")
      play = int(input("Enter 1 to play again or 0 to quit: "))
    tries = 1
    x=random.randrange(5756)
    word=wordlist[x]

  else:
    tries += 1
    for i in range(5):
      if guess[i] == word[i]:
        check[i] = guess[i]
      elif guess[i] in word:
        check[i]='*'
      else:
        check[i]='X'
    for i in range(5):
      print(check[i], " ", end ='')
    print(" ")
    for i in range(5):
      print(guess[i], " ", end ='')
    print("\n")
  


  




