#Two suggested optimisations for the algorithm to calculate the divisors of a number are to initalise the divisors
#tuple to include 1 and the number itself and to only search from 2 and as far as half of the number.

#define function finddivisors(num1)
#divisors()#change this to include 1 and the numbers themselves = divisors (1,num1,num2)
#to find up to half of the numbers :do 
#nnum1=num1//2
#nnum2=num2//2
#for i in range (2,min (nnum1,nnum2)+1): #change here = start at 2 instead of one and just search up until half of the numbers given . 
#   if num1% i==0 and num2%i ==0:
#divisors +=(i,)
#return divisors 

#prompt user for input (number1= int(input(enter a number)))
#number2=int(input(enter another number))
#if number1 <= 0 or number2 <= 0: #check both numbers are positive 
    #print("Numbers should be > 0.")
#else: 
#finddivisors (num1 , num2)
# print them out
#total =0
#for d in divisors :
#total +=d 
# print("Sum of the common divisors is:", total)
        #print("Finished!")
def findDivisors(num1):
      #"""Finds the common divisors of num1 and num2,Assumes that num1 and num2 are positive integers,Returns a tuple containing the common divisors of num1 and num2"""
    divisors = (1,num1)
    nnum1=num1//2
    for i in range(2,(nnum1)+ 1):
        if num1 % i == 0:
            divisors += (i,)
    return divisors

number1 = int(input("Enter a positive integer:  "))

if number1 <= 0:
    print("Numbers should be > 0.")
else:
    # First of all, get the common divisors and print them outdivisors = 
    divisors=findDivisors(number1)
    print("The common divisors of,", number1,"are:", divisors)
    # Now sum them and print the total
    total = 0
    for d in divisors:
        total += d
    print("Sum of the common divisors is:", total)
print("Finished!")

