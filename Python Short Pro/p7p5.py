#program to sum integers between 1 and 10,000)
#set running total variable total=0
#set counter for loop i (i in range 1-10000)
#if i in range (1,10000):do 
    #if i divisable by 3 or i divisable by 5: then ...
        #total = total +i  (running total)
        #i =i +1
        #print total 
#finish progam 

#running total =0
total=0

#counter for loop
i=1 

for i in range(1,10000):
    if i % 3 ==0 or i % 5==0:
        total = total + i
        i = i + 1
        print("total is :" + str(total))


