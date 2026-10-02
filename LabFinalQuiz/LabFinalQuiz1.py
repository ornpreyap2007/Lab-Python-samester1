balance = input('Enter the initial balance : ')
if not balance.isnumeric() :
    print('Invalid balance !')
    exit()
balance = int(balance)
while True :
    type_amount = input('Transaction type and amount ("done 0" to exit): ')
    if type_amount == "done 0" :
        break
    try :
        type,amount = type_amount.split()
    except ValueError :
        print('Invalid input !')
        continue
    if type not in ['D','W'] :
        print('Invalid transaction!')
        continue
    if not amount.isnumeric() :
        print('Invalid transaction!')
        continue
    amount = int(amount)
    if amount < 0 :
        print('Invalid transaction!')
        continue
    if type == "D" :
        balance += amount
        print('> Deposit = %d THB, current balance = %d THB.'%(amount,balance))
    else :
        if amount > balance :
            print('Invalid transaction!')
        else : 
            balance -= amount
            print('> Withdrawal = %d THB, current balance = %d THB.'%(amount,balance))
print('> Current balance = %d THB.'%balance)

