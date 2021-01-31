#input (number 1)
#input num2 
#input num3 

#if num1 % !=0:
    #print("num1")
        #num1=odd1
#if num2 % !=0:
    #print (numb2)
        #numb2=odd2
#if num3 % !=0:
    #print (num3)
        #num3=o



num1=int(input("enter a number"))
num2=int(input("enter another number"))
num3=int(input("enter a third number"))

if num1 % 2==0 and num1 % 2==0 and num1 % 2==0:
    print("None of these numbers are odd numbers")
if num1 % 2!=0 or num2 %2 !=0 or num3 %2 !=0:
    num1,num2, num3=x,y,z


if num1 %2 != 0:
    odd1=num1
else:
    even1=num1

if num2 %2 !=0:
   odd2=num2
else:
    even1=num2
   
if num3 %2 != 0:
    odd3=num3
else:
    even3=num3


if odd1>odd2>odd3:
    print(str(odd1) + "is the largest odd number")
elif odd2>odd3>odd1:
    print(str(odd2) +" is the largest odd number")
elif odd3>odd2>odd1:
    print(str(odd3) +"is the largest odd number")







