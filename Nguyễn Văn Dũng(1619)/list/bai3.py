_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
list_chan = []
list_le = []

for x in _list:
    if x % 2 == 0:
        list_chan.append(x)
    else:
        list_le.append(x)

print("Các số chẵn:", list_chan)
print("Các số lẻ:", list_le)