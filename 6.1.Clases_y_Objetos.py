class Vehiculo:
    color: str = None
    ruedas: int = None
    puertas: int = None

    def __init__(self, **args) -> None:
        self.color = args['color']
        self.ruedas = args['ruedas']
        self.puertas = args['puertas']

class Coche(Vehiculo):
    velocidad = None
    cilindraje = None

    def __init__(self, **args) -> None:
        super().__init__(**args)
        self.velocidad = args['velocidad']
        self.cilindraje = args['cilindraje']

color = str(input('Color del auto: '))
ruedas = int(input('Cantidad de ruedas: '))
puertas = int(input('Cantidad de puertas: '))
velocidad = float(input('Velocidad (km/hs): '))
cilindraje = float(input('Cilindraje: '))

coche = Coche(
    color = color, 
    ruedas = ruedas, 
    puertas = puertas, 
    velocidad = velocidad, 
    cilindraje = cilindraje
)

print('Coche de color '+str(coche.color)+' con '+str(coche.ruedas)+' ruedas, velocidad '+str(coche.velocidad)+' kms/hs y '+str(coche.cilindraje)+' de cilindraje.')