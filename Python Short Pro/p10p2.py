#progrm to find cuberoot of a number entered by user 
#prompt user for number 
#int (input(enter a number ))
#if number<0:
#newnumber=-number
#else: newnumber = number 

#cuberoot=0
#if number ==0 :
#   exit program 
#else:
#while cuberoot**3<newnumber do:
#increment cuberoot. 
#if cuberoot**3== newnumber:
#   if number<0:
        #cuberoot=-cuberoot
    #print - cube root of number
#else print numnber is not a perfect cube. 


number=int(input("Enter a number please"))


if number < 0:
    new_number = -number
else:
    new_number = number

cuberoot=0

if number==0:
    print()
else:
    while cuberoot **3 < new_number:
        cuberoot+=1
    if cuberoot **3==new_number:
        if number<0:
            cuberoot=-cuberoot
        print("cube root of", number, "is" ,cuberoot)
    else:
        print(number, "is not a perfect cube")  

