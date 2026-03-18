import random
from hangman__art import stages,logo
from hangman_words import categories


print(logo)

print("\nAvailable categories:")
for category in categories:
    print("-", category.replace("_", " ").title())

while True:
    user_category = input("\nChoose a category: ").lower().replace(" ", "_")
    if user_category in categories:
        break
    print("Invalid category. Try again.")

while True:
    user_level = input("Choose difficulty (easy, medium, hard): ").lower()
    if user_level in categories[user_category]:
        break
    print("Invalid difficulty. Try again.")


chosen_word = random.choice(categories[user_category][user_level])

if user_level == "hard" :
    LIVES=5
elif user_level == "medium" :
    LIVES = 7
else :
    LIVES = 10
lives=LIVES
display = ["_"] * len(chosen_word)
guessed_letters = []
game_over = False

print(f"****************************LET'S START**************************************")
while not game_over:


    
    print(f"****************************{lives}/{LIVES} LIVES LEFT****************************")

    guess = input("Guess a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one alphabet letter.")
        continue

    if guess in guessed_letters:
        print(f"You already guessed '{guess}'.")
        continue

    guessed_letters.append(guess)

    if guess in chosen_word:
        print(f"Good guess! '{guess}' is in the word ")
        for i in range(len(chosen_word)):
            if chosen_word[i] == guess:
                display[i] = guess
    else:
        lives -= 1
        print(f"Wrong guess! '{guess}' is not in the word ")

    print("Word to guess:", " ".join(display))
    print("Guessed letters:", ", ".join(guessed_letters))
    print(stages[lives])

    if "_" not in display:
        game_over = True
        print("****************************YOU WIN****************************")
        print("The word was:", chosen_word)

    if lives == 0:
        game_over = True
        print("\n You lose!")
        print("The word was:", chosen_word)