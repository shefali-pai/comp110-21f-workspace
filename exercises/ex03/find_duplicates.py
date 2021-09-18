"""Finding duplicate letters in a word."""

__author__ = "730466264"


chosen_word: str = str(input("Enter a word: "))
length: int = len(chosen_word)
bool_value: bool = bool(False)
i: int = 0

while i <= length - 1:
    position = i + 1
    while position <= length - 1:
        if chosen_word[i] == chosen_word[position]:
            bool_value = True
            position = length
            i = length
        position = position + 1
    i = i + 1

print("Found duplicate: " + str(bool_value))
