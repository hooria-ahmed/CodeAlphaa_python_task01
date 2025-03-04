
import random


def choose_secret_word():
    """Select a secret word from a list."""
    words = ['python', 'hangman', 'programming', 'challenge', 'development']
    return random.choice(words).lower()


def draw_hangman(attempts_left):
    """Draw a unique hangman based on remaining attempts."""
    hangman_art = [
         """
           ________
          |        |
          |        O
          |       /|\\
          |       / \\
          |
        """,
        """
           ________
          |        |
          |        O
          |       /|\\
          |       / 
          |
        """,
        """
           ________
          |        |
          |        O
          |       /|
          |        
          |
        """,
        """
           ________
          |        |
          |        O
          |        |
          |        
          |
        """,
        """
           ________
          |        |
          |        O
          |        
          |        
          |
        """,
        """
           ________
          |        |
          |        
          |        
          |        
          |
        """,
        """
           ________
          |        
          |        
          |        
          |        
          |
        """
    ]
    return hangman_art[attempts_left]


def get_word_hint(secret_word, guessed_letters):
    """Provide a dynamic hint based on the secret word and guessed letters."""
    unguessed_letters = [letter for letter in secret_word if letter not in guessed_letters]
    if unguessed_letters:
        hint_letter = random.choice(unguessed_letters)
        return f"🔍 Hint: The word contains the letter '{hint_letter}'."
    else:
        return "🔍 Hint: You've already guessed all the letters!"


def start_the_game():
    """Start the Hangman game with quirky elements."""
    while True:
        secret_word = choose_secret_word()
        guessed_letters = []
        attempts_left = 6
        easter_egg_chance = 3  # Chance to show an Easter egg message

        print("🎉 Welcome to Hangman! 🎉")
        print("Guess the word or type 'hint' for a clue!")

        while attempts_left > 0:
            print(draw_hangman(attempts_left))
            current_progress = ' '.join([letter if letter in guessed_letters else '_' for letter in secret_word])
            print("Current word: " + current_progress)
            print("Guessed letters: " + ' '.join(guessed_letters))

            guess = input("Guess a letter or type 'hint': ").lower()

            # Check for Easter egg message randomly
            if random.randint(1, 10) == easter_egg_chance:
                print("🎉 Whoa there! Did you know that your guess is like a treasure hunt? Let's find the word!")

            # Hint option
            if guess == 'hint':
                print(get_word_hint(secret_word, guessed_letters))
                continue

            # Input validation
            if len(guess) != 1 or not guess.isalpha():
                print("🚫 Invalid input! Please enter a single letter.")
                continue

            # Check for full-word guess
            if len(guess) == len(secret_word):
                if guess == secret_word:
                    print(f"🔥 Brilliant! You guessed '{secret_word}'!")
                    break
                else:
                    print(f"😱 Oops! That's not it. You lose 1 attempt!")
                    attempts_left -= 1
                    continue

            if guess in guessed_letters:
                print("🤔 You've already guessed that letter. Try something new!")
            elif guess in secret_word:
                guessed_letters.append(guess)
                print("🎉 Awesome guess!")
            else:
                guessed_letters.append(guess)
                attempts_left -= 1
                failure_messages = [
                    "😞 Wrong guess! Oof, you have {} attempts left.",
                    "😩 Nope! Try again. You have {} attempts remaining.",
                    "😢 That's not it! You have {} attempts left.",
                    "😖 Uh-oh! You have {} attempts left now."
                ]
                print(random.choice(failure_messages).format(attempts_left))

            # Check if the player has guessed all letters in the secret word
            if all(letter in guessed_letters for letter in secret_word):
                print("🎊 Congratulations! You've uncovered the word: " + secret_word)
                break

        if attempts_left <= 0:
            print(draw_hangman(attempts_left))
            print("😢 Sorry, you've run out of attempts. The word was: " + secret_word)
            if len(guessed_letters) >= len(secret_word) // 2:
                print("You were close! Better luck next time!")
            else:
                print("Don't give up! Practice makes perfect.")

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thanks for playing! Goodbye!")
            break


if __name__ == "__main__":
    start_the_game()