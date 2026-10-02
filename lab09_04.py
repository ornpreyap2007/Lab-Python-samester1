def UserInput() :
    weight = input('Input your weight (kilogram) : ')
    height = input('Input your height (meter) : ')
    if weight.isalpha() or height.isalpha() :
        print('Error')
        exit()
    height ,weight = float(weight) , float(height)
    return weight, height
def FindBMI(hh,ww) :
    return (ww)/(hh**2)
def ShowBMI(MyBMI) :
    print('The user BMI is %.2f'%MyBMI)
hh,ww = UserInput()
MyBMI = FindBMI(hh,ww)
ShowBMI(MyBMI)
