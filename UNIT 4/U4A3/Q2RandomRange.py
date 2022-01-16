
# NAME OF AUTHOR:  Carter King  (CK-OCSB)
# NAME OF THE PROGRAM:  Q2RandomRange
# DATE OF CREATION:  January 15th, 2022
# PURPOSE OF PROGRAM:  Generates a number between a set range given by the user.


# VARIABLE DEFINITION. I am unsure if a variable that is input goes here or in the input section so I did both
#Var1 = input()
#Var2 = input()

# INPUT: The set rage of numbers
print ("Give two numbers and random number generator will generate one between the two given")
Var1= int(input())
Var2= int(input())


# PROCESSING
import random
Kelp = random.randint(Var1,Var2)




# OUTPUT
print("The number generateor has produced")
print(Kelp)
print("as your number")