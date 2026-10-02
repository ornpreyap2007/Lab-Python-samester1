number = input("Enter an integer number : ")
if number.isalpha() :
    print("Input must be a number !!")
    exit
else :
    number = int(number)
print("x"* number)
i =0 
while i < (number-2) :
    print("x"+" "*(number-2)+"x")
    i += 1
print("x"*number)
