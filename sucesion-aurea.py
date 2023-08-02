import math

array_inicial = [1, 1.618, 2.618, 4.236]
print("Números iniciales:", array_inicial)

phi = (1 + (math.sqrt(5))) / 2

cant_numeros_siguientes = int(input('Ingrese la cantidad de números que desea conocer en la sucesión dada: '))

for i in range(cant_numeros_siguientes):
    elemento_siguiente = array_inicial[-1] * phi
    array_inicial.append(round(elemento_siguiente, 4))

print("Los números de la sucesión ahora son: ", array_inicial)

