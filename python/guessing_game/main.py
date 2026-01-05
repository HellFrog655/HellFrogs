import random

answer = random.randint(1, 10)

while True:
    guess = int(input("Guess number 1-10: "))
    if guess == answer:
        print("Correct!")
        break
    print("Try again")
