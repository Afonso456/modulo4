"""
Escreva uma função que recebe um array de números e retorna a soma de todos os elementos.
Restrição: Não use sum().
"""

import numpy as np
numeros = np.zeros(10,dtype = "i")
soma = 0

for i in range(len(numeros)):
    numeros[i] = input("Insira um numeros:")
    soma += numeros[i]

print(f"A soma de todos os numeros é de {soma}")