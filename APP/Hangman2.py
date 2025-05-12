import random
import time

# Initial Steps to invite in the game:
print("\nWelcome to Hangman game :-) \n")
name = input("Enter your name: ")
print("Hello " + name + "! Best of Luck!")
time.sleep(2)
print("The game is about to start!\n Let's play Hangman!")
time.sleep(3)

def main():
    global count
    global display
    global word
    global already_guessed
    global length
    global play_game
    words_to_guess = ["january", "border", "image", "film", "promise", "kids", "lungs", "doll", "rhyme", "damage", "plants"]
    word = random.choice(words_to_guess)
    length = len(word)
    count = 0
    display = '_' * length
    already_guessed = []
    play_game = ""

# A loop to re-execute the game when the first round ends:
def play_loop():
    global play_game
    play_game = input("Do You want to play again? y = yes, n = no \n")
    while play_game not in ["y", "n", "Y", "N"]:
        play_game = input("Do You want to play again? y = yes, n = no \n")
    if play_game == "y":
        main()
        hangman()  # To start a new round after resetting the game
    elif play_game == "n":
        print("Thanks For Playing! We expect you back again!")
        exit()

# Initializing all the conditions required for the game:
def hangman():
    global count
    global display
    global word
    global already_guessed
    global play_game
    limit = 5
    guess = input("This is the Hangman Word: " + display + " Enter your guess: \n")
    guess = guess.strip().lower()

    # Validate guess: it should be a single alphabet character
    if len(guess) != 1 or not guess.isalpha():
        print("Invalid input, try a single letter.\n")
        hangman()  # Retry the same turn
        return

    if guess in already_guessed:
        print("You have already guessed that letter. Try another one.\n")
        hangman()  # Retry the same turn
        return

    if guess in word:
        already_guessed.append(guess)
        # Replace all occurrences of the guessed letter in the display
        display = ''.join([guess if word[i] == guess else display[i] for i in range(len(word))])
        print("Correct! " + display + "\n")

    else:
        count += 1
        
        if count == 1:
            time.sleep(1)
            print("   _____ \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print(f"Wrong guess. {limit - count} guesses remaining\n")

        elif count == 2:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print(f"Wrong guess. {limit - count} guesses remaining\n")

        elif count == 3:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print(f"Wrong guess. {limit - count} guesses remaining\n")

        elif count == 4:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print(f"Wrong guess. {limit - count} last guess remaining\n")

        elif count == 5:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |    /|\\ \n"
                  "  |    / \\ \n"
                  "__|__\n")
            print("Wrong guess. You are hanged!!!\n")
            print(f"The word was: {word}")
            play_loop()

    if display == word:  # Player guessed the word
        print("Congrats! You have guessed the word correctly!")
        play_loop()

    elif count < limit:
        hangman()  # Keep playing

main()
hangman()
