#Calcular promedio de las temperaturas
def calc_promedio(lista):
    try:
        temp_prom = sum(lista)/len(lista)
    except ZeroDivisionError:
        temp_prom = 0
    return temp_prom

#Cantidad de días con temperatura bajo cero
def calc_cant_dias_bajo_cero(lista):
    temps_bajo_cero = []
    cant_dias_bajo_cero = 0
    for temp in lista:
        if temp < 0:
            temps_bajo_cero.append(temp)
            cant_dias_bajo_cero += 1
    return cant_dias_bajo_cero, temps_bajo_cero

#Promedio de temperaturas de los días cálidos
def calc_prom_temp_dias_calidos(lista, temp_calida=20):
    calidos = []
    for temp in lista:    
        if temp > temp_calida:
            calidos.append(temp)
    try:
        prom_temp_dias_calidos = sum(calidos)/len(calidos)
    except ZeroDivisionError:
        prom_temp_dias_calidos = 0
    return prom_temp_dias_calidos,calidos
        
def buscar_temp_mayor_a(lista,temp_param=40):
    #Si/No dia>40
    cuarentas =[]
    mensaje = "Sin temperaturas a validar"
    for temp in lista:
        if temp > temp_param:
            cuarentas.append(temp)
            dia_mayor_cuarenta = True
    mensaje = "Si" if dia_mayor_cuarenta else "No"
    return  mensaje, cuarentas
   
def buscar_temp_mayor_nocalidos(lista, temp_calida=20):
    max_temp = 0
    no_calidos =[]
    for temp in lista:    
        if temp < temp_calida:
            no_calidos.append(temp)
    max_temp = max(no_calidos)
    return max_temp, no_calidos

def calc_dias_menor_prom(lista):
    prom = calc_promedio(lista)
    for temp in lista:
        if temp < prom:
            cant_menor_prom =+ 1
    return cant_menor_prom
