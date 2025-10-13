from validadores import *
import random

class Surtidor:
    def __init__(self, numero, cantidad, tipo):
        self.numero = numero
        self.cantidad = cantidad
        self.tipo = tipo

def generador_aleatorio():
    numero = random.randint(1,30)
    cantidad = random.randint(1,1000)
    tipo = random.randint(1,3)
    return Surtidor(numero, cantidad,tipo) 
  
def to_string(reg):
    return (
        f"Numero: {reg.numero:>2} |  "
        f"Cant litros: {reg.cantidad:>3,d} |  "
        f"Tipo: {reg.tipo:>1}"
    )

def generar_surtidores(cant=10):
    surtidores = []
    nums_usados = set()
    for i in range(cant):
        surtidor = generador_aleatorio()
        while not validar_id_unico(surtidor.numero, nums_usados):
            surtidor = generador_aleatorio()
        surtidores.append(surtidor)
        #print(f"[{i+1:>2d}] - {to_string(surtidor)}")
    #surtidores.sort(key=lambda s: s.cantidad)
    return surtidores
    
def cargar_surtidores(cantidad = 2):
    surtidores = []
    for i in range(cantidad):
        numero = validar_num_entre("Ingrese numero de Surtidor: ",1,30)
        cantidad = validar_num_entre("Ingrese cantidad de litros vendidos: ",1,1000)
        tipo = validar_num_entre("Ingrese tipo de combustible vendido [1:Nafta Super  |  2:Nafta Especial  |  3:GasOil]: ",1,3)
        surtidores.append(Surtidor(numero,cantidad,tipo))
    return surtidores

def prueba():
    print(to_string(generador_aleatorio()))

#prueba()