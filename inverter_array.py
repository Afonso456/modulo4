"""
Programa que inverte um array de nomes com 5 elementos
"""
import numpy as np

NR_ELEMENTOS= 10
nome= np.empty(NR_ELEMENTOS,dtype= "U15")
for i in range(NR_ELEMENTOS):
    nome[i]= input(f"Introduza um nome: ")

#criar um array para os nomes invertidos
nome_invertido= np.empty(NR_ELEMENTOS,dtype= "U15")

#preencehr o array invertendo as posições
k = NR_ELEMENTOS - 1
for i in range (NR_ELEMENTOS):
    nome_invertido[k] = nome[i]
    k = k - 1

print(nome,nome_invertido)
