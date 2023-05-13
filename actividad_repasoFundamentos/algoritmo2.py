def promedio_est(nota1,nota2,nota3,nota4)->float:
    notas=[nota1,nota2,nota3,nota4]
    sumatoria=0
    for elemento in notas:
        sumatoria+=elemento
    return sumatoria/4

def estadistica(promedios:list)->str:
    sumatoria=0
    promedio_curso=0
    reprobados=0
    for elemento in promedios:
        sumatoria+=elemento
        if elemento<3.0:
            reprobados+=1
    promedio_curso=sumatoria/len(promedios)
    promedios.sort()
    return f'el promedio del curso es {promedio_curso:.2f} \nel promedio mas bajo es {promedios[0]} | el promedio mas alto fue {promedios[len(promedios)-1]} \nen total reprobaron {reprobados} perona/s'

if __name__=="__main__":
    print('Bienvenido')
    promedios_estudiante=[]
    lista_notas=[]
    n_estudiantes=int(input('Por favor ingrese el numero de estudiantes de su curso '))
    if n_estudiantes<=0:
        print('Ha ocurrido un error')
        n_estudiantes=int(input('Por favor ingrese el numero de estudiantes de su curso '))
    for j in range(n_estudiantes):
        i = 1 
        lista_notas = [] 
        while i <= 4:
            n = float(input(f'Ingrese la nota {i} del estudiante {j+1}: '))
            lista_notas.append(n)
            i += 1
        promedios_estudiante.append(promedio_est(*lista_notas))
        print()
        
    print(estadistica(promedios_estudiante))
            