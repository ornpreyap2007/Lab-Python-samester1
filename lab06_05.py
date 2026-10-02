a = []
b = []
c = []
n = input('how many people in a group? : ')
print("\nplease enter grade from group A")
for i in range(int(n)) :
    x = input("enter grade : ")
    a.append(float(x))
print("\nPlease enter grade from group B")
for i in range(int(n)) :
    x = input("enter grade : ")
    b.append(float(x))
print("\nPlease enter grade from group C")
for i in range(int(n)) :
    x = input("enter grade : ")
    c.append(float(x))
print(f'''\nthe heighest grade of group A is {max(a)}
the heighest grade of group B is {max(b)}
the heighest grade of group C is {max(c)}''')
    

