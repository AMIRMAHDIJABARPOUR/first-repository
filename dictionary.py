# FIRST CHANGE
#secend change
import random

def select_word():
    words = ["tiger", "tree", "underground", "giraffe", "chair"]
    return random.choice(words)

def remove_letter(word, guessed_letter):
    return word.replace(guessed_letter, "")

def guess_letter(word, guessed_letter):
    if guessed_letter in word:
        return remove_letter(word, guessed_letter), True
    else:
        return word, False

def play_hangman():
    word = select_word().upper()
    remaining_attempts = 6
    guessed_letters = ""

    while remaining_attempts > 0:
        print(f"Word: {' '.join(letter if letter in guessed_letters else '_' for letter in word)}")
        guessed_letter = input("Guess a letter: ").upper()

        if guessed_letter in guessed_letters:
            print("You already guessed this letter.")
        else:
            word, correct = guess_letter(word, guessed_letter)
            if correct:
                guessed_letters += guessed_letter
            else:
                print(f"There are no {guessed_letter}'s")
                remaining_attempts -= 1

        if "_" not in word:
            print(f"Congratulations! The word was {word}. You win!")
            break

    if remaining_attempts == 0:
        print(f"Sorry, you're out of attempts. The word was {word}. Better luck next time!")

if __name__ == "__main__":
    play_hangman()
