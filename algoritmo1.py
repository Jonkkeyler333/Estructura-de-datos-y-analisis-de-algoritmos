def calcular_porcentajes(mujeres:int,hombres:int)->str:
    total=mujeres+hombres
    total_mujeres=(mujeres*100)/total
    total_hombres=(hombres*100)/total
    return f'El numero de mujeres es {total_mujeres} y el número de hombres es {total_hombres}'

print("BIENVENIDO")
try:
    total_mujeres=int(input("por favor ingrese el número total de mujeres  :  "))
    total_hombres=int(input("por favor ingrese el número total de hombres :  "))
except TypeError:
    print("Has ingresado un dato no valido")
    
print(calcular_porcentajes(total_mujeres,total_hombres))