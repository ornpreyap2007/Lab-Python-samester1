n = input("enter no. of lines : ")
if n.isnumeric() :
    n = int(n)
    if n > 1 :
        for i in range(1,n+1) :
            if i%2 == 0 :
                print("*"*i)
            else :
                print("-"*i)
    else :
        print("Error")
else :
    print("Please number for lines")

