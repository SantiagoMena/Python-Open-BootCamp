from functools import reduce

paises = str(input('Ingresa una lista de paises separados por coma: '))
paisesArray = paises.split(',')
paisesCapitalize = map(lambda x: x.strip().capitalize(), paisesArray)
paisesUnicos = reduce(lambda a, b: a if b in a else f'{a},{b}', paisesCapitalize)
paisesUnicosArray = paisesUnicos.split(',')
paisesOrdenados = sorted(paisesUnicosArray)

print(paisesOrdenados)