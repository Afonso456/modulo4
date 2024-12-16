"""
Programa que inverte um array de nomes com 5 elementos
"""
import numpy as np

NR_ELEMENTOS= 10
nome= np.empty(NR_ELEMENTOS,dtype= "U15")
for i in range(NR_ELEMENTOS):
    nome[i]= input(f"Introduza um nome: ")


#preencehr o array invertendo as posições
k = NR_ELEMENTOS - 1
for i in range (NR_ELEMENTOS//2):
    temp= nome[i]
    nome[i] = nome[k]
    nome[k] = temp
    k = k - 1

print(nome,temp)
