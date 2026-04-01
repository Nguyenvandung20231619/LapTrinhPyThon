
n = int(input("Nhập vào số nguyên dương n: "))
if n <= 1:
    print("không phải số nguyên tố")
else:
    is_prime = True
    i = 2
    while i * i <= n:
        if n % i == 0:
            is_prime = False
            break 
        i += 1
        
    if is_prime:
        print("Đây là số nguyên tố")
    else:
        print("không phải số nguyên tố")