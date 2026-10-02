i = input("Input : ")
if len(i) != 9 :
    print("Error")
else :
    valid = True
    for x in i :
        if (x != "X") and (x != "O") and (x != ".") :
            valid = False
    if valid == False :
        print("Error")
    else :
        print("-------")
        for xo in range(0,9,3) :
            print("|"+i[xo]+"|"+i[xo+1]+"|"+i[xo+2]+"|")
            print("-------")
            