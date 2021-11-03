import random
print("Welcome to Richards guessing game, lets see if you can guess the number on my mid...")

x = random.randrange(1, 10)
num_of_guesses = 3


guess = int(input("What number do you think I'm thinking of?: "))

while guess != x:
    print("Oops, try again! \n")
    guess = int(input("What number do you think I'm thinking of?: "))

print("Congratulations, you figured me out!")
