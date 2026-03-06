lista = [1 ,2, 3, 4, 5, 6, 7]

def soma_lista_recursiva(valor) :
    if len(valor) == 0:
        return 0
    return valor[0] + soma_lista_recursiva(valor[1:])

print(soma_lista_recursiva(lista))