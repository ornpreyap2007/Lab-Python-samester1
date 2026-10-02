print("Multiplication table :")
n = input("Please enter a number between 1 to 25 : ")
if n.isnumeric :
    n = int(n)
    if 1 < n < 25 :
        print("Multiplication table of %d :" %n)
        for i in range(1,13) :
            print(f'{n} x {i} = {n*i}')
    else :
        print("You entered invalid number")
else :
    print("Please Enter a number!")
