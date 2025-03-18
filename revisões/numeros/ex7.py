"""
Escreva um array de números e retorna o maior valor presente.
"""

import numpy as np

numeros = np.zeros(10,dtype = "i")

for i in range(len(numeros)):
    numeros[i] = input("Insira um numero:")
print(max(numeros))