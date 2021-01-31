#define the function fact:
#def fact(x):
#if x==0:
#return 1
#else: do 
#return x * fact(x-1)
#promt user for input int :
#number = int(input(enter a non negative number please))
# check it is non negative :
#if number <0:
#print error message 
# else: call funtion and retrieve answer :
# check funtion working : print (number * fact(number - 1))
#print("factorial of", number, "is", fact(number))




#part a :
#recursive function that takes as its single argument a non-negative integer and returns the factorial of the number.

def fact(x):
    if x==0:
        return 1
    else:
        return x * fact(x-1)

#part b
#program which prompt user for a number, checks this number is non negative
#if non negative call function def fact above 
#if not print error message 

number= int(input("enter a non negative number please"))

if number<0:
    print(" error , number must be positive")
else:
    print (number * fact(number - 1))
    print("factorial of", number, "is", fact(number))

#partc = included print statement "number * fact(number - 1)"

