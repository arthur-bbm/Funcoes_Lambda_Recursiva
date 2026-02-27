#Funcao para reajustar o valor para 130%

def calculo_reajuste(valor):
    return valor * 1,3

print(calculo_reajuste(1000))


#Funcao lambda - reajuste

reajuste = lambda x: x * 1,3

print(reajuste(1000))

#Funcao lambda - maiuscula

maiuscula = lambda string: string.upper()

print(maiuscula("leonardo"))