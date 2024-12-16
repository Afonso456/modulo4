import numpy as np

#definir um array para strings
"""
i- inteiros
f- reais
b-boleanos
S- string
U- unicode string
M- datetime
"""
nomes= np.empty(10,dtype="U20")
for i in range (len(nomes)):
    nomes[i]= input("Introduza um nome:")
print(nomes)