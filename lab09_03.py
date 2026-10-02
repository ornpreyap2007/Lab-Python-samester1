def UserInput() :
    xList = []
    while True :
        UserInput = input('Enter an input: ')
        if UserInput == "Done":
            break
        if not UserInput.isnumeric() :
            print('Error')
            exit()
        else :
            UserInput = int(UserInput)
            xList.append(UserInput)
def SumOut(xList) :
    return sum(xList)
def MinOut(xList) :
    return min(xList)
def MaxOut(xList) :
    return max(xList)
xList = UserInput()
print('The summation is',SumOut(xList))
print('The minimum is',MinOut(xList))
print('The maximum is',MaxOut(xList))