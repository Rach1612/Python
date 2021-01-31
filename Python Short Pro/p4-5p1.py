#currencies choosen that baht and euro 
#exchange rate = 36.79 (todays exchange rate)


euroamount=(float (input("Please enter amount in Euro you would like to convert to Thai Baht (amount cannot be a negative number for program to run)")))
print(float(euroamount))
if euroamount <0:
    print("Amount must be >= 0. Please try again")
else:
    thaibahtamount=euroamount * 36.79
    print("thank you, in thai baht this amount is converted to " + str(float(thaibahtamount)))

