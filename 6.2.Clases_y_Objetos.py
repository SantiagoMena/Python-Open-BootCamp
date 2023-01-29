class Alumno:
    nombre: str = None
    nota: int = 0

    def __init__(self, **args) -> None:
        self.nombre = args['nombre']
        self.nota = args['nota']

    def setNombre(self, nombre: str) -> None:
        self.nombre = nombre

    def setNota(self, nota: int) -> None:
        self.nombre = nota

    def aprobo(self) -> bool:
        return self.nota > 5

    def printNotaAlumno(self) -> str:
        if self.aprobo():
            print('El alumno', self.nombre, 'aprobó con la nota', self.nota)
        else:
            print('El alumno', self.nombre, 'desaprobó con la nota', self.nota)

alumno = Alumno(nombre = 'Santiago', nota = 7)
alumno.printNotaAlumno()
