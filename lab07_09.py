while True: 
    print("="*5+"MAIN MENU"+"="*5+"\n1. Addition\n2. Subtraction\n3. Exit\n")
    x = input("Select an operation (1-3): ")
    if x == "3" :
        print("Bye !!!")
        exit()
    a,b = input("Enter two numbers: ").split()
    if a.isalpha() or b.isalpha() :
        print("Please enter number")
        exit()
    else :
        a,b = int(a) ,int(b)
    if x == "1" :
        print(f"{a} + {b} = {a+b}\n")
    elif x == "2" :
        print(f"{a} - {b} = {a-b}\n")
    


