#programm to check password and deny access if incorrect password used 3 times. 

#correct password=HiRachel - saved in variable
#user input to store passwords which entered 
#conditional statement If password correct:
    #do the following : print (you have sucessfully logged in)
    #and terminate program
#or else : (any other password or sequence of character inputted) 
#while loop 
#Limit = 3 
#count =1 
#while count<3 : do 
#print incorrect password try again
#count +=1 -logging wrong password number 1 
#repeat while loop until count =3 :
#then go back an indent print "you have been denied access"
#finish program



correctpassword=("HiRachel")
passwordentered=(input("Enter your password please"))
if passwordentered==correctpassword:
    print("You have successfully logged in.")
else:
    count=1
    while count<3: 
        print("incorrect password try again!")
        count += 1
        passwordentered=(input("Enter your password please"))
    print("you have been denied access")







