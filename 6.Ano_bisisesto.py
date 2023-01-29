def isBisiesto(year: int) -> bool:
    return year % 4 == 0

year = int(input('Ingrese un año: '));

if(isBisiesto(year)):
    print('El año' + str(year) + ' es bisisesto')
else:
    print('El año' + str(year) + ' no es bisisesto')