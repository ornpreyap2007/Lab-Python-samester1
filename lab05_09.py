height = input("Height : ")
if height.isnumeric() :
    height = int(height)
    if height < 1 :
        print("Error")
    elif height == 1 :
        print(".")
    else :
        for x in range(1,height+1) :
            h = "#"*(height-x)
            d = "."*(2*x-1)
            print(h+d+h)
else :
    print("Error")