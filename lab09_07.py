def TriArea(h,b) :
    a = (1/2)*h*b
    print('The area of the triangle is %.1f'%a)
    
h = input('Enter the height(h): ')
b = input('Enter the base (b): ')
if h.isalpha() or b.isalpha() :
    print('The input must be a number!')
    exit()
else :
    h,b = float(h),float(b) 
TriArea(h,b)
