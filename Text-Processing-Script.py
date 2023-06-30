txt = input()
txt_2 = txt.lower().replace('a', '').replace('e', '').replace('i', '').replace('o', '').replace('u', '')
txt_3 = '.'.join(txt_2)
txt_4 = '.' + txt_3
print(txt_4)
