frutas = ["Laranja", "Maçã", "Uva"]
frutas2 = []
letras = list("python")
numeros = list(range(10))
carro = ["Ferrari", "f8", 4200000, 2020, "Mulungu", True]

print(frutas)
print(frutas2)
print(letras)
print(numeros)
print(carro)

print(frutas[0])
print(frutas[2])
print(frutas[-1])

matriz =[
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matriz)
print(matriz[0])
print(matriz[0][0])
print(matriz[0][-1])
print(matriz[-1][-1])
print(matriz[1][1])


carros = ["gol", "celta", "palio"]

for carro in carros:
    print(carro)

numeros2 = list(range(20))
pares = []
for numero in numeros2:
    if numero % 2 == 0:
        pares.append(numero)
    
print(pares)

numeros3 = list(range(20))
impares = [numero for numero in numeros3 if numero % 2 == 1]
print(impares)