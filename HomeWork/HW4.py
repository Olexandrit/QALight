# fruits = ['apple', 'banana', 'cherry']

# fruits.reverse()

# print(fruits)

a = "AAAACCCGGT"
  # "TGGCCCAAAA"
  #  ACCGGGTTTT

print(a)
print(list(a))

b = list(reversed(a))
print(b)

dic = {'A':'T','T':'A','C':'G','G':'C'}

d = [dic[w] for w in b]
print(d)

c = ''.join(d)
print(c)

# print(b)
# print(''.join(list(a).reverse()))
# print([a[-1*(i+1)] for i in range(len(a))]) 


# b = ACCGGGTTTT