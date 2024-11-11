def make_dict(k,v=0):
    if v==0:
        v=[0]*len(k)
    d={}
    for i,j in zip(k,v):
        d.update({i:j})
    return d

print(make_dict([0,1,2],[32,43,55]))
print(make_dict([0,1,2]))