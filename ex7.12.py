l = []
while True : 
    try :
        x = input("Input (DONE = exit) : ")
        if x == "DONE" :
            break
        x = int(x)
        l.append(x)
    except ValueError :
        print('Please enter number!')
print("Sum =",sum(l))