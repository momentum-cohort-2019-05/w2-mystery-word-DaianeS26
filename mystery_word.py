import random

with open("words.txt") as word_file:
      text_file = word_file.read()
      text_list = text_file.lower().split()

easy_words = []
medium_words = []
hard_words = []


for i in text_list:
    if len(i) <= 6:
        easy_words.append(i.lower().strip())
    if len(i) >=7 and len(i) <= 10:
        medium_words.append(i.lower().strip())
    if len(i) >= 11:
        hard_words.append(i.lower().strip())

def game (easy_words, medium_words, hard_words):

    active_list = choose_level(easy_words, medium_words, hard_words)
    word_to_guess = random.choice(active_list)
    round_guess = 8
    current_guesses = []
    alphabet_letters = "abcdefghijklmnopqrstuvwsyz"
    outcome = ""
    for i in word_to_guess:
        current_guesses.append("_")
    actual_word = []
    for i in word_to_guess:
        actual_word.append(i)


    already_guessed = []
#     print(word_to_guess)
#     print(*actual_word)
    while current_guesses != actual_word and round_guess > 0:
        print(f'This is {round_guess} round')
        print(*current_guesses)
        guess = input("Choose a letter:  ").lower()
        
        if guess not in alphabet_letters or len(guess) > 1:
            print('Not a valid guess')
        elif guess in already_guessed:
            print("You used this letter before")
        elif guess in actual_word:
            index = list_of_indexes(guess, word_to_guess)
            for i in index:
                current_guesses[i] = guess
            if "_" not in current_guesses:
                print("Congratulations. You guessed the word!")
                outcome = "W"
                round_guess = 0
            else:
                round_guess -= 1
                print(f'You have {round_guess}')
                # round_guess -= 1
            already_guessed.append(guess)
        else:
            print("You have not figure out the word")
            already_guessed.append(guess)
            round_guess -= 1
    if outcome != "W":
        print(f"I am sorry. You lost. The correct word was {word_to_guess.upper()}!")
    
    play_again(input("Would like play again? (Y)es or (N)o  "))


def play_again(string):
    if string.lower() == "y":
        return game(easy_words, medium_words, hard_words)
    elif string.lower() == "n":
        print("Thanks for playing!")
        exit()
    else: 
        return play_again(input("Please choose an option"))

    
    
def list_of_indexes(guess, word):
    index = []
    x = 0
    for i in word:
        if i == guess:
            index.append(x)
        x += 1

    return index 



def choose_level(easy_words, medium_words, hard_words):
    list_of_words = []
    choose_level = input ("Choose a level: (E)asy, (M)edium, (H)ard  ").upper()
    if choose_level == "E":
        list_of_words = easy_words
    elif choose_level == "M":
        list_of_words = medium_words
    elif choose_level == "H":
        list_of_words = hard_words
    else:
        print("I don't understand what you said.")
        return choose_level(easy_words, medium_words, hard_words)
    return list_of_words


game(easy_words, medium_words, hard_words)
  

