_list=["Python", "Java", "C++", "JavaScript","10"]
n = int(input("Nhập số n: "))
for i in range(len(_list)):
    if len(_list[i]) > n:
        print(_list[i])
