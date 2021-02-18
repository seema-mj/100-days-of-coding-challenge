import random
from replit import clear
from hangman_art import logo , stages
from hangman_words import word_list

print(logo)
print("\n")
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6
display = []
for i in range(word_length):
  display += "_"
print(display)

while not end_of_game:
    guess = input("\nGuess a letter: ").lower()
    clear()
    if guess in display:
      print(f"You've already guessed {guess}")

    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        # print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
          display[position] = letter
    #print(display)
    print(f"{' '.join(display)}")

    #Check if user is wrong.
    if guess not in chosen_word:
        print(f"\nSorry... {guess} is not present in the word")
        lives -= 1
    if lives == 0:
      end_of_game = True
      print("\nYou lose.")
      print(f"\nThe movie name is {chosen_word}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("\nYou win.")

    print(stages[lives])
