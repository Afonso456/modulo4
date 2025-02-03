"""
Definir uma matriz 5,3 e preencher coma multiplicação das linhas com as colunas
"""
import numpy as np

matriz= np.zeros((5,3),dtype= int)

#ciclo para percorrer as linhas
for l in range(matriz.shape[0]):
    for c in range(matriz.shape[1]):
        matriz[l,c] = l * c

print(matriz)