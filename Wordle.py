print("Hello and welcome to Wordle")

with open('five_letter_words.txt', 'r') as file:
    words_string = file.read()

print(words_string)