#save correct password correctpassword="HiRachel"
# user input to store passwords which entered 
#conditional statement If password correct:
    #do the following : print (you have sucessfully logged in)
    #and terminate program
#or else : (any other password or sequence of character inputted) 
#print : sorry the password is wrong please enter correct password 3 times
# while loop 
#Limit = 3 
#count =0 
#while count<3 : do 
#ask for password
#count +=1 -logging correct password number 1 
#repeat while loop until count =3 :
#then go back an indent print "you have sucessfully logged in"
#finish program


correctpassword=("HiRachel")
passwordentered=(input("Enter your password please"))
if passwordentered==correctpassword:
    print("You have successfully logged in.")
elif passwordentered !=correctpassword:
    print("sorry the password is wrong please enter correct password 3 times")
    passwordentered=(input("Enter your password please")) 
    if passwordentered != correctpassword:
        print("you have been denied access")
    else:
        count=1
        while count<3:
            if passwordentered==correctpassword:
                count=count+1
                print(count)
                passwordentered=(input("Enter your password please"))
        print("you have sucessfully logged in")
        



    
