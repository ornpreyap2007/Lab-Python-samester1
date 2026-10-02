while True:
    num = int(input("Enter an integer number (0 to exit): "))

    if num == 0:
        print("Exit program. Bye!")
        break

    if num < 0 or num > 9:
        print("Valid value is between 0 and 9!")
        break

    # ทำสามเหลี่ยมแบบ centered
    for i in range(1, num + 1):
        # จำนวนช่องว่างด้านหน้า
        spaces = num - i
        print(" " * spaces, end="")
        
        # พิมพ์เลข
        for j in range(i):
            print(num, end=" ")
        print()  # ขึ้นบรรทัดใหม่

    print()  # เว้นบรรทัดตามโจทย์