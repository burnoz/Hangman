import random

words_l = ["python", "java", "swift", "javascript"]

wins = 0

losses = 0

print("H A N G M A N")

while True:
    ans = input('Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit: \n')

    if ans == "play":

        wordy_word = random.choice(words_l)

        wordy_set = set(wordy_word)

        letters = set()

        wrongy_wrong = set()

        tries = 8

        while tries > 0 and wordy_set != letters:

            hinty_hint = ""

            for c in wordy_word:

                if c in letters:
                    hinty_hint += c

                else:
                    hinty_hint += "-"

            user_guess = input(f'\n{hinty_hint}\nInput a letter: ')

            if len(user_guess) != 1:
                print("Please, input a single letter.")

            elif not(user_guess.isalpha()) or user_guess.isupper():
                print("Please, enter a lowercase letter from the English alphabet.")

            elif user_guess in letters or user_guess in wrongy_wrong:
                print("You've already guessed this letter.")

            elif user_guess not in wordy_set:
                tries -= 1
                wrongy_wrong.add(user_guess)
                print("That letter doesn't appear in the word")

            else:
                letters.add(user_guess)

        if wordy_set == letters:
            print("You guessed the word {}!".format(wordy_word))
            print("You survived!\n")
            wins += 1

        else:
            print("You lost!\n")
            losses += 1

    elif ans == "results":
        print("You won: {} times".format(wins))
        print("You lost: {} times".format(losses))

    elif ans == "exit":
        break

    else:
        print("Please enter a valid option")
        continue

# burnoz
