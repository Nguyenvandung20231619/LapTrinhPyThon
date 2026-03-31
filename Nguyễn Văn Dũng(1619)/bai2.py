n = int(input("Nhập n = "))
if n > 10:
    print("Số nhập phải bé hơn 10")
else:
    for i in range(1, n):
        if i % 2 == 0:
            print(i)
 