"""
Criar um array com 10 elementos em que cada elemento é o dobro do indice da sua posição
"""
import numpy as np 

numero= np.empty(10)
NR_ELEMENTOS= 10

for i in range(NR_ELEMENTOS):
    numero[i]= [i] * 2

print(numero)