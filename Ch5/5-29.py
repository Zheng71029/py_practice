s = input('請輸入:')
for i in s:
    if not i.isdigit():
        print('輸入的數包含不合法的字元')  
        break   
else:
    print(s)