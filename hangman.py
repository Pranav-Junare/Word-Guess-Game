import random

with open("wordlist.txt", "r") as f:
    word = f.readlines()

word = random.choice(word)[:-1]

allowed_error = 7
guesses = []
done = False

while not done:
    for letter in word:
        if letter.lower() in guesses:
            print(letter, end = " ")
        
        else:
            print("_", end = " ")
    
    print("")

    guess = input(f"Allowed error: {allowed_error}, next guess: ")
    guesses.append(guess.lower())

    if guess.lower() not in word.lower():
        allowed_error -= 1
        if allowed_error == 0:
            break
    
    done = True
    for letter in word:
        if letter.lower() not in guesses:
            done = False

if done:
    print(f"Good, the word was {word}")
else:
    print(f"You failed, the word was {word}")