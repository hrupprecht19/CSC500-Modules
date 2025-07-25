# Module 1: Critical Thinking Assignment
# Holly Rupprecht
# CSC500 Principles of Programming
# Douglas Mujeye
# create 12 JUN 2025 

#Creating Python Programs
#Part 1:
#Write a Python program to find the addition and subtraction of two numbers.

#Ask the user to input two numbers (num1 and num2). Given those 
#two numbers, add them together to find the output. Also, 
#subtract the two numbers to find the output.

#this will loop until interger are given 
while True:
    try:
        num1, num2 = [int(x) for x in input('Please provide two numbers separated by a space: ').split()]
        break  # Exit loop once valid input is received
    except ValueError:
        print("Invalid input. Please enter two integers separated by a space.")
print( num1, '+', num2, '=', num1 + num2 )
print( num1, '-', num2, '=', num1 - num2 )

#Part 2:
#Write a Python program to find the multiplication and division of two numbers.

#Ask the user to input two numbers (num1 and num2). Given those two 
#numbers, multiply them #together to find the output. Also, divide 
#num1/num2 to find the output.
while True:
    try:
        num1, num2 = [int(y) for y in input('Please provide two numbers separated by a space: ').split()]
        break  # Exit loop once valid input is received
    except ValueError:
        print("Invalid input. Please enter two integers separated by a space.")
print( num1, '*', num2, '=', num1 * num2 )
print( num1, '/', num2, '=', num1 / num2 )
#Compile and submit your pseudocode, source code, and screenshots of the 
#application executing #the code from parts 1 and 2, the results and 
#GIT repository in a single document (Word is #preferred).