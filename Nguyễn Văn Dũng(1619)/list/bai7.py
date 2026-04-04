_list = ['abc', 'xyz', 'abc', '12', 'ii', '12', '5a']
# Loại bỏ phần tử trùng lặp
_new = [x for x in _list if _list.count(x) == 1]
print("Chỉ giữ lại phần tử không bị trùng:", _new)
#giữ lại 1 phần tử duy nhất
_new = list(dict.fromkeys(_list)) 
print("Mỗi phần tử chỉ xuất hiện 1 lần:", _new)