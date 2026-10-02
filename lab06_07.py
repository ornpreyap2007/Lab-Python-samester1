import random as r
words = []
for i in range(4) :
    x = input('Enter string#%d:'%(i+1))
    words.append(x)
ans = r.shuffle(words)
print('Random order of sentence :',end="")
for j in words :
    print(j,end=" ")
