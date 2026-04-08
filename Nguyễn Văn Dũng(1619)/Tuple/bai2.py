_tuple = ('ab', 'b', 'e', 'c', 'd', 'e', 'ab')
ket_qua_list = []

for phan_tu in _tuple:
    so_lan_xuat_hien = _tuple.count(phan_tu)
    if so_lan_xuat_hien == 1:
        ket_qua_list.append(phan_tu)

_new_tuple = tuple(ket_qua_list)

print(" _new_tuple:", _new_tuple)