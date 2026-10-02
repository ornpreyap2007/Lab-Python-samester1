print("Welcome to the BMI Category Checker! \n==================================")
w,uw = input("Please insert the weight and its unit (kg or lbs): ").split()
h,uh= input("Please insert the height and its unit (cm , m, ft, in): ").split()
print("==================================")
if (uw == "kg" or uw == "lbs") and (uh=="cm" or uh == "m" or uh == "ft" or uh == "in"):
    w,h = float(w) , float(h)
    weight, height = 0 , 0
    if (uw == "kg" or uw == "lbs") :
        if uw == "lbs" :
            weight = w / 2.20462 
        elif uw == "kg" :
            weight = w
    if (uh=="cm" or uh == "m" or uh == "ft" or uh == "in") :
        if uh == "cm" :
                height = h / 100
        elif uh == "ft" :
                height = h / 3.28084
        elif uh == "in" :
                height = h / 39.3701
        elif uh == "m" :
                height = h
    bmi = weight/height**2
    if bmi < 17 :
        d = "You are underweight."
    elif 17 <= bmi < 18.5 :
        bmir = "Underweight (Mild thinness)"
        d = "You are slightly underweight"
    elif 18.5 <= bmi < 25 :
        bmir = "Normal range"
        d = "Great! Your BMI is in the normal range."
    elif 25 <= bmi < 30 :
        bmir = "Overweight (Pre-obese)"
        d = "Your BMI is in the overweight range."
    elif bmi >= 30 :
        bmir = "Obese"
        d = "Your BMI is in the obese range."

    print(f'''Your BMI : {bmi:.2f}.
    Category : {bmir}
    Description : {d}''')

else :
    print("Error:Invalid unit.") 


