namelist = ['Satawat','Pisit','Thanaphong','Pished','Nut','Amon']
for i in range(6) :
    print('Student list:',namelist)
    x = input("Please enter a student's name that you want to delete (q=exit) : ")
    if x == "q" :
        exit()
    n = input(f"You will remove '{x}' from this class.\nPlease type (Confirm 'y',Cancel 'n') : ")
    if n == "y" :
        namelist.remove(x)
        print()
    if n == "n" :
        print()
