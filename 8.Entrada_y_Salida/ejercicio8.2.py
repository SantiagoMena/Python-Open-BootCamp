import pickle

class Vehiculo:
    tipo: str = None
    color: str = None
    ruedas: int = None

    def __init__(self, **args) -> None:
        self.tipo = args['tipo']
        self.color = args['color']
        self.ruedas = args['ruedas']

moto = Vehiculo(tipo='Moto', color='Rojo', ruedas=2)

fileDir = __file__
arrayDir = fileDir.split('/')
arrayDir.pop()
dir = '/'.join(arrayDir)

f = open(dir + '/moto.bin', 'wb')
pickle.dump(moto, f)
f.close()

f = open('moto.bin', 'rb')
motoBin = pickle.load(f)
f.close()

print(motoBin)