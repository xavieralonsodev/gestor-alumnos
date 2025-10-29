# Módulo que contiene las funcionalidades que trabajan con la lista de alumnos.
# Funciones que contendrá este módulo: afegir, mostrar, buscar (por nombre).

def pedir_entero(mensaje, minimo = None, maximo = None):
    while True:
        try:
            valor = int(input(mensaje))
            if minimo is not None and valor < minimo: continue
            if maximo is not None and valor > maximo: continue
            return valor
        except ValueError:
            print('Introduce un número válido')

def pedir_float(mensaje, minimo = None, maximo = None):
    while True:
        try:
            valor = float(input(mensaje))
            if minimo is not None and valor < minimo: continue
            if maximo is not None and valor > maximo: continue
            return valor
        except ValueError:
            print('Introduce un número válido')

def afegir ( lista_alumnos ):
# Función que le pide al usuario: nombre (str), edad(int) y nota(float), las valida y, si son correctas, añade el alumno a lista_alumnos.

    print('\nIntroduzca los valores requeridos para dar de alta al nuevo alumno en el sistema.')
    try:
        nombre = input('Instroduzca el nombre del nuevo alumno: ').strip()
    except ValueError:
        print('Error: nombre no válido.')
        return

    edad = pedir_entero('\nIntroduzca la edad del nuevo alumno: ',1,100)
    nota = pedir_float('\nIntroduzca la nota del nuevo alumno: ',0,10.0)

    lista_alumnos.append({ 'nombre':nombre, 'edad':edad, 'nota':nota })

def mostrar ( lista_alumnos ):
# Función que recibe una lista de diccionarios que contienen los datos de los alumnos.
# Muestra por pantalla la lista de alumnos con sus datos, desglosada.

    for i, alumno in enumerate(lista_alumnos):
        print(f'{i+1}.- {alumno['nombre']}, nota: {alumno['nota']}')

def buscar ( lista_alumnos ):
# Función que recibe una lista de diccionarios que contienen los datos de los alumnos.
# Pregunta al usuario por un nombre y printa todos los alumnos cuyo 'nombre' sea igual a ese valor.
# Se estandariza el input y los nombres con los métodos .strip().lower()

    try:
        nombre = input('\nIntroduzca el nombre de los alumnos a buscar: ').strip().lower()
        if not nombre:
            print('\nError: el nombre a buscar no puede ser una cadena vacía.')
        else:
            encontrado = False
            for alumno in lista_alumnos:
                if alumno['nombre'].strip().lower() == nombre:
                    encontrado = True
                    print(f'Alumno: {alumno['nombre']}, edad: {alumno['edad']}, nota: {alumno['nota']}')
            if not encontrado:
                print('\nAlumno no encontrado en el sistema.')
    except ValueError:
        print('\nError: nombre no válido.')