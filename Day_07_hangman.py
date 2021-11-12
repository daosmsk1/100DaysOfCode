import random
import os
from Day_07_hangman_art import stages, logo
from Day_07_hangman_words import word_list


display = []
chosen_word = random.choice(word_list)
end_of_game = False
lives = 6

print(logo)

# Answer
# print(f'Pssst, the solution is {chosen_word}.')

for letter in chosen_word:
    display += "_"

while not end_of_game and lives > 0:
    guess = input("Guess a letter: ").lower()

    os.system('cls' if os.name == 'nt' else 'clear')

    for position in range(len(chosen_word)):
        if guess == chosen_word[position]:
            display.pop(position)
            display.insert(position, chosen_word[position])
    if guess in display:
        print(f"You've already guest {guess}")
    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        print(stages[lives])
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose")
            print(stages[lives])

    print(f"{' '.join(display)}")

    if "_" not in display and lives > 0:
        end_of_game = True
        print("You win.")







