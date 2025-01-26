import random

randomNumber = random.randint(1, 100)
print("Welcome to the guessing game! You have 10 tries to guess the number.")

num = 1
while num < 11:
    userNum=int(input(f"Attempt #{num}: Guess a number between 1 to 100:"))
    num = num + 1
    if userNum > randomNumber:
        print("Your guess was too high")
    if userNum < randomNumber:
        print("Your guess was too low")
    if userNum == randomNumber:
        print(f"You are correct the number was {randomNumber}")
        print("YOU WIN!")
        break

if num > 10:
    print(f"The correct answer was {randomNumber}")
    print("YOU LOSE!")