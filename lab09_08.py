def myRange(FirstVal, UpperBound, StepSize) :
    a = list(range(FirstVal,UpperBound,StepSize))
    print('Range = ',a )

FirstVal = input('Enter the first number: ')
UpperBound = input('Enter the upper bound: ')
StepSize = input('Enter the step: ')
if FirstVal.isalpha() or UpperBound.isalpha() or StepSize.isalpha() :
    print('Input must be a number!')
    exit()
else :
    FirstVal, UpperBound, StepSize = int(FirstVal) , int(UpperBound) , int(StepSize)
myRange(FirstVal, UpperBound, StepSize)