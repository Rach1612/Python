#program to sum integers up to 5,000
#set running total variable total=0
#set count count =1 
#while count<=5000 :do 
    #total=total + count (collecting running total)
    #count=count+1 (continuing to use next integer)
    #print total = print running total until count = 5000 
#finish progam 



#running total =0
total=0

#counter for loop
count=1 

while count <= 5000:
    count = count + 1
    if count % 3 ==0 and count %5 ==0:
        total = total + count
        print("total is :" + str(total))


#running total =0
total=0

#counter for loop
count=0 

while count <= 30:
    count = count + 1
    if count % 3 ==0 and count %5 ==0:
        total = total + count
        print("total is :" + str(total))

