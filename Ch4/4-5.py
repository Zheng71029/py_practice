#a
lst = [43, 12, 12, 34]
lst.extend([2, 12])
print(lst.count(12))

#b
lst = [43, 12, 12, 34]
lst.append([25, 99])
print(lst)

#c
lst = [43, 12, 12, 34]
lst.insert(2, 65)
print(lst)

#d
lst = [43, 12, 12, 34]
lst.remove(12)
lst.remove(12)
print(lst)

#e
lst = [43, 12, 12, 34]
lst.sort(reverse=True)
print(lst)

#f
lst = [43, 12, 12, 34]
lst.pop(-1)
lst.pop(2)
print(lst)