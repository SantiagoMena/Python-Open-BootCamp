from functools import reduce

numeros = str(input("Ingrese una lista de numeros separados por coma: "))
numerosInputArray = numeros.split(',')
numerosInputArray = filter(lambda x: x.strip(), numerosInputArray)
numerosImpares = filter(lambda x: x if x.isdigit() and int(x) % 2 != 0 else False, numerosInputArray)
sumatoria = reduce(lambda a, b: int(a) + int(b), numerosImpares)

print(f'La sumatoria de los números impares ingresados es: {sumatoria}')