n = int(input("Enter number of passenger : "))
for i in range(n) :
    print(f"Passnger {i+1}")
    s = input("Enter start station (A , B , C) :")
    d = input("Enter destination station (A , B , C) :")
    dset = ("A,B,C")
    if (s == d) :
        print("invalid route")
    elif s not in dset or d not in dset :
        print("invalid station")
    else :
        price = 0
        if (s== "A" and d =="B") or (s== "B" and d =="A")  :
            price += 20
        elif (s== "B" and d =="C") or (s== "C" and d =="B") :
            price += 30
        elif (s== "C" and d =="B") or (s== "D" and d =="C") :
            price += 40
        print(f'Ticket price {price}')

