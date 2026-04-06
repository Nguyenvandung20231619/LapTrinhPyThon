_tuple = ('ab', 'b', 'e', 'c', 'd', 'e', 'ab')
tui_loc = []

for phan_tu in _tuple:
    if phan_tu not in tui_loc:
        tui_loc.append(phan_tu)

_new_tuple = tuple(tui_loc)

print(" _new_tuple:", _new_tuple)