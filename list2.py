l=[12,2,5,9,8]
l.extend([15,25])
#del l[5]
l.insert(1,27)
l[1]=100

l.remove(25)
print(l)
print(max(l))
print(len(l))
print(sum(l))
l.sort()
#print(sorted(l))
print(l[-1])
b=[1,2,3]
print(l+b)
print(l*2)
l.insert(5,[12,4,6])
print(l.pop())
print(l)
