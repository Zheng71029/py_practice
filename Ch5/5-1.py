t=int(input('請輸入當前氣溫: '))

if t>28:
    print('開冷氣')
elif t<15:
    print('開暖氣')
else:
    print(f'現在溫度為{t}度，不開冷暖氣')