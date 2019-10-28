

def Reorganizar(lista_elementos, lista_posiciones):
    LE = lista_elementos
    LP = lista_posiciones
    LP.reverse()
    ## La lista de posiciones esta al reves

    nuevo_listado = list() ## Lista vacia
    ## Recorremos el listado de posiciones
    i = 0
    while(i < len(LP)):
        ## Buscamos el elemento que esta en la primera posicion descrita por LP
        ## LP[i] = Una posicion en LE
        elemento = LE[LP[i]]

        ## añadimos el elemento al nuevo listado
        nuevo_listado.append(elemento)
        ##
        i += 1

    return nuevo_listado

print(Reorganizar(["a","b","c","d"], [1,3,0,2]))
        
