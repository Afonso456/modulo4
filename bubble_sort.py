"""
Implementar a ordenação bubble sort com um array
"""
import numpy as np

numeros= np.array([29,10,37,14,14,30,100,19,80,56])

def bubble_sort(vetor):
    """
    Função que ordena um array usando bubble sort mudando as posições constantemente
    """
    tamanho= len(vetor)
    for i in range(tamanho):
        for j in range(0,tamanho-i-1):
            if vetor[j] > vetor[j+1]:
                t= vetor[j]
                vetor[j]= vetor[j+1]
                vetor[j+1]= t

print(numeros)
bubble_sort(numeros)
print(numeros)