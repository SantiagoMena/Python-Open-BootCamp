fileDir = __file__
arrayDir = fileDir.split('/')
arrayDir.pop()
dir = '/'.join(arrayDir)
file = 'file.txt'

f = open(dir + '/' + file, 'x')
f.close()

f = open(dir + '/' + file, 'w')
f.write('Hola Mundo!')
f.close

f = open(dir + '/' + file, 'r')
print(f.read())