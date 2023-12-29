from hangman_word import word_list
from hangman_art import logo, stages
import random
from replit import clear

# choose the word randomly
choice_word = random.choice(word_list)
word_length = len(choice_word)

print(logo)
print("Guess the word, save the hangman! 🎩🪓🔤\n")
live = 6

display = []
for _ in range(word_length):
  display += "_"
print(display)

# check if the letter the user guessed
end_of_game = False

while not end_of_game:
  guess = input("Enter a letter: ").lower()

  clear()

  # Check for errors (only letters allowed)
  if guess in display:
    print(f"You have already guessed {guess}.")
  for position in range(word_length):
    letter = choice_word[position]

    if letter == guess:
      display[position] = letter

  if guess != choice_word:
    print(f"You guessed {guess}, that's not in the word. You lose a life. ")
    live -= 1
    if live == 0:
      end_of_game = True
      print("You lose.")

  print(f"{' '.join(display)}")

  if "_" not in display:
    end_of_game = True
    print("Congratulations! You have won!")

  print(stages[live])

print("Thanks for playing!")
