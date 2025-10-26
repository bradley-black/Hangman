import random

hangman_pics = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

print(''' _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/                       ''')

print("\nWelcome to Hangman")
print(f'{hangman_pics[0]}\n')

word_list = ["ant", "baboon","beaver","moose","camel", "tiger", "zebra", "lion", "giraffe", "elephant", "crocodile",
             "mouse", "owl", "monkey","hippo", "duck","python","snake", "turtle","shark","spider","whale","eagle","rhino"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
guessed_word = ["_" for i in range(word_length)]
guesses = 0
wrong_guesses = 0
guessed_letters = []

while wrong_guesses < len(hangman_pics)-1:
    user_guess = input("Guess a letter: ")
    if user_guess in guessed_letters:
        print("You already guessed that")
        continue
    for i in range(len(chosen_word)):
        if chosen_word[i] == user_guess:
            guessed_word[i] = user_guess
    guessed_letters.append(user_guess)

    if user_guess not in chosen_word:
        wrong_guesses += 1
        print(wrong_guesses)
        print(hangman_pics[wrong_guesses])

    word = ""
    for char in guessed_word:
        word += char
    if word == chosen_word:
        break
    guesses += 1
    print(guessed_word)

if word == chosen_word:
    print(f'The word is {chosen_word}. You Won with {guesses} guesses')
else:
    print("You lost. Try again.")