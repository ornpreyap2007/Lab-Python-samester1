print("="*20+"\nCashier Program\n"+"="*20)
print()
l = []
i = 0
while True :
    x = input("Enter item price or -1 when finished: ")
    if x == "-1" :
        break
    if x.isalpha() :
        print("Please enter price an a number!!!")
    else :
        x = float(x)
        l.append(x)
        i += 1
print("\nTotal purchase amount is",sum(l))
while True :
    cash = input("\nYour payment : ")
    if cash.isalpha():
        print("Please enter you payment as a number !!")
    else:
        cash = float(cash)
        break
print(f"\nYou bought {i} items today.\nYour change is {cash-(sum(l)):.2f} baht.")

        
