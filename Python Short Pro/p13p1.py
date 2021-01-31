#program to print out the largest of two numbers entered by the user
# # Uses a function max def max(a, b):
# """Function that returns the largest of its two arguments"""
# if a > b:
# return a
# else:return b
# # Prompt the user for two numbers
# number_1 = int(input(’Enter a number please '))
# number_2 = int(input(’Enter another number please’))
# largest= max(number_1, number_2)
# print("The largest number is largest")
# print(’Finished!’)

def max(a,b):
    if a>b:
        return a
    else:
        return b

number_1=int(input("enter a number please "))
number_2=int(input("enter another number please"))

largest=max(number_1,number_2)
print("the largest number is", largest)

print ("finished!")

