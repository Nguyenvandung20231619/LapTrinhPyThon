a = float(input("Nhập cạnh a: "))
b = float(input("Nhập cạnh b: "))
c = float(input("Nhập cạnh c: "))

if a + b > c and a + c > b and b + c > a:
    print("Độ dài ba cạnh tam giác")
else:
    print("Đây không phải độ dài ba cạnh tam giác")