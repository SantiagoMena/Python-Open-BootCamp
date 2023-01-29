class Motor:
    tipo = "Diesel"

class Ventanas:
    cantidad = 5

    def cambiarCantidad(self, cantidad):
        self.cantidad = cantidad

class Ruedas:
    cantidad = 4

class Carroceria:
    ventanas = Ventanas()
    ruedas = Ruedas()

class Coche:
    motor = Motor()
    carroceria = Carroceria()

c = Coche()
print("Motor es:", c.motor.tipo)
print("Ventanas:", c.carroceria.ventanas.cantidad)
c.carroceria.ventanas.cambiarCantidad(4);
print("Ventanas:", c.carroceria.ventanas.cantidad)
