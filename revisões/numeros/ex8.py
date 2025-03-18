"""
Crie uma função que calcula a média de uma lista de números.
Restrição: Não use sum()
"""

import numpy as np

numeros = np.zeros(10, dtype = "i")

for i in range(len(numeros)):
    numeros[i] = input("Insira um numero:")
    soma = sum(numeros)
    media = soma / len(numeros)
print(media)