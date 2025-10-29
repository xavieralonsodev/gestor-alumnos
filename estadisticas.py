alumnos = [
    {"nombre": "Ana", "edad": 20, "nota": 8.5},
    {"nombre": "Luis", "edad": 22, "nota": 6.9}
]

def estadisticas(alumnos):
    total_notas = 0
    nota_lista = []
    for alumno in alumnos:
        nota_lista.append(alumno['nota'])
        total_notas += alumno['nota']
        media_nota = total_notas / len(alumnos)
        maximo = max(nota_lista)
        minimo = min(nota_lista)
    print(f'La media nota es. {media_nota}')
    print(f'El maximo nota. {maximo}')
    print(f'El minimo nota. {minimo}')
estadisticas(alumnos)            
    