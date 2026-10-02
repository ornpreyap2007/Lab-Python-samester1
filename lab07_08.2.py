while True :
    x = input("Enter an integer number ('x' to exit): ")
    if x == "x" :
        break
    if x.isalpha() :
        print()
    else :
        x = int(x)
        for i in range(x) :
            for j in range(x) :
                if i == 0 or i == x-1 or j == 0 or j == x-1 :
                    print("#",end="")
                else :
                    print(".",end="")
            print()
        print
