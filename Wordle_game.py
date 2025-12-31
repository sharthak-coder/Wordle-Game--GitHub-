# ----------------🎮 WORDLE_GAME 🎮---------------- #
import random

word_list = [
    "apple", "grape", "mango", "peach", "berry",
    "lemon", "olive", "guava", "melon"
]

secret_word = random.choice(word_list)
max_attempts = 6
attempt = 1

print("🎮 WELCOME TO WORDLE (TEXT MODE)")
print("You have to guess a fruit name which is of 5 letter.")
print("Guess the 5-letter word")
print("You have 6 attempts\n")

while attempt <= max_attempts:
    guess = input(f"Attempt {attempt}: ").lower().strip()

    if len(guess) != 5:
        print("❌ Please enter exactly 5 letters\n")
        continue

    if guess == secret_word:
        print("🎉 Congratulations! You guessed the word correctly!")
        break

    feedback = []

    for i in range(5):
        if guess[i] == secret_word[i]:
            feedback.append("🟩")      # correct position
        elif guess[i] in secret_word:
            feedback.append("🟨")      # wrong position
        else:
            feedback.append("⬜")      # not in word

    print("Feedback:", " ".join(feedback), "\n")

    attempt += 1

if attempt > max_attempts:
    print("❌ Game Over!")
    print("The correct word was:", secret_word)