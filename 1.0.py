item_price = {}
while True :
    items = input('Enter item and price: ')
    if items == "done 0" :
        break
    item , price = items.split()
    if not item.isalpha :
        print('Input validation !')
        continue
    if not price.isnumeric :
        print('Price must be integer !')
        continue
    price = int(price)
    if not (1 <= price <= 1000) :
        print('Price must be between 1-1000 !')
        continue
    if item not in item_price :
        item_price[item] = price
    else :
        print('item is already recorded !')
if len(item_price) == 0 :
    print('No item recorded !')
else :
    print('Output :')
    for key , value in item_price.items() :
        print(key,":",value)
    print(f'''Number of items : {len(item_price)}
    Total price : {sum(item_price.values())}
    Average price : {sum(item_price.values())/len(item_price):.2f}''')
