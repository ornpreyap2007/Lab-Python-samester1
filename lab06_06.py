x = input("\nEnter dd/mm/yyyy: ")
if len(x) == 8 :
    if 0 < int(x[0:2]) <= 31 : print(end="")
    else :
        print("Error ! There're 1-31 days")
        exit()
    if 0 < int(x[2:4]) <= 12 : print(end="")
    else :
        print("Error ! There're 12 months")
        exit()
else :
    print("Please enter 8 digits!!")
    exit()
print(f'''Date = {x[0:2]}
Month = {x[2:4]}
Year = {(int(x[4:8]))-543}''')