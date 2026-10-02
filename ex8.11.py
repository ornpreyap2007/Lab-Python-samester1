word = {}
while True :
    x = input("Input (DONE = exit) : ")
    if x == "DONE" :
        break
    if x not in word :
        word[x] = 1
    else :
        word[x] += 1 
print("Output : ")
for i in word :
    print(i," = ",word[i])