points = 100
while True :
    x = input('Command: ')
    if x == "done 0" :
        break
    try :
        type , value = x.split()
        value = int(value)
    except ValueError :
        print('Invalid command')
        continue
    if value <= 0 :
        print('Invalid command')
        continue
    if type == "P" :
        point = value//50
        points += point
        print('You earned %d points'%point)
        print('Your accumulated points = %d points'%points)
        continue
    elif type == "R" :
        if value > points :
            print('Not enough points')
            continue
        else :
            points -= value
            print('You redeemed %d points'%value)
            print('Your accumulated points = %d points'%points)
            continue
    else:
        print('Invalid command')

