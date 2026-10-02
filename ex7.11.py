while True :
    try :
        x = int(input('input : '))
        if x < 0 :
            break
    except ValueError :
        print("Enter number !")