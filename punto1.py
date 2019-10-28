## Funcion que calcula los subtotales a pagar por multiples productos
## dadas las cantidades, precios e ivas de los mismos

## Se asume que las tres entradas tienen el mismo tamaño

def calcular_subtotales(cantidades, precios, ivas):
    subtotales = list()

    ## Ciclo para ir calculando el total de cada producto
    i = 0
    while (i < len(cantidades)):
        subtotales.append(cantidades[i]*precios[i]*((100 + ivas[i]) / 100))
        i += 1
        
    return subtotales                                  


## Funcion que calcula la suma de una lista de numeros
def calcular_total(lista_numeros):
    total = 0

    ## Ciclo para ir sumando cada numero al total
    i = 0
    while (i < len(lista_numeros)):
        total += lista_numeros[i]
        i += 1
        
    return total

## Funcion que dadas cuatro listas, representando los valores de unos productos
## generera una factura de compra
def facturar_productos(cantidades, productos, precios, ivas):

    ## Se usa la funcion calcular_subtotales
    subtotales = calcular_subtotales(cantidades, precios, ivas)
    ## Impresion de listas
    ## \n: Salto de linea
    ## Se genera el mensaje a verse en pantalla

    mensaje = "cantidad-producto-precio-iva-total\n"

    i = 0
    while(i < len(subtotales)):
        mensaje += str(cantidades[i]) + "-"
        mensaje += str(productos[i]) + "-"
        mensaje += str(precios[i]) + "-"
        mensaje += str(ivas[i]) + "-"
        mensaje += str(subtotales[i]) + "\n"
        i += 1

    mensaje += "TOTAL:"+str(calcular_total(subtotales)) ## Se calcula el total
    print(mensaje)

facturar_productos([3,2], ["bananos", "manzanas"], [100, 300], [10, 5])
    
    
    
