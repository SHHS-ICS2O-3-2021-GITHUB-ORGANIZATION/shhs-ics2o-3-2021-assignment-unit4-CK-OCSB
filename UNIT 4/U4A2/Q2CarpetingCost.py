# NAME OF AUTHOR:  Carter King (CK-OCSB)
# NAME OF THE PROGRAM:  Q2CarpetingCost
# DATE OF CREATION:  January 12th, 2022
# PURPOSE OF PROGRAM:  To calculate the cost and ammount of carpet needed to cover a room in the users house.

#The top code is the running fuctioning code and the bottom code is the sorted code.
print("What is the Width mesuremnt of your room in metres?")
Width = int(input())

print("what is the lenght mesurement of your room in metres?")
lenght = int(input())
Area = Width * lenght

CarpetPrice = 2.25
print("The price of carpet for one squared metre is $2.25")
print("You need"),print(Area), print("square metres of carpet") 

print ("In order to cover your room in carpet it will cost you")

Cost = Area * CarpetPrice

print ("$"+ str(Cost))





"""
# VARIABLE DEFINITION
Width = int(input())

lenght = int(input())

Area = Width * lenght

Cost = Area * CarpetPrice
# INPUT
Width = int(input())

lenght = int(input())

# PROCESSING
Area = Width * lenght

Cost = Area * CarpetPrice

# OUTPUT
print("What is the Width mesuremnt of your room in metres?")

print("what is the lenght mesurement of your room in metres?")
print("The price of carpet for one squared metre is $2.25")
print("You need"),print(Area), print("square metres of carpet") 

print ("In order to cover your room in carpet it will cost you")
print ("$"+ str(Cost))
"""