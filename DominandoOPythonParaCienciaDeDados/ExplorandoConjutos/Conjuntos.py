print(set([1, 2, 2, 3, 5, 5, 8])) # {1, 2, 3, 5, 8}
print(set("abaxaci")) # {'b', 'c', 'i', 'a', 'x'}
print(set(("Palio", "Palio", "gol", "celta"))) # {'gol', 'Palio', 'celta'}
print(set({"java", "Python", "js", "Python"})) # {'js', 'java', 'Python'}

numeros = {1, 2, 3, 4, 4, 4, 7, 8, 9}
print(numeros)
numeros = list(numeros)
print(numeros[3])


for numero in numeros:
    print(numero)

for index, carro in enumerate(numeros):
    print(f"{index}: {carro}")

conjunto_a = {1, 2, 3}
conjunto_b = {3, 4, 5, 1, 2}
conjunto_c = {10, 0}

print(conjunto_a.union(conjunto_b)) # {1, 2, 3, 4, 5}

print(conjunto_a.intersection(conjunto_b)) # {3}

print(conjunto_a.difference(conjunto_b)) # {1, 2}
print(conjunto_b.difference(conjunto_a)) # {4, 5} 

print(conjunto_a.symmetric_difference(conjunto_b)) # {1, 2, 4, 5}


print(conjunto_a.issubset(conjunto_b))
print(conjunto_b.issubset(conjunto_a))

print(conjunto_a.issuperset(conjunto_b))
print(conjunto_b.issuperset(conjunto_a))

print(conjunto_a.isdisjoint(conjunto_b))
print(conjunto_b.isdisjoint(conjunto_a))
print(conjunto_b.isdisjoint(conjunto_c))

sorteio = {1, 230}
sorteio.add(25)
print(sorteio)
sorteio.add(25)
print(sorteio)
sorteio.add(55)
print(sorteio)
sorteio.discard(25)
print(sorteio) 
print(1 in sorteio)