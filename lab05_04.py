n = input("Enter an integer number (n>0) : ")
print("""(1) Factorial of n (n!)
(2) Summation of n integers""")
s = input("Select oparation : ")
if n.isnumeric() :
    n=int(n)
    if n > 0 :
        if s == "1" :
            sum = 1 
            for i in range(1,n+1) :
                sum *= i
            print("Factorial of n (n!) = %d" %sum)
        elif s == "2" :
            sum = 0 
            for i in range(1,n+1) :
                sum += i
            print("Summation of n  integers = %d" %sum)
    else :
        print("N/A Operation!")
else :
    print("N/A Operation!")