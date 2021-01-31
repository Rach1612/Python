#Write a program that takes as input a floating-point number and prints out whether the number is positive,
#negative or equal to 0 (Use the if ... elif ... else construct).

number=float(input("please enter a value (float)"))
if number >0:
    print("number is positive")
elif number==0:
    print("number is equal to 0")
else:
    print("number is negative")
    