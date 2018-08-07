print("Lesson2")

from time import time as t

n = range(10 ** 4)

t1 = t()
l1 = []
for i in n:
    l1.append(i)
print("l1=", t() - t1)

# t2 = t()
# l2 = []
# for i in n:
#   l2.insert(0,i)
# print(t()-t2)

# t4 = t()
# print(-1 in l1)
# print(t()-t4)

t1 = t()
d1 = {}
for i in n:
    d1[i] = 1
# print(d1)
print("d1=", t() - t1)

t3 = t()
for i in n:
    -1 in l1
print("fl1=", t() - t3)

t4 = t()
for i in n:
    -1 in d1
print("fd1=", t() - t4)

# list1 = []
# list2 = []
# list3 = []

# for i in range(2,10):
#   list1.append(i)

# for j in range(2,10):
#   list2.append(j)

# for i in list1:
#   for j in list2:
#     list3.append(i*j)

# print(list3)

# r = range(2,10)
# print([i*j for i in r for j in r])

# print(list(range(5)))

# for i in range(2,10):
#   for j in range(1,10):

#     # print('{0} * {1} = {2}'.format(i, x, i*x))
#     print(i,'*',j,'=',i*j)

# print(0 ^ 1)

# name = ''
# print(name or 'No name')

# print(5 and '5' and [] and {1: 'HI!'})
# print(' ' or {} or () or 0.001)

# # CRUID
# l = [1]
# print(l)
# print(l[0])
# l[0] = 0
# del l[0]
# del l

# d={1:1}
# print(d)
# print(d[1])
# d[0] = 0
# print(d[0])
# print(d)
# del d[1]
# del d