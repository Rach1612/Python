# program to print out the largest of two numbers entered by the user
# # Uses a function max
# # Uses max in a print statementdef max(a, b):
# """Function that returns the largest of its two arguments"""
# if a > b:
# return a
# else:
# return b
# # Prompt the user for two numbers
# number1 = float(input(’enter a number please  ’))
# number2 = float(input(’Enter another number please’))
# print(’The largest of’, number_1, ’and’, number_2, ’is’,max(number_1, number_2))
# print(’Finished!’)

def max(a,b):
    if a>b:
        return a
    else:
        return b

number_1=int(input("enter a number please "))
number_2=int(input("enter another number please"))

largest=max(number_1,number_2)
print("The largest of", number_1, "and", number_2, "is",max(number_1, number_2))

print ("finished!")
