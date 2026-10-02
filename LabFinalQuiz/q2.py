n = input("Input :")
if n.isnumeric() :
    n = int(n)
    if 1 <= n <= 15 :
        for x in range(1,n+1) :
            for i in range(1,n+1) : 
                print(x, end="\t")
                print()
            
            

    else : 
        print("Invalid input")
else :
    print("Invalid input")