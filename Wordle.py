import random
from sys import exit

# methods
def print_list(wordle_list):
    message = ""
    for letter in wordle_list:
        message += str(letter) + "  "
    print(message)

def check_valid_input(input_word):
    if len(input_word) == 5:
        return input_word
    else:
        while len(input_word) != 5:
            print("Invalid input, try again.")
            input_word = input()
        return input_word

def check_answer(input_word, wordle_word):
    display_word = []
    for i in range(0, 5):
        if input_word[i] == wordle_word[i]:
            display_word.append("|{}|".format(input_word[i].upper()))
        elif input_word[i] in wordle_word:
            display_word.append(input_word[i].upper())
        else:
            display_word.append(input_word[i])
    return display_word

def attempt(attempt_number, wordle_word):
    print("Please enter your guess for attempt number {}".format(attempt_number))
    input_one = input()
    input_one_final = check_valid_input(input_one).lower()
    display_word = check_answer(input_one_final, wordle_chars)
    print_list(display_word)
    count = 0
    for i in range(0, 5):
        if input_one[i] == wordle_word[i]:
            count += 1
    if count == 5:
        print("Congrats! You did it!")
        exit(0)
    
    

print("Hello and welcome to Wordle")

with open('five_letter_words.txt', 'r') as file:
    words_string = file.read()

words_list = words_string.split()

wordle_word = words_list[random.randint(0, len(words_list))]

wordle_chars = list(wordle_word)
wordle_response = ["[]", "[]", "[]", "[]", "[]"]

for i in range(1, 7):
    attempt(i, wordle_chars)
    
print("Sorry, you lost :(")