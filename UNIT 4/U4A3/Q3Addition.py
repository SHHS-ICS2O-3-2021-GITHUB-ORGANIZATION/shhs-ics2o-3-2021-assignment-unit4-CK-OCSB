# NAME OF AUTHOR:  Carter King  (CK-OCSB)
# NAME OF THE PROGRAM:  Q3Addition
# DATE OF CREATION:  January 16th, 2022
# PURPOSE OF PROGRAM:  Generates a number between a set range given by the user.


# VARIABLE DEFINITION.
import random
Var1 = random.randint(1, 100)
Var2 = random.randint(1, 100)
CorrectAnswer = Var1 + Var2

# INPUT: The only input we need is the answer from the user

#answer = input()

# PROCESSING
print("Welcome to simple addition practice, numbers 1-100")
print("your question is:",str(Var1), "+", str(Var2) +"= ?")
answer = int(input())



# OUTPUT
if answer == CorrectAnswer:
  print("Correct!")
if answer < CorrectAnswer :
  print("Incorrect, keep practicing!")
  print("The correct answer was",str(CorrectAnswer))
if answer > CorrectAnswer :
  print("Incorrect, keep practicing!")
  print("The correct answer was",str(CorrectAnswer))

print("If you would like another addition problem press stop and run this program again.")