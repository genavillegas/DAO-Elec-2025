from generadores import *
from procesadores import *

def principal():
    temperaturas = generar_temperaturas()
    print("\n-----------------------------------------------------")
    print("Lista de Temperaturas:\n", temperaturas)
    print("-----------------------------------------------------")
    
    temp_prom = calc_promedio(temperaturas)
    print(f"\nPromedio de temperaturas: {temp_prom:6.3f}") 

    cant_dias_bajo_cero, temps_bajo_cero = calc_cant_dias_bajo_cero(temperaturas)
    print(f"\nCantidad de dias con temperatura bajo cero: {cant_dias_bajo_cero}\n",temps_bajo_cero)
    
    prom_temp_dias_calidos,calidos= calc_prom_temp_dias_calidos(temperaturas)
    print(f"\nPromedios de temp de dias calidos (t>20): {prom_temp_dias_calidos:6.3f}\n",calidos)

    mensaje, cuarentas=buscar_temp_mayor_a(temperaturas)
    print("\nHubo dias con mas de 40 grados: "+ mensaje + "\n", cuarentas)

    max_temp, no_calidos = buscar_temp_mayor_nocalidos(temperaturas)
    print(f"\nMayor temp de dias no calidos: {max_temp}\n", no_calidos)
    
    cant_menor_prom= calc_dias_menor_prom(temperaturas)
    print(f"\nCantidad de dias con temps menores al prom: {cant_menor_prom}")


if __name__ == "__main__":
    principal()