l = []
while True :
    x = input("Input: Enter a word: ")
    if x == "exit" :
        break
    if x[-1] == "y" :
        l.append(x[:-1] + "ily")
    else :
        l.append(x)
print("output :",l)
