def gen(n):
    a=1
    while a<=n:
        if a%3==0 and a%5!=0:
            yield a
        a+=1

print(list(gen(10)))