# leap year (John's algorithm)
#algorithm below : 
#Prompt the user for a year
# Read the year
# ifyear>=0then:
# if(year % 4 = 0 and year % 100 != 0)
#   or year % 400 = 0 then 
# Print(“Year is a leap year”) 
# else Print(“Year is not a leap year”)
# else:
#   Tell the user that the year must be> 0
# Program finishes

year=int(input("Enter a year")) #propt user for a year and store it as variable "year"
if year >0:
    if year % 4 !=0 and year %100 !=0 or year % 400 ==0:
        print("this is not a leap year")
    else:
        print("this is a leap year") 
else:
    print("Year must be greater than 0")
print ("finished!")





