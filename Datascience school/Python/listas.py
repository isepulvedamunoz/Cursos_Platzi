a = [1,2,3]
b = a
print(id(b))
print(a)
print(id(b))
print(b)

my_list = list(range(100))
print(my_list)

pares = [i for i in my_list if i % 2 == 0]
print(pares)