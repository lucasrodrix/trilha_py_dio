numeros = [1, 30, 21, 2, 9, 65, 34]
# pares = []

#Filtro 1
# for numero in numeros:
#     if numero % 2 == 0:
#         pares.append(numero)
        
pares = [numero for numero in numeros if numero % 2 == 0]

# Modificar valores
numeros = [1, 30, 21, 2, 9, 65, 34]
quadrado = []
for numero in numeros:
    quadrado.append(numero ** 2)

quadrado = [numero**2 for numero in numeros]
print(numeros)
print(quadrado)