#!/usr/bin/env python3 
import random

print("Hello this is your handgame program!!")
WordList=["hacker","secdojo","rebot"] # liste of words 
secret = random.choice(WordList) 

empty = []
for letter in secret:
    empty += "_"
print(empty)

game_over = False

while not game_over:
    choice = str(input("Enter your guess letter: ")).lower()
    for position in range(len(secret)): # loop through each letter in the secret word
        letter = secret[position]
        if choice == letter :
            empty[position]= letter
            print("right :)")
    print(empty) 
          
    if "_" not in empty:
        print("You win :) You guess the full word")
        game_over = True

