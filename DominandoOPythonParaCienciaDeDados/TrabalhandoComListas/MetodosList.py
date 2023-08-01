lista = []
lista.append(1)
lista.append("Python")
lista.append([40, 30, 20])
lista.append("Python")

print(lista) # [1, 'Python', [40, 30, 20], 'Python']

listanova = lista.copy()

lista.clear()
print(lista) # []
print(listanova) # [1, 'Python', [40, 30, 20], 'Python']
print(listanova.count("Python")) # 2


linguagens = ["python", "C", "JS"]
print(linguagens) # ['python', 'C', 'JS']
linguagens.extend(["C++", "C#", "Java", "C#"])
print(linguagens) # ['python', 'C', 'JS', 'C++', 'C#', 'Java', 'C#']
print(linguagens.index("C#")) # 4

print(linguagens) # ['python', 'C', 'JS', 'C++', 'C#', 'Java', 'C#']
linguagens.pop()
print(linguagens) # ['python', 'C', 'JS', 'C++', 'C#', 'Java']
linguagens.pop(1)
print(linguagens) # ['python', 'JS', 'C++', 'C#', 'Java']

linguagens.remove("JS")
print(linguagens) #['python', 'C++', 'C#', 'Java']

linguagens.reverse() 
print(linguagens) # ['Java', 'C#', 'C++', 'python']

linguagens.sort()
print(linguagens) # ['C#', 'C++', 'Java', 'python']

linguagens.sort(key=lambda x: len(x)) # Tamanho das palavras
print(linguagens) # ['C#', 'C++', 'Java', 'python']

linguagens.sort(key=lambda x: len(x), reverse=True) # Tamanho das palavras
print(linguagens) # ['python', 'Java', 'C++', 'C#']

print(len(linguagens)) # 4

print(sorted(linguagens, key=lambda x: len(x), reverse=True)) # ['python', 'Java', 'C++', 'C#']

print(sorted(linguagens, key=lambda x: len(x))) # ['C#', 'C++', 'Java', 'python']

print(sorted(linguagens)) # ['C#', 'C++', 'Java', 'python']

print([n**2 if n > 6 else n for n in range(10) if n % 2 == 0])