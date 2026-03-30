# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 12:21:20 2026

@author: Rachel
"""
import random

def pickRandom():
    words = []
    with open('sowpods.txt', 'r') as f:
        for line in f:
            word = ""
            for char in line:
                if char != '\n':
                    word += char
            words.append(word)
    return random.choice(words)

def printHangman(hangman):
    for item in hangman:
        print(item, end = " ")
    print()

chosenWord = pickRandom()
#print(chosenWord)
print(">>> Welcome to Hangman!")
print("Enter an uppercase letter.")

hangman = []
for i in range(len(chosenWord)):
    hangman.append('_')

printHangman(hangman)

guessed = []
correct = 0
incorrect = 0
win = False

while incorrect < 6 and win == False:
    print()
    guess = input(">>> Guess your letter: ")
    
    if guess in guessed:
        print("You already guessed that letter.")
    
    elif len(guess) > 1 or guess == guess.lower():
        print("Not a valid letter.")
    
    else:
        guessed.append(guess)

        inWord = False
        indices = []
        for i in range(len(chosenWord)):
            if chosenWord[i] == guess:
                inWord = True
                indices.append(i)

        if inWord:
            print("Correct!")
            correct += 1
            for index in indices:
                hangman[index] = guess
            printHangman(hangman)
        else:
            incorrect += 1
            print("Incorrect!")
            printHangman(hangman)
    
    if '_' not in hangman:
        win = True
    
    if win == False:
        print()
        print(">>> You have", (6 - incorrect),  "incorrect guesses left.")

if win:
    print()
    print("You won!")
else:
    print()
    print("You lost.")
    print("The correct word was", chosenWord)
        
        