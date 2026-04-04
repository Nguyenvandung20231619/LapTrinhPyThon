_list = ['abc', 'xyz', 'aba', '1221', 'ii', 'ii2', '5yhy5']
n = int(input("Nhập số n: "))
count = 0

for s in _list:
    if len(s) >= n and s[0] == s[-1]:
        count += 1

print("Số lượng chuỗi thỏa mãn:", count)