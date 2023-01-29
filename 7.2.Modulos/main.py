import time

HORA_DE_SALIDA = 18

currentTime = time.localtime(time.time())
currentHourTime = currentTime.tm_hour
print('La hora es:', currentHourTime)

if(currentHourTime >= HORA_DE_SALIDA):
    print('Es hora de salir!')

