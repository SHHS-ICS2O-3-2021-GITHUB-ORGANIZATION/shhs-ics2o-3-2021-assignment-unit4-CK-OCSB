# NAME OF AUTHOR:  Carter King
# NAME OF THE PROGRAM:  Q3Taxes
# DATE OF CREATION:  January 13th, 2022
# PURPOSE OF PROGRAM:  Calculate the subtotal, HST, and Toatl costs of 10 items

#The top code runs as inteded the code below is sorted

print("Please list the 10 item's prices one at a time")
print ("Plese make sure to press the enter key after every number")
item1 = float(input())

item2 = float(input())

item3 = float(input())

item4 = float(input())

item5 = float(input())

item6 = float(input())

item7 = float(input())

item8 = float(input())

item9 = float(input())

item10 = float(input())
print ("One moment while we calculate your total")

subtotal = item1 + item2 + item3 + item4 + item5 + item6 + item7 + item8 + item9 + item10

print (" Your subtotal is")
print ("$" + str(subtotal))

HST = float(subtotal) * 0.13
HST = round(HST, 2)
print ("HST (taxing) cost is 13%")
print("Your tax comes to")
print ("$" + str(HST))

Total = HST + subtotal
print("Your total is")
print ("$" + str(Total))
#Was unsure of required way to run code, the sorted code is below and the unsoreted runing code is above.

""""
# NAME OF AUTHOR:  Carter King (CK-OCSB)
# NAME OF THE PROGRAM:  Q3Taxes
# DATE OF CREATION:  January 13th, 2022
# PURPOSE OF PROGRAM:  Calculate the subtotal, HST, and Toatl costs of 10 items


# VARIABLE DEFINITION
#User will be propted to give info of 10 it here
item1 = float(input())

item2 = float(input())

item3 = float(input())

item4 = float(input())

item5 = float(input())

item6 = float(input())

item7 = float(input())

item8 = float(input())

item9 = float(input())

item10 = float(input())

# Not all items have the same values and can be subject to variable change

subtotal = item1 + item2 + item3 + item4 + item5 + item6 + item7 + item8 + item9 + item10

HST = float(subtotal) * 0.13
HST = round(HST, 2)

Total = HST + subtotal

# INPUT
#Input is random numbers and relys on users numbers given at the begining of the program
item1 = float(input())
item2 = float(input())
item3 = float(input())
item4 = float(input())
item5 = float(input())
item6 = float(input())
item7 = float(input())
item8 = float(input())
item9 = float(input())
item10 = float(input())

# PROCESSING
print("Please list the 10 item's prices one at a time")
print ("Plese make sure to press the enter key after every number")

subtotal = item1 + item2 + item3 + item4 + item5 + item6 + item7 + item8 + item9 + item10


# OUTPUT
#print("Please list the 10 item's prices one at a time")
#print ("Plese make sure to press the enter key after every number")
print ("One moment while we calculate your total")
print (" Your subtotal is")
print ("$" + str(subtotal))
print ("HST (taxing) cost is 13%")
print("Your tax comes to")
print ("$" + str(HST))
print("Your total is")
print ("$" + str(Total))
"""