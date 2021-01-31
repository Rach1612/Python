Game=0
for i in range(0,101,1):
    if Game %5 ==0 and Game %3 ==0:
        print("FizzBuzz")
    elif Game %3 ==0:
        print("fizz")
    elif Game %5 ==0:
        print ("Buzz")
    else:
        print(Game)
    Game=Game +1 
