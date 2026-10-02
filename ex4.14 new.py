d = input("Enter your distance : ")
if d.isnumeric :
    d = int(d)
    if 0 < d < 100 :
        cost = 10
    elif 100 <= d < 150 : 
        cost = 10+5*(d-100)
    elif 150 <= d : 
        cost = 260+7*(d-150)
    print("Your cost is %d" %cost)
else : 
    print("You  distance must be a number!")
