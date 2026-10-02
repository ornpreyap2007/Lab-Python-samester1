def CelsiusToFahrenheit(c) :
    f = (c*9/5)+32
    print('The degree in fahrenheit is %.2f'%f)
c = input('Input temperature in degree Celcius: ')
if c.isalpha() :
    print('Your input should be a number!')
    exit()
else :
    c = int(c)
CelsiusToFahrenheit(c)