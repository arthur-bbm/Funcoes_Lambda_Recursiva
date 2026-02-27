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

lista = ['ana', 'joao', 'maria', 'carlos']

print(list(map(maiuscula, lista)))


numros = [1,2,3,4,5,6,7,8,9,10]

print(list(map(lambda x: x % 2 == 0, numros)))