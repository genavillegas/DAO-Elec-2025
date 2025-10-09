import random
from validadores import *

temp_inf = -20  
temp_sup = 50
temperaturas = []

def generar_temperaturas():
    while True:
        temp = random.randint(temp_inf,temp_sup)
        if temp == temp_sup:
            print("Se finaliza la carga - Se generó un 50")
            break
        temperaturas.append(temp)
        #print(temperaturas)  
    return temperaturas

def cargar_temperaturas():
    while True:
        temp = validar_num_entre("Ingrese un valor de temperatura: ",temp_inf,temp_sup)
        if temp == temp_sup:
            print("Se finaliza la carga - Se ingreso un 50")
            break
        temperaturas.append(temp)
        #print(temperaturas)  
    return temperaturas
    

#print(generar_temperaturas())
#print(cargar_temperaturas())
