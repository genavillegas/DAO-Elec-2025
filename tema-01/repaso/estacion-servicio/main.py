from surtidor import *
from procesadores import *

def main():
    #surtidores = generar_surtidores()
    surtidores = cargar_surtidores()
    print("\nSURTIDORES\n")
    for idx, s in enumerate(surtidores, start=1):
        print(f"[{idx:>2d}] - {to_string(s)}")

    cant_uno, cant_dos, cant_tres = calc_total_vendidos(surtidores)
    print("\nCantidad litros vendidos en la jornada: ")
    print(f"Nafta Super: {cant_uno:>7}\n" +
        f"Nafta Especial: {cant_dos:>4}\n"+
        f"GasOil: {cant_tres:>12}")  

    menor_surtidor = buscar_surtidor_menor_venta(surtidores)
    print("\nSurtidor con menor venta:")
    print(to_string(menor_surtidor))

    prom_combustible = calc_prom_combustible(surtidores)
    print(f"\nPromedio de litros vendidos: {prom_combustible}")


# if __name__ == main:
#     main()
main()