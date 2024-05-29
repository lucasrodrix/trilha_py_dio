def gerador(numeros:list[int]):
    for numero in numeros:
        yield numero * 2

for i in gerador(numeros=[2,4,6]):
    print(i)