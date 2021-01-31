#progrm to find square root of a number entered by user 
#prompt user for number 
#int (input(enter a number ))
#save square root variable and set to 0 
#squareroot=0
#if number <0 :
#   exit program 
#elif number >0 :do 
#while squareroot**2<number entered: do:
#increment square root. 
#if sqaureroot**2== number:
#this is square root of that number
#print that message 
#else print numnber is not a perfect square. 

number=int(input("Enter a number please"))

squareroot=0

if number<0:
    print()
elif number>0:
    while squareroot **2 <number:
        squareroot+=1
    if squareroot **2==number:
        print("square root of", number, "is" ,squareroot)
    else:
        print(number, "is not a perfect square")  





