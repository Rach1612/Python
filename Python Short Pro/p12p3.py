#program using function to find the approximate square root of a number 
#set function name and values : def approot (x,y): 
#set step =y**2
#set root=0.0
#while abs(x-root**2)>= y ad root <=x: do 
#increment the step, incremenet the number of guesses
#if abs(x-root**2) <=y and root <=x :
#if abs(x-root**2) <= y and root <=x:
    # return root

def approot (x,y):
    step =y**2
    root=0.0
    numGuesses=0
    root=0.0
    while abs(x - root**2) >= y and root <=x:
        root +=step
        numGuesses +=1
        if abs(x -root**2)<=y and root <=x:
            return root
        



number=float(input("enter a number for which you would like to find the square root of"))
tolerance=(float(input("enter the tolerance or epsilon number value")))
if number >=0:
    print("the approximate square root of this number is", approot(number,tolerance))
else:
    print("error , this number is a negative number, please try again")




