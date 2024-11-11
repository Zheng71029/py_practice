n=int(input('請輸入一個數: '))

if n == 0:
    c=1
else:
    c = 0
    
while n > 0:
    n //= 10
    c += 1

print(c)