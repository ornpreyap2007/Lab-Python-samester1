c = input("Enter the number of customers: ")
if c.isnumeric() :
    c = int(c)
    for x in range(1,c+1) :
        n = input(f'Enter the name of customer {x} : ')
        s = input(f'Enter the spending amount for {n} : ')
        if s.isnumeric() :
            s = int(s)
            if s < 500 :
                d = 0
            elif 500 <= s <= 999 :
                d = 0.05
            elif 1000 <= s <= 1999 : 
                d = 0.10
            else : #s>=2000
                d = 0.15
            print(f"{n} paid {s-(s*d):.2f} Baht")
        else :
            print("Please enter spending amount as a number.")
else :
    print("Please enter the number of customers as a number.")
