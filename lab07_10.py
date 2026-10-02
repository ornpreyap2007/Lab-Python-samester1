L = []
while True :
    x = input("Enter an integer (-1 to exit): ")
    if x == "-1" :
        break
    if x.isalpha() :
        print("")
    else :
        x = int(x)
        L.append(x)
print("The sum of 5 number(s) is.",sum(L))