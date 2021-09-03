"""
File: guessmynumber.py
----------------------
This program checks if a user's guess of a number matches that guessed by the computer
"""

# import random
# use code below  to generate a random integer between 30 and 50 for example
# print(random.randint(1, 99))

# ********************************** YOUR CODE GOES BELOW HERE *********************************************************

#Use random to generate random numbers
import random

#Use secret_number as the variable for the random numbers
secret_number = (random.randint(1, 99))
print('I am thinking of a number between 1 and 99')

#Use the Guess as the input from user
Guess = int(input('Enter a guess: '))

#This line of code check whether the User's guess matches the generated number.
while (Guess != secret_number):

#The if condition checks whether the user's guess is less or higher than the secret number
    if Guess < secret_number:
        print('Your guess is too low')
        Guess = int(input('Enter a guess: '))
    elif Guess>secret_number:
        print('Your guess is too high')
        Guess = int(input('Enter a guess: '))

#If the User's gets the secret number right, the loop will break and this will be printed
else:
    print("Congrats! The number was: " ,Guess)