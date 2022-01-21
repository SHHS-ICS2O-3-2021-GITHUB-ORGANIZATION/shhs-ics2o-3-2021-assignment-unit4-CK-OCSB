# NAME OF AUTHOR: Carter King (CK-OCSB)
# NAME OF THE PROGRAM: Q2Average)
# DATE OF CREATION: 1/20/22
# PURPOSE OF PROGRAM: Recives input from user until zero is enterd, once zero is enterd then the program will output the sum and average

# VARIABLE DEFINITION 
addedSum = (0)
Average = (0) 
counter = (0)


# INPUT
nonZeroNumb = float(input("Enter your numbers (when ready type 0 to Exit): ")) #reciving the numbers to calculate

# PROCESSING
while nonZeroNumb != 0:  # the program counts the amount of numbers added
    addedSum = addedSum + nonZeroNumb
    nonZeroNumb = float(input())
    counter = counter + 1

addedSum = addedSum + nonZeroNumb #adds all numbers togeather to get sum 
Average = addedSum/counter #calculates  average


# OUTPUT 
print ("Total sum of entered number is", addedSum) #prints the sum of all numbers entered
print("Total average of entered number is", Average)