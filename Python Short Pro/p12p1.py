#def fact(x):
# """Function that returns the factorial of its argumentAssumes that its argument is a non-negative integer"""
# res = 1
# for i in range(1, x+1):
# res*= i
# return res
# # Prompt the user for an integernumber = int(input("Enter a number ""))
# if number >= 0:
# print(fact(number))

#A



def fact (x):      
    res=1
    for i in range(1,x+1):
       res*=i 
    return res

#B
#prompt user for number 


number=int(input("enter a number please(number above 0)"))

if number >=0:
    print(fact (number))
else:
    print(number + "is negative")

