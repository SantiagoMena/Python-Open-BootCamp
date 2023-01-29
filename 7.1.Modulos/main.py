from calculadora.calculadora import sumar, restar, multiplicar, dividir

def main():
    operacion = str(input('Ingrese una operacion (sumar / restar / multiplicar / dividir): '))
    valorA = float(input('Ingrese el primer valor: '))
    valorB = float(input('Ingrese el segundo valor: '))
    resultado = 0

    match operacion:
        case 'sumar':
          resultado = sumar(valorA, valorB) 

        case 'restar':
          resultado = restar(valorA, valorB)

        case 'multiplicar':
          resultado = multiplicar(valorA, valorB)

        case 'dividir':
          resultado = dividir(valorA, valorB)
            
    print('El resultado es:', resultado);
    
if __name__ == '__main__':
    main()
