#for this program we will be matching towns/cities with the province in which there are located. 
#


a , b, c, d, e, f, g, h, i, j, = "Dublin", "Belfast", "Cork","Limerick", "Derry", "Galway", "Lisburn", "Kilkenny", "Waterford","Sligo"

towncity=(input("Please enter a name of city or town in Ireland"))
print(towncity)


if towncity==c or towncity==d or towncity==i:
    print("town/city you have entered is in Munster")
elif towncity==a or towncity==h:
    print("town/city you have entered is in Lenster")
elif towncity==g or towncity== b or towncity==e:
    print("town/city you have entered is in Ulster")
elif towncity==f or towncity==j:
    print("town/city you have entered is in connaught")
else:
    print("answer is not known please try again")

