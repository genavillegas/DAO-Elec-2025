def validar_num_entre(mensaje, limInf, limSup):
    while True:
        entrada = input(mensaje)
        try:
            valor = int(entrada)
        except ValueError:
            print("-" * 10)
            print("ATENCIÓN! el valor debe ser un número ENTERO")
            print("-" * 10)
            continue
        if valor < limInf or valor > limSup:
            print("-" * 10)
            print(f"ATENCIÓN! el valor debe estar entre {limInf} y {limSup}")
            print("-" * 10)
            continue
        return valor