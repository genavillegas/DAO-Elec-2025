# Total de litros vendidos en la jornada, por tipo de combustible
def calc_total_vendidos(surtidores):
    total1 = total2 =   total3 = 0
    for s in surtidores:
        if s.tipo == 1:
            total1 += s.cantidad
        elif s.tipo == 2:
            total2 += s.cantidad
        elif s.tipo == 3:
            total3 += s.cantidad
        else:  
            pass
    return total1, total2, total3

def buscar_surtidor_menor_venta(surtidores):
    if not surtidores:
        return None
    return min(surtidores, key=lambda s: s.cantidad)

def calc_prom_combustible(surtidores):
    acum_combustible = 0
    for s in surtidores:
        acum_combustible =+ s.cantidad
    return (acum_combustible / len(surtidores))
            

        
            

