'''
1 no index in set
2 set never accept dublicate values
3 its try to arrange in accesnding oreder

methods

1 add()
2 clear()
3 copy()
4 difference()
5 difference_update()
6 discard()
7 intersection()
8 pop()
9 remove()
10 union()
11 update()'''

a={12,2,3,4,2}

print(type(a))
a.add(14)
y=a.copy()
y.add(20)
print(a,y)
b={12,2,3,40}
print(a,b)
c={101,102,103}
'''a.difference_update(b)
print(a)
a.intersection_update(b)
print(a)'''

print(a.isdisjoint(c))
print(a.issuperset(b))
#a.remove(2)
#print(a)
'''a.symmetric_difference_update(b)
print(a)'''

l=[1,5,8]
z=a.update(l)
print(a)






