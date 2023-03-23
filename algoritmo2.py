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
    n_estudiantes=int(input('Por favor ingrese el numero de estudiantes de su curso '))
    if n_estudiantes<=0:
        print('Ha ocurrido un error')
        n_estudiantes=int(input('Por favor ingrese el numero de estudiantes de su curso '))
    
    for j in range(n_estudiantes):
            n1=float(input(f'ingrese la nota 1 del estudiante {j+1} '))
            n2=float(input(f'ingrese la nota 2 del estudiante {j+1} '))
            n3=float(input(f'ingrese la nota 3 del estudiante {j+1} '))
            n4=float(input(f'ingrese la nota 4 del estudiante {j+1} '))
            promedios_estudiante.append(promedio_est(n1,n2,n3,n4))
            print()
    print(estadistica(promedios_estudiante))
            