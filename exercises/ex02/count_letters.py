"""Counting letters in a string."""

__author__ = "730466264"


# Begin your solution here...
letter: str = input("What letter do you want to search for?: ")
word: str = input("Enter a word: ")

position: int = 0
i: int = 0

while position < len(word):
    if word[position] == letter:
        i = i + 1
    position = position + 1

print("Count: " + str(i))
