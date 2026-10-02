number = input("Enter an integer number : ")
if number.isalpha() :
    print("Input must be a number !!")
    exit()
else :
    number = int(number)
print("o"*number)
i = number-2
x = 0
while i >= 1 :
    print("o"+" "*(x)+"x"*i+"o")
    i -= 1
    x += 1
print("o"*number)