items = {'bag':150,'shoe':600,'shirt':250,'pants':400}
list_item = []
total = 0
while True :
    item_b = input('Input: ')
    if item_b == "done" :
        break
    if item_b not in items :
        print('invaid item')
        continue
    while True :
        amount = input('Input: ')
        try :
            amount=int(amount)
        except ValueError :
            print('amout must be integer')
            continue
        price = amount*items[item_b]
        total += price
        list_item.append((item_b,amount,price))
        break
print(list_item)
print(f'Total = {total}')
if total>1000 :
    extra = total-1000
else :
    extra = 0
print(f'extra payment = {extra}')


