frutas = ("laranja", "pera", "uva",)
letras = tuple("python")
numeros = tuple([1, 2, 3, 4])
pais = ("Brasil",)

print(frutas)
print(letras)
print(numeros)
print(pais)

print(frutas[0])
print(frutas[-1])
print(numeros[0])

matriz =(
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 9),
)

print(matriz)
print(matriz[0])
print(matriz[0][0])
print(matriz[0][-1])
print(matriz[-1][-1])
print(matriz[1][1])

carros = ("gol", "celta", "palio",)

print(carros[2:])
print(carros[:2])
print(carros[1:3])
print(carros[0:3:2])
print(carros[::])
print(carros[::-1])

for carro in carros:
    print(carro)

print(carros.count("celta"))
print(carros.count("gol"))

print(carros.index("palio"))

print(len(carros))

motos = ("Start")
print(isinstance(motos, tuple))