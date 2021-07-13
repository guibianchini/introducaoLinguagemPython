# -*- coding: utf-8 -*-
#Lista - Criação, Comparação, Exclusão
minha_lista = ["abacaxi","melancia","abacate"]
minha_lista_2 = [1,2,3,4,5]
minha_lista_3 = ["abacaxi",2,9.89,True]

minha_lista.append("limão")

print(minha_lista)

if 3 in minha_lista_2:
    print("3 está na lista")

del minha_lista[2:]
print(minha_lista)
