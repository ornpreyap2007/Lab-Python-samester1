coins_balance = {'1':0,'2':0,'5':0,'10':0}
deposit = 0
print('Welcome to coin deposit machine')
while True :
    coin = input('Please insert coin: ')
    if coin == "done" :
        break
    if coin not in coins_balance :
        print('Only 1,2,5 and 10 baht coin are allowed')
        continue
    else :
        coins_balance[coin] += 1 
        deposit += int(coin)
    print(f'You inserted {coin} baht coin')
    print(f'Current Balance: {deposit} baht')
print('<-----Deposit Summary----->')
for coins , amount in coins_balance.items() :
    print(f'{coins} baht coins -> {amount}')
print(f'Deposit Amount: {deposit} baht')