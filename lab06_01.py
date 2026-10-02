x = input('Enter a comma-seperated list : ').split(",")
if len(x) == 3 :
    a = x[0]
    b = x[1]
    c = x[2]

    print((a, b, c),
    (a, c, b),
    (b, a, c),
    (b, c ,a),
    (c, a, c),
    (c, b, a))
    
else :
    print('Please in enter 3 values !')

