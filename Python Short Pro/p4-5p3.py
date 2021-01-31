#this program takes amount of income inputted by the user 
#it then divides it 60:40
#tax rate is 23% on larger amount 
#tax rate is 41% on smaller amount 
#program will then print out total amount due (inital amount plus taxes)

grossamount=(float(input("Please enter grossamount to be converted into gross amount? ")))
print (float(grossamount))

if grossamount <0:
    print("Amount of income must be >= 0. Please try again")

else :
    onepart=int(float(grossamount))/5
    print(float(onepart))

    applytaxrate1=onepart*3 #identifying tax group one the larger amount
    print(applytaxrate1)

    applytaxrate2=onepart*2 #identifying tax group two the smaller amount
    print(applytaxrate2)

    tax_payable_l=applytaxrate1/100*23 #identifying total tax for larger amount 
    print(tax_payable_l)

    tax_payable_s=applytaxrate2/100*41  #identifying total tax for smaller amount 
    print(tax_payable_s)

    total_tax_payable=tax_payable_l + tax_payable_s #calcualting total tax payable 
    print(total_tax_payable)

    total_amount_payable=grossamount - total_tax_payable #subtracting total tax due plus intial figure to get overall amount due. 
    print(total_amount_payable)

