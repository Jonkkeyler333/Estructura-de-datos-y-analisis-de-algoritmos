def calcular_porcentajes(mujeres:int,hombres:int)->int:
    total=mujeres+hombres
    total_mujeres=(mujeres*100)/total
    total_hombres=(hombres*100)/total
    return f'El numero de mujeres es {total_mujeres} y el número de hombres es {total_hombres}'

