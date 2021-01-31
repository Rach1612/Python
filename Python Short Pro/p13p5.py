#program to illustrate scoping in Python

#add in variable j - 
#add + operator to line : j=j+y 
def f (x):
    print("in function f:")
    x+=1
    y=1
    print("x is", x)
    print("y is", y)
    print("z is", z)
    print("j is", j)
    return x




x, y, z, j = 7, 8, 9,10
print("Before function f:")
print("x is", x)
print("y is,", y)
print("z is" , z)
j=j+y
print("j is", j)

z = f ((x))
print("After function f:")
print("x is", x)
print("y is", y)
print ("z is", z)
j=j+y
print("j is", j)

