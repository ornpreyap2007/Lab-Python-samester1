rates = {"JPY":0.29,"USD":31.99,"EUR":35.62}
data = []
while True :
    currency_amount = input('Input: ')
    if currency_amount == "end" :
        break
    try :
        currency , amount = currency_amount.split()
    except :
        print('Input must have 2 value')
        continue
    try :
        amount = float(amount)
    except :
        print('Your value must be integer')
        continue
    if amount <= 0 :
        print('ERROR')
        continue
    if currency not in rates:
        print('ERROR')
        continue
    else :
        data.append((currency,amount))
for currency , amount in data :
    thb = amount*rates[currency]
    print(f'{amount:.2f} {currency} is {thb:.2f} THB')
    