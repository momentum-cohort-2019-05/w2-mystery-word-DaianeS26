# Ask user to pick difficulty level
# Switch between levels

import random

with open("words.txt") as word_file:
        #create a variable
        text_file = word_file.read()
        #create a new variable. This will create a list with lower case words.
        text_list = text_file.lower().split()
        # new variable that will randomly choose word from list. Need to loop first
        # random_word= random.choice(text_list)

# print to test
# print(text_file)
# print(text_list)
# print(random_word)

#for loop iterates through list and add words based on difficulty to assigned variables

easy_words = []
medium_words = []
hard_words = []

for i in text_list:
        if len(i) <= 6:
               easy_words.append(i)
        if len(i) >= 7 and len(i) <=10:
                medium_words.append(i)
        if len(i) >= 11:
                hard_words.append(i)

#variables by difficulty

random_easy_words = random.choice(easy_words)
random_medium_words = random.choice(medium_words)
random_hard_words = random.choice (hard_words)
# print(random_easy_words)
# print(random_medium_words)
# print(random_hard_words)

# word_to_guess = random_easy_words
word_to_guess = random_medium_words
# word_to_guess = random_hard_words

# print(random_word)
current_guesses = "_" * len(word_to_guess)

def guess_word(letter, user_guess):
    if user_guess == letter:
        return user_guess
    return "_"

has_won = False
wrong_guess = 0

def guess_checker(word_to_guess, current_guesses, user_guess):
        new_guesses = ""
        for letter in word_to_guess:
                if letter in current_guesses != "_":
                        new_guesses += letter
                else:
                        new_guesses += guess_word(letter, user_guess)
        return new_guesses
print()
# print(current_guesses)

while has_won == False and wrong_guess <= 3:
        user_guess = input("Choose a letter: ").lower()
        current_guesses = guess_checker(word_to_guess, current_guesses, user_guess)
        if user_guess not in word_to_guess:
                wrong_guess +=1

        if "_" not in current_guesses:
                print("Congratulations! You are the best!")
                has_won = True 
        print(current_guesses)

if has_won == False:
        print(f'I am sorry. You lost. The correct word was: {word_to_guess}!')
  