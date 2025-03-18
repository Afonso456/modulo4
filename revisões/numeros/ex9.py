"""
Crie um array que recebe do utilizador numeros e mostra o produto final desses numero todos junto
Restrição: Não use math.prod().
"""

import numpy as np

numeros = np.zeros(10, dtype ="int")
produto = 1

for i in range(len(numeros)):
    numeros[i] = int(input("Insira um numero:"))
    produto *= numeros[i]
print(produto)