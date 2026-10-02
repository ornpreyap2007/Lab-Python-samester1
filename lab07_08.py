while True :
    x = input("Enter an integer number ('x' to exit) : ")
    if x == "x" :
        break
    if x.isdigit():
        x = int(x)
        for i in range(x) :
            for j in range(x) :
                if i == j or i+j == x-1 :
                    print("x",end=" ")
                else:
                    print(".",end=" ")
            print()
    else :
        print()
    print()
       