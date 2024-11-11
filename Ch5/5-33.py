lst = ['Spring','Summer','Autumn','Winter']

a = [i for s in lst for i in s if i in 'aeiouAEIOU']

print(a)