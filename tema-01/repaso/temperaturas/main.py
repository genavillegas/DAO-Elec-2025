from utilities import generar_temperaturas

temperaturas = generar_temperaturas()
#temperaturas = []

cant_dias_bajo_cero = 0
acum_temp_dias_calidos = 0
prom_temp_dias_calidos = 0
cant_dias_calidos = 0
dia_mayor_cuarenta = False
mayor_temp_nocalidos = 0
cant_dias_temp_menor_prom =0
calidos = []
cuarentas =[]
no_calidos =[]
menor_prom = []
mensaje = "Sin temperaturas a validar"
max = 0
cant_menor_prom =0

try:
    prom_temp = sum(temperaturas)/len(temperaturas)
except ZeroDivisionError:
    prom_temp =0

for temp in temperaturas:
    #Cantidad de días con temperatura bajo cer
    if temp < 0:
        cant_dias_bajo_cero += 1
    
    #Promedio de temperaturas de los días cálidos
    if temp > 20:
        calidos.append(temp)
        acum_temp_dias_calidos += temp
        cant_dias_calidos += 1
    else:
        no_calidos.append(temp)    
        max = temp if temp > max else max
       
   
    #Si/No dia>40
    if temp > 40:
        cuarentas.append(temp)
        dia_mayor_cuarenta = True
    mensaje = "Si" if dia_mayor_cuarenta else "No"
   
    if temp < prom_temp:
        menor_prom.append(temp)
        cant_menor_prom +=1

try:
    prom_temp_dias_calidos = acum_temp_dias_calidos /cant_dias_calidos
except ZeroDivisionError:
    prom_temp_dias_calidos = 0

#Mensajes por consola
print("\n-----------------------------------------------------")
print("Lista de Temperaturas:\n", temperaturas)
print("-----------------------------------------------------")
print(f"\nCantidad de dias con temperatura bajo cero: {cant_dias_bajo_cero}")
print(f"\nPromedio de temperaturas: {prom_temp:6.3f}") 
print(f"\nPromedios de temp de dias calidos (t>20): {prom_temp_dias_calidos:6.3f}")
print(calidos)
print("\nHubo dias con mas de 40 grados: "+ mensaje)
print(cuarentas)
print(f"\nMayor temp de dias no calidos: {max}")
print(no_calidos)
print(f"\nCantidad de dias con temps menores al prom: {cant_menor_prom}")
print(menor_prom)