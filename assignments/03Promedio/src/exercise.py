def main():
    #escribe tu código abajo de esta línea
    n1 = float(input('Calificación de la materia: '))
    n2 = float(input('Calificación de la materia: '))
    n3 = float(input('Calificación de la materia: '))
    n4 = float(input('Calificación de la materia: '))

    promedio = ( n1 + n2 + n3 + n4 ) / 4

    print('El promedio es: '+str(promedio))


if __name__ == '__main__':
    main()
