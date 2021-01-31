#Program A
#for this program the user will input length 

print("To calculate area of a square we need to find lenght of one side of the square")
sideofsquare=(float(input("Enter length of side of the square"))) #ask user to enter lengh 

print(float(sideofsquare)) #check lengh is correct
if sideofsquare <0:#check lengh is not negative number
    print("Length must be >= 0. Please try again")
else:
    areaofsquare=sideofsquare ** 2 #calculation to find area of square
    print("thank you")
    print("area of square is" ":"+ str(float(areaofsquare)))

#program B 
lengthofside=(float(input("Please input length of side")))
print(float(lengthofside))

if lengthofside <0:
    print("Length must be >= 0. Please try again") #check lengh is not negative number
    

else:  
    areaofcube=lengthofside**3
    print(float(areaofcube))
    print("area of cube is :" + str(float(areaofcube)))

#Program C
#area of circle with diameter : 202067.39 
#if diameter= 202067.39 radius = half of this 
#formula for calculating area of circle is A= pi x radius squared 

#import math
import math 
math.pi
print(math.pi) #to check math is working correctly

diameterofcircle=(float(input("Enter the diameter of the cirle please")))
print(float(diameterofcircle))

if diameterofcircle <0:
    print("Length must be >= 0. Please try again.")

else:
    radius=diameterofcircle/2
    print(float(radius))

    areaofcircle=float(math.pi)*radius**2
    print("area of circle is :" + str(float(areaofcircle)))

#Program D
#volume of a sphere with diameter length :202067.39
#formula : v = 3/4 x pi x radius to the power of 3 

#radius= diameter/2 

diameterofsphere=int(float(input("Enter the length of diameter of the sphere please")))
print (float(diameterofsphere))

if diameterofsphere <0:
    print("Length must be >= 0. Please try again.")
else:
    radiusofsphere=(float(diameterofsphere / 2))
    print(float(radiusofsphere))

    volumeofsphere=3/4 * (math.pi *(float(radiusofsphere **3)))
    print(float(volumeofsphere))

#Program E
#volume of cylinder with diameter:202067.39 and side length :202067.39
#formula v=pi x r** x height 

height=(float(input("Enter height of cylinder please")))
print(float(height))

if height <0:
    print("Length must be >= 0. Please try again")
else:
    radiusofcylinder=(float(height/2))
    print(float(radiusofcylinder))

    volumeofcylinder=(float(math.pi * float(radiusofcylinder * (float(height)))))
    print(float(volumeofcylinder))

