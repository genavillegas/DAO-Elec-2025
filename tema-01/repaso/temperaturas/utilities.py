import random

temp_limite = 50

def generar_temperaturas():
    temperaturas = []
    while True:
        temp = random.randint(-20,temp_limite)
        if temp == temp_limite:
            break
        temperaturas.append(temp)
        #print(temperaturas)  
    return temperaturas

#print(generar_temperaturas())