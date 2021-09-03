"""
File: khansole_academy.py
-------------------------
Khansole Academy is a program that teaches users how to add by asking users to input answers for the addition of two
randomly generating integers between 10 and 99 inclusive. The program returns feedback based on the User's answers.

"""

#import random
# use code below  to generate a random integer between 30 and 50 for example
#print(random.randint(30, 50))

# ********************************** YOUR CODE GOES BELOW HERE *********************************************************
import random

#this code counts the number of times the program loops
loop_count=0

while (loop_count<3):
#For the first random number
    num1 = random.randint(10,99)
#code for the second random number
    num2 = random.randint(10,99)

#the code below takes the answer of the user
    user_input=int(input(f'What is the sum of {num1} + {num2}: '))
    answer=num1 + num2

#Condition to check if user's input is correct
    if user_input==answer:
        loop_count += 1
        print(f"You've gotten {loop_count} correct in a row")

#This displays when user input is incorrect
    else:
        print("Incorrect. The expected answer is", answer)
#this code resets the counter to 0 and restarts from line 26
        loop_count = 0

#when the user provides the correct answer in three succession,
#the program breaks out of the loop and displays this.
print("Congratulations, You mastered addition")