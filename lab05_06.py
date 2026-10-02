for x in range(5) : 
    n = input("enter a number between 1 and 20 : ")
    if n.isnumeric() :
        n = int(n)
        if 1 <= n <= 20 :
            if n % 2 == 0 :
                print("%d is an even number" %n)
            else :
                print("%d is an odd number" %n)
        else :
            print("number is invalid")
    else :
        print("Invalid input")

    