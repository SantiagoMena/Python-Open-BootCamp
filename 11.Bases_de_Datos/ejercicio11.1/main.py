import getpass
import sqlite3

def main():
    nombre = str(input("Nombre de alumno: ")).lower()
    print(buscar_alumno(nombre))

def buscar_alumno(nombre):
    conn = sqlite3.connect('alumnos.db')
    cursor = conn.cursor()

    query = f'SELECT * FROM alumnos WHERE LOWER(nombre)="{nombre}"'
    rows = cursor.execute(query)

    data = rows.fetchone()

    cursor.close()
    conn.close()

    if data == None:
        return 'Alumno no encontrado!'

    return f'Alumno encontrado: #{data[0]} {data[1]} {data[2]}'

def crear_alumno(identificador, nombre, apellido):
    conn = sqlite3.connect('alumnos.db')
    cursor = conn.cursor()

    query = f'INSERT INTO alumnos(id, nombre, apellido) VALUES ({identificador}, "{nombre}", "{apellido}")'
    rows = cursor.execute(query)

    data = rows.fetchone()

    conn.commit()
    cursor.close()
    conn.close()

    return data != None

if __name__ == '__main__':
    main()
