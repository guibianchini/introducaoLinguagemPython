#List Comprehension
"""
x = [1,2,3,4,5]
y = []

for i in x:
    y.append(i**2)

print(x)
print(y)
"""
x = [1,2,3,4,5]
# [valor_a_adicionar | laço | condicao]
y = [i**2 for i in x]
z = [i for i in x if i%2==1]
print(z)
