"""
Programa que lê as matriculas dos carros e indica as que estão repetidas
"""
import numpy as np
marcas= np.array(10,dtype= "U10")
carros=np.array(["bmw","mercedes","audi","bmw","bmw","bmw","mercedes","mercedes","mercedes","mercedes"])
NR_MAX= 10

for i in carros:
    n= 0
    if i in carros:
        print(i)
        continue
    marcas[i] = carros
    n += 1
    contar = 0
    for j in carros:
        if i == j:
            contar += 1
    print(f"A marca {carros} aparece {contar} vezes")