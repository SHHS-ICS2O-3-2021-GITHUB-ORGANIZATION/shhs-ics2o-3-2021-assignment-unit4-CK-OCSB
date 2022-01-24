# NAME OF AUTHOR:  Carter King (CK-OCSB)
# NAME OF THE PROGRAM: NumberGuessingGame
# DATE OF CREATION:  2022-01-24
# PURPOSE OF PROGRAM:  To play a number guessing game with the user

# VARIABLE DEFINITION
import random
#imports the random module
LowRange = input("Please enter the smallest number in the range of numbers you would like to guess from: ")
# This is setting the lowest number the computer can generate.

HighRange = input("Please enter the largest number in the range of numbers you would like  to guess from: ")
#The user 7sets the highest number the computer can generate.

CorrectNumb = random.randint(int(LowRange),int(HighRange))
#Generates the the number for the user to guess!

attempts = (1)
#This will be used to track the number of attempts  
#The attempts start at one


# INPUT
print("It is now time to guess! \n Please enter the number you think is the same one as the computer       generated")
UserAnswer = int(input())
#The user is promted to guess the number which was generated.

# PROCESSING


while UserAnswer != CorrectNumb:
 print("Please try again")
 UserAnswer = int(input())
 attempts = attempts + 1
#The user is promted to attempt at guessing the number again
#The attempts will increase to keep track of attempts
if UserAnswer == CorrectNumb:
  print ("Correct!")
  print("You took",attempts,"to guess correctly")
#Prints the counter(attempts) in a user freindly matter


# OUTPUT
print("thank you for playing the number guessing game! To play again, run the prgram again. May I suggest a larger range?")
#A closing statement to thank the user for playing