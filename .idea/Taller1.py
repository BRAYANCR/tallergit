def calcular_franja(dia, hora, minuto):
    if dia > 6:
        franja = "Franja C"
    else:
        if (hora > 20) and (hora <= 23)
            franja = "Franja B"
        else
            franja = "Franja A"
    return franja


def precio_comercial(franja, tiempo):
    if franja == "Franja A":
        precio = time * 10000000
    elif franja == "FranjaB":
        precio = time * 8000000
    else:
        precio = time * 12000000
    return precio


def principal():
    empresa = eval(input("Ingrese el nombre de la Empresa \n"))
    dia = input("Ingrese el día del Comercial \n")
    hora = eval(input("Ingrese la hora del Comercial \n"))
    minuto = eval(input("Ingrese el minuto del Comercial \n"))
    tiempo = input("Ingrese la duración del Comercial (En Segundos) \n")
    franja = calcular_franja(dia, hora, minuto)
    precio = precio_comercial(franja, tiempo)
    print("La empresa " empresa " debe pagar " precio " por su comercial en la " franja)


principal()

