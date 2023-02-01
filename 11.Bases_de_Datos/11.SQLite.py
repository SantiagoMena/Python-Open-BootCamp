import getpass
import sqlite3

def main():
    username = input("Nombre de usuario: ")
    password = getpass.getpass('Contraseña: ')

    if verifica_credenciales(username, password):
        print('Login correcto!')
    else:
        print('Login incorrecto!')

def verifica_credenciales(username, password):
    conn = sqlite3.connect('miaplicacion.db')
    cursor = conn.cursor()

    query = f'SELECT * FROM users WHERE username="{username}" AND password ="{password}"'
    rows = cursor.execute(query)

    data = rows.fetchone()

    conn.commit()
    cursor.close()
    conn.close()

    return data != None

def crear_usuario(identificador, username, password):
    conn = sqlite3.connect('miaplicacion.db')
    cursor = conn.cursor()

    query = f'INSERT INTO users(id, username, password) VALUES ({identificador}, "{username}", "{password}")'
    rows = cursor.execute(query)

    data = rows.fetchone()

    cursor.close()
    conn.close()

    return data != None

if __name__ == '__main__':
    main()

print('\nLista de usuarios:\n')
conn = sqlite3.connect('miaplicacion.db')
cursor = conn.cursor()

rows = cursor.execute('SELECT * FROM users')

for row in rows:
    print(row)

cursor.close()
conn.close()