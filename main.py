import os
import funciones_alumnos as func
import estadisticas as est

alumnos = [
    {"nombre": "Ana", "edad": 20, "nota": 8.5},
    {"nombre": "Luis", "edad": 22, "nota": 6.9}
]
while True:
    os.system('cls')
    print('''
        Opcion 1. Ver lista de alumnos
        Opcion 2. Añadir un nuevo alumno
        Opcion 3. Buscar un alumno por nombre
        Opcion 4. Mostrar estadísticas del grupo
        Opcion 5.- Salir 
          ''')
    
    opcion = input('Introduzca la opción (1-5)  :')
    if 0 < int(opcion) <= 5:
        match opcion:
            case '1':
                func.mostrar(alumnos)
                input('Presiona Return ....')
            case '2':
                func.afegir(alumnos)
            case '3':
                func.buscar(alumnos)
            case '4':
                est.estadisticas(alumnos)
            case '5':
                break
    else:
        print('Opcion no valida')
        
        