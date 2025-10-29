import os

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
                mostrar()
                input('Presiona Return ....')
            case '2':
                afegir()
            case '3':
                buscar()
            case '4':
                estadisticas()
            case '5':
                break
    else:
        print('Opcion no valida')
        
        