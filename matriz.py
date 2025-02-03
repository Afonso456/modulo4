"""
Introdução aos arryas de 2 dimensões(matrizes)
"""
import numpy as np

matriz = np.array([[0,1,2],[3,5,0]])

#print da matriz
print(matriz)

#primeiro elemento da matriz
print(matriz[0,0])

#ultimo elemento da matriz
print(matriz[1,2])

#percorrer todos os elementos da matriz
for l in range(2):
    for c in range(3):
        print(matriz[l,c])

#nº de elemntos
print(f"Função len com a matriz: {len(matriz)}")

#nº de colunas 
print("Nº de colunas da matriz:",matriz.shape[1])
#nº de linhas
print("Nº de linhas da matriz:",matriz.shape[0])