y = int(input("Enter a year : "))

if y % 400 == 0 :
    print("leap year")
elif y % 100 == 0 :
    print("Not a leap year")
elif y % 4 == 0 : 
    print("leap year")
else :
    print("Not a leap year")