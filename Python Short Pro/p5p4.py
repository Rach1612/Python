#Write a program that takes as input an integer and prints out one of the following messages indicating whether
#the number is in one of the specified ranges:
# Number is equal to 0
# Number is greater than 0 and less than or equal to 20
#Number is greater than 20 and less than or equal to 40
#Number is greater than 40 and less than or equal to 60
#Number is greater than 60 and less than or equal to 80
#Number is greater than 80 and less than or equal to 100
#Number is greater than 100
#If the number entered is less than 0, a message should be printed out to that effect.

number=int(input("please enter a value (int)"))
if int(number) ==0:
    print("number is 0")
elif number >0 and number <=20:
    print("number between 0 and 20")
elif number >20 and number <=40:
    print("number between 20 and 40")
elif number >40 and number <=60:
    print("number between 40 and 60")
elif number >60 and number <=80:
    print("number between 60 and 80")
elif number >80 and number <=100:
    print ("number between 80 and 100")
elif number >100:
    print ("number greater than 100")
elif number < 0:
    print("number less than 0")


