ITS = float(input("enter grade from ITS100 :"))
EL = float(input("enter grade from EL171 :"))
SCS = float(input("enter grade from SCS183 :"))

print(f'''
Your GPA is {((ITS*3)+(EL*3)+(SCS*1))/7:.2f}
        ''')