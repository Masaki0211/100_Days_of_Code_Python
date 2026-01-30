import random
from hangman_words import word_list
from hangman_art import stages

def hangman_game():




    random_word = word_list[random.randint(0,2)]


    blank = []
    for i in range(len(random_word)):
        blank.append("_")

    s = "".join(blank)

    life = 6

    while True:
        print(f"*********************<???>/{life}/6 LIVES LEFT*********************")

        guess = input("Guess a letter: ").lower()
        check = 0
        for i in range(len(random_word)):
            if random_word[i] == guess and blank[i] != guess:
                blank[i] = guess
                check += 1
            elif random_word[i] == guess and blank[i] == guess:
                print(f"You already guessed {guess}")
                check += 1
                break
            else:
                continue


        if check != 0:
            pass
        else:
            print(f"You guessed {guess}, that's not in the word. You lose a life.")
            life -= 1


        if life == 0:
            print(f"It was {random_word}! You lose.")
            print(s)
            print(stages[life])
            break

        s = "".join(blank)
        print(s)
        print(stages[life])
        if s == random_word:
            print("You win.")
            break


hangman_game()
