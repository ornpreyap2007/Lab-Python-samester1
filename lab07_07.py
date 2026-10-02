even = 0
odd = 0
while True :
    x = input("Enter an integer (0 to exit): ")
    if x == "0" :
        break
    if x.isalpha() :
        print("Input must be a number !!")
    else :
        x = int(x)
        if x % 2 == 0 :
            even += 1
        else :
            odd += 1
print("-"*30)
print("The number of even integers is %d\nThe number of odd integers is %d"%(even,odd))

