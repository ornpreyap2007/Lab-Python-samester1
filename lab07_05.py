while True :
    x = input("Enter an integer number : ")
    if x.isnumeric() :
        x = int(x)
        if 1 < x < 10 :
            break
        else :
            print("1-10 !!")
    else :
        print("Input must be a number !")
i = 1
while i <= x :
    for j in range(1,i+1) :
        print(j,end=" ")
    print()
    i += 1
i = (x-1)
while i >= 1 :
    for j in range(1,i+1) :
        print(j,end=" ")
    print()
    i -= 1