h,m,s = input("Input : ").split(":")
if h.isnumeric() and m.isnumeric() and s.isnumeric() :
    h,m,s = int(h),int(m),int(s)
    sum = 0 
    if (0 <= h <= 23) and (0 <= m <= 59) and (0 <= s <= 59) :
            sum = (h*3600)+(m*60)+s
            print(f"The number of seconds = {sum}")
    else : 
        print("Invalid time")
else :
    print("Invalid time")
